from project_testing_2.slice import my_slice


def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5, 6], 1) == [2, 3, 4, 5, 6]
    assert my_slice([], 1, 3) == []
    assert my_slice([1, 2, 3, 4, 5, 6], -3, 5) == [4, 5]
    assert my_slice([1, 2, 3, 4, 5, 6], -10, 5) == [1, 2, 3, 4, 5]
