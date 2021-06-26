import logging, os, warnings
warnings.filterwarnings("ignore")

from cbioge.datasets.dataset import read_dataset_from_pickle
from cbioge.grammars import Grammar
from cbioge.problems import CNNProblem

from cbioge.algorithms.dsge import GrammaticalEvolution
from cbioge.algorithms.selection import TournamentSelection
from cbioge.algorithms.crossover import DSGECrossover
from cbioge.algorithms.mutation import DSGENonterminalMutation
from cbioge.algorithms.operators import ElitistReplacement, HalfAndHalfOperator

from cbioge.utils import checkpoint as ckpt
from cbioge.utils import experiments as exp
from cbioge.utils.experiments import check_os

def run_evolution():

    # defines the checkpoint folder
    ckpt.ckpt_folder = exp.get_simple_args('c10res').checkpoint

    problem = CNNProblem(
        Grammar('data/grammars/res_cnn.json'), 
        read_dataset_from_pickle('data/datasets/cifar10.pickle'), 
        batch_size=128, 
        epochs=1, 
        workers=2, 
        multiprocessing=True)
    problem.train_size = 10
    problem.valid_size = 10

    algorithm = GrammaticalEvolution(problem, problem.parser, 
        pop_size=20, 
        max_evals=100, 
        selection=TournamentSelection(t_size=5, maximize=True), 
        crossover=HalfAndHalfOperator(
            op1=DSGECrossover(cross_rate=1.0), 
            op2=DSGENonterminalMutation(mut_rate=1.0, parser=problem.parser, end_index=7), 
            rate=0.6), 
        replacement=ElitistReplacement(rate=0.25, maximize=True), 
        verbose=False)

    population = algorithm.execute(checkpoint=True)

    population.sort(key=lambda x: x.fitness, reverse=True)
    for s in population:
        print(f'{float(s.fitness):.2f}', s)

    print('UNIQUE SOLUTIONS', len(algorithm.all_solutions))


if __name__ == '__main__':
    logging.getLogger('tensorflow').disabled = True
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    check_os()
    run_evolution()
    #test_validity()