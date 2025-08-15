import pytest
a = 10
b = 4

@pytest.fixture
def setup_teardown():
    print("this is a 2nd setup operation!!")
    yield "2nd setup complete"
    print("this is a teardown operation!!")

@pytest.mark.basicmath
def test_addition(setup, setup_functionscope, setup_modulescope, setup_sessionscope):
    assert setup=="setup complete"
    print(" The addition is: ", a+b)

@pytest.mark.basicmath
def test_substraction(setup_teardown, setup_functionscope, setup_modulescope, setup_sessionscope):
    assert setup_teardown == "2nd setup complete"
    print(" The substraction is: ", a - b)

@pytest.mark.skip
def test_multiplication(setup, setup_teardown, setup_functionscope, setup_modulescope, setup_sessionscope):
    assert setup == "setup complete"
    assert setup_teardown == "2nd setup complete"
    print(" The multiplication is: ", a * b)

@pytest.mark.basicmath
def test_division(setup, setup_teardown, setup_functionscope, setup_modulescope, setup_sessionscope):
    assert setup == "setup complete"
    assert setup_teardown == "2nd setup complete"
    print(" The division is: ", a / b)