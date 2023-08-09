# Any pytest file should start with test_ or end with _test
# pytest methods should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method name execution, -s logs in output, - v stands for more data metadata
# You can run specific file with py.test <file name>
#@pytest.mark.xfail if we want the test case to run but not display the result.
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")
    print("HelloA")
    print("HelloB")
    print("HelloC")
    print("HelloD")
    print("HelloE")
    print("Hi")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")
    print("Good MorningA")
    print("Good MorningB")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])





