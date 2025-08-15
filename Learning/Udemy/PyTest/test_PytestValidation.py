import pytest
# @pytest.fixture
# def open_browser():
#     print("Opening browser")
#
# def test_browser(open_browser):
#     assert open_browser == "browser_instance"

# @pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def preWork():
    print("I am module scope fixture")


@pytest.mark.smoke
def test_inititalCheck(preWork):
    print("This is first test")
@pytest.mark.skip
def test_inititalCheck2(open_browser):
    print("This is second test")

# @pytest.mark.parametrize
def test_inititalCheck3(open_browser):
    pass

