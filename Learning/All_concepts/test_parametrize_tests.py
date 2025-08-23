import pytest

@pytest.mark.parametrize("input", [2, 4, 8, 10, 18])
def test_even_numbers(input):
    assert input%2 == 0

@pytest.mark.parametrize("input1, input2, expected_output", [(1, 2, 3), (3, 9, 12), (0,0,0), (100, 0, 100)])
def test_addition(input1, input2, expected_output):
    assert input1 + input2 == expected_output

@pytest.mark.parametrize("d", [{"name": "Wasim"}, {"name": "Almas"}])
def test_parameterize_dict(d):
    print("my name is", d["name"])