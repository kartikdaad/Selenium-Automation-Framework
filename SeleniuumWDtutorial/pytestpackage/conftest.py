import pytest
@pytest.yield_fixture()
def setUp():
    print("Running Conftest demo setUp")
    yield
    print("Running Conftest demo tearDown")
@pytest.yield_fixture(scope="class")
def OneTimeSetUp(browser, osType):
    print("Running Conftest demo setUp one time")
    if browser == 'firefox':
        print("Running test on Firefox")
    else:
        print("Running on Chrome")
    yield
    print("Running Conftest demo tearDown one time")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")