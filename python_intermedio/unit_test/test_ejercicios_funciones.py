import pytest
from ejercicios_funciones import sum_numbers, reverse_string, count_upper_and_lower_letters, order_words, get_prime_numbers

def test_sum_numbers_with_a_list_returns_the_sum_of_the_numbers():
    #Arrange
    input_list = [4, 6, 2, 29]
    #Acct
    result = sum_numbers(input_list)
    #Assert
    assert result == 41

def test_sum_numbers_with_a_list_of_a_number_returns_same_number():
    #Arrange
    input_list = [4]
    #Acct
    result = sum_numbers(input_list)
    #Assert
    assert result == 4

def test_sum_numbers_with_invalid_parameter_returns_fail():
    #Arrange
    input_list = "[4, 6, 2, 29]"
    #Acct #Assert
    with pytest.raises(TypeError):
        sum_numbers(input_list)

def test_reverse_string_with_a_string_returns_the_reverse():
    #Arrange
    input_list = "Hola mundo"
    #Acct
    result = reverse_string(input_list)
    #Assert
    assert result == "odnum aloH"

def test_reverse_string_with_a_character_returns_the_same_character():
    #Arrange
    input_list = "a"
    #Acct
    result = reverse_string(input_list)
    #Assert
    assert result == "a"

def test_reverse_string_with_invalid_parameter_fail():
    #Arrange
    input_list = 1
    #Acct #Assert
    with pytest.raises(TypeError):
        reverse_string(input_list)

def test_count_upper_and_lower_letters_with_a_string_returns_the_count_of_upper_and_lowers():
    #Arrange
    input_list = "Hola mundo"
    #Acct
    result = count_upper_and_lower_letters(input_list)
    #Assert
    assert result == "There's 1 upper cases and 8 lower cases"

def test_count_upper_and_lower_letters_with_a_empty_string_returns_cero_of_upper_and_lowers():
    #Arrange
    input_list = ""
    #Acct
    result = count_upper_and_lower_letters(input_list)
    #Assert
    assert result == "There's 0 upper cases and 0 lower cases"

def test_count_upper_and_lower_letters_with_invalid_parameter_fail():
    #Arrange
    input_list = 1
    #Acct #Assert
    with pytest.raises(TypeError):
        count_upper_and_lower_letters(input_list)

def test_order_words_with_unordered_words_returns_the_words_ordered():
    #Arrange
    input_list = "python-variable-funcion-computadora-monitor"
    #Acct
    result = order_words(input_list)
    #Assert
    assert result == "computadora-funcion-monitor-python-variable"

def test_order_words_with_empty_string_returns_empty():
    #Arrange
    input_list = ""
    #Acct
    result = order_words(input_list)
    #Assert
    assert result == ""

def test_order_words_with_invalid_parameter_fail():
    #Arrange
    input_list = True
    #Acct #Assert
    with pytest.raises(AttributeError):
        order_words(input_list)


def test_get_prime_numbers_with_a_list_of_numbers_returns_a_list_with_primes():
    #Arrange
    input_list = [1, 4, 6, 7, 13, 9, 67]
    #Acct
    result = get_prime_numbers(input_list)
    #Assert
    assert result == [7, 13, 67]

def test_get_prime_numbers_with_a_list_of_no_prime_numbers_returns_a_empty_list():
    #Arrange
    input_list = [1, 4, 6, 9]
    #Acct
    result = get_prime_numbers(input_list)
    #Assert
    assert result == []

def test_get_prime_numbers_with_invalid_parameter_fail():
    #Arrange
    input_list = True
    #Acct #Assert
    with pytest.raises(TypeError):
        get_prime_numbers(input_list)