import pytest
from algoritmos_ordenamiento.Ejercicio1 import bubble_sort

def test_bubble_sort_with_small_list_returns_ordered_list():
    #Arrange
    input_list = [5, 1, 4, 2, 8, 3]
    #Act
    result = bubble_sort(input_list)
    #Assert
    assert result == [1, 2, 3, 4, 5, 8]

def test_bubble_sort_with_big_list_returns_ordered_list():
    #Arrange
    input_list = [42, 17, 8, 99, 23, 56, 4, 71, 12, 65, 31, 3, 88, 50]
    #Act
    result = bubble_sort(input_list)
    #Assert
    assert result == [3, 4, 8, 12, 17, 23, 31, 42, 50, 56, 65, 71, 88, 99]

def test_bubble_sort_with_empty_list_returns_empty_list():
    #Arrange
    input_list = []
    #Act
    result = bubble_sort(input_list)
    #Assert
    assert result == []

def test_bubble_sort_with_invalid_parameter_fail():
    #Arrange
    input_list = "[3, 4, 8, 12, 17, 23, 31, 42, 50, 56, 65, 71, 88, 99]"
    #Act #Assert
    with pytest.raises(TypeError):
        bubble_sort(input_list)
    