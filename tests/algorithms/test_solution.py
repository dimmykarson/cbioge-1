import pytest

from cbioge.algorithms import GESolution

def test_create_solution_from_list():
    solution = GESolution([[0,0],[0,0,0],[0]])
    assert solution.genotype == [[0,0],[0,0,0],[0]]

def test_create_solutino_from_json():
    json_string = {
        'id': None, 
        'genotype': [[1, 1], [1, 1, 1], [1]], 
        'phenotype': None, 
        'fitness': -1, 
        'evaluated': False, 
        'time': None, 
        'params': None
    }
    solution = GESolution(json_data=json_string)
    assert solution.to_json() == json_string

@pytest.mark.parametrize("genA, genB, expected", [
    ([[0,0],[0,0,0],[0]], [[0,0],[0,0,0],[0]], True),
    ([[0,0],[0,0,0],[0]], [[0,0],[0,0,0],[1]], False),
    ([[0,0],[0,0,0],[0]], 'copy', True),
    ([[0,0],[0,0,0],[0]], 'json', True),
    ([[0,0],[0,0,0],[0]], None, False),
    ([[0,0],[0,0,0],[0]], [], False)])
def test_eq_override(genA, genB, expected):
    objA = GESolution(genA)
    if genB == 'copy':
        objB = objA.copy()
    elif genB == 'json':
        objB = GESolution(json_data=objA.to_json())
    else:
        objB = GESolution(genB)
    
    assert (objA == objB) == expected

def test_modified_copy():
    solA = GESolution([[0], [0], [0], [0]])
    solB = solA.copy()

    assert solA == solB
    solB.genotype[0] = 1
    assert solA != solB

def test_modified_deepcopy():

    solA = GESolution([[0], [0], [0], [0]])
    solB = solA.copy(deep=True)

    assert solA == solB
    assert solA.to_json() == solB.to_json()

    solB.fitness = 999
    assert solA == solB
    assert solA.to_json() != solB.to_json()

def test_solution_in_list():

    aux_list = [GESolution([[0], [0], [0], [0]])]
    new_solution = GESolution([[0], [0], [0], [0]])
    ref_solution = aux_list[0]
    cpy_solution = aux_list[0].copy()
    dpy_solution = aux_list[0].copy(deep=True)
    mod_solution = aux_list[0].copy()
    mod_solution.genotype[0] = 1

    assert new_solution in aux_list
    assert ref_solution in aux_list
    assert cpy_solution in aux_list
    assert dpy_solution in aux_list
    assert mod_solution not in aux_list