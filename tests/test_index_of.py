from project_testing_2.index_of import index_of


def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([], 2) == -1
    assert index_of([2, 7, 3, 2, 4], 2, from_index=-1) == -1
    assert index_of([2, 7, 3, 2, 4], 2, from_index=-8) == 0
