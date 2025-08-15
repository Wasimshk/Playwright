import pytest


@pytest.fixture
def setup():
    print("//////////////Browser Setup/////////////////////")
    return "Setup Something"

def test_example(setup):
    print("///////////////this is a test function Example/////////////////////////")
    assert "Setup" in setup

def test_example2(browser_setup):
    print("///////////////this is a test function Example22/////////////////////////")
