# Any pytest file should start with test_ or end with _test
# pytest methods should start with test
# Any code should be wrapped in method only
#you can mark (tag) tests and @pytest.mark.smoke then run with -m
#You can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize
# fixtures and  make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with rerurn statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end.
# (interview questions. Queries Email: mentor@rahulshettyacademy.com)

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because the strings do not match"


def test_SecondCreditCard():
    a = 4
    b =6
    assert a+2 == 6, "Addition does not match"


@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixture demo method")