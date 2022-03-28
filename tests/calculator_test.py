"""Testing the Calculator"""
# From specifies the namespace
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Mult, Division as Div



def tuple_list():
    """Arranging Data for AAA Testing"""
    return 1.0, 2


def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method

    ## Act for AAA testing
    result = Add.add(tuple_list()[0], tuple_list()[1])

    ## Assertion for AAA testing
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert Sub.subtract(tuple_list()[0], tuple_list()[1]) == -1


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    assert Mult.multiply(tuple_list()[0], tuple_list()[1]) == 2


def test_calculator_division_method():
    """Testing the Calculator Subtract"""
    assert Div.divide(tuple_list()[0], tuple_list()[1]) == 0.5
