'''
DSGE para CIFAR 10

epochs 10
batch 32

pop 20
evals 500
selection 5
halfandhalf 60/40
elitism 0.25

'''
import os

from cbioge.algorithms.dsge import GrammaticalEvolution
from cbioge.algorithms.selection import TournamentSelection
from cbioge.algorithms.crossover import DSGECrossover
from cbioge.algorithms.mutation import DSGENonterminalMutation
from cbioge.algorithms.operators import ElitistReplacement, HalfAndHalfOperator

from cbioge.datasets.dataset import read_dataset_from_pickle
from cbioge.grammars import Grammar
from cbioge.problems import CNNProblem

from cbioge.utils.model import *
from cbioge.utils import checkpoint as ckpt
from cbioge.utils.experiments import check_os


def run_evolution():

    # check if Windows to limit GPU memory and avoid errors
    check_os()

    ckpt.ckpt_folder = os.path.join('exp_cifar10', str(os.getpid()))

    dataset = read_dataset_from_pickle('data/cifar10.pickle')
    parser = Grammar('data/cnn.json')
    problem = CNNProblem(parser, dataset)

    problem.epochs = 10
    problem.batch_size = 32
    problem.timelimit = 3600 #1h
    problem.workers = 4
    problem.multiprocessing = 1

    problem.train_size = 100
    problem.valid_size = 100
    problem.test_size = 100

    algorithm = GrammaticalEvolution(problem, parser)
    algorithm.pop_size = 20
    algorithm.max_evals = 60
    algorithm.selection = TournamentSelection(t_size=5, maximize=True)
    algorithm.replacement = ElitistReplacement(rate=0.25, maximize=True)
    algorithm.crossover = HalfAndHalfOperator(
        op1=DSGECrossover(cross_rate=1.0), 
        op2=DSGENonterminalMutation(mut_rate=1.0, parser=parser, end_index=4), 
        rate=0.6)

    # 0 - sem log
    # 1 - log da evolução
    # 2 - log do problema
    # 3 - log da gramatica
    verbose = 0
    algorithm.verbose = verbose > 0
    problem.verbose = verbose > 1
    parser.verbose = verbose > 2

    population = algorithm.execute(checkpoint=False)

    # remove and add better post-run
    population.sort(key=lambda x: x.fitness, reverse=True)
    for s in population:
        print(s.fitness, s)


if __name__ == '__main__':
    run_evolution()