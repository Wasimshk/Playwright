import pytest
@pytest.fixture(scope="module")
def setup_driver():
    print("setup web driver")

@pytest.fixture
def open_browser():
    print("Opening browser")
    login = "start login"
    yield login
    print("close browser")

@pytest.mark.smoke
def test_browser1(setup_driver, open_browser):
    assert open_browser == "start login"

def test_browser2(setup_driver, open_browser):
    assert "login" in open_browser