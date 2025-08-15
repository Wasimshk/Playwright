import pytest


@pytest.fixture(scope="session")
def open_browser():
    print("Opening browser: I am session scope fixture")

@pytest.fixture(scope="function")
def setup():
    print("this is a setup operation!!")
    return "setup complete"

@pytest.fixture(scope="function")
def setup_functionscope():
    print("this is a setup_functionscope operation!!")
    return "setup complete"

@pytest.fixture(scope="module")
def setup_modulescope():
    print("this is a setup_modulescope operation!!")
    return "setup complete"

@pytest.fixture(scope="session")
def setup_sessionscope():
    print("this is a setup_sessionscope operation!!")
    return "setup complete"

