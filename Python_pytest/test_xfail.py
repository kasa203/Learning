import pytest
import sys

def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


#this is a failed test
def test_a2():
    assert 9//5 == 1.5, 'failed test'


@pytest.mark.xfail(reason='Known issue')
def test_a3():
    assert 9//5 == 1 #, 'failed test'


@pytest.mark.xfail(sys.platform!='win32',reason='works only in win32')
def test_a3():
    assert 9 // 5 == 1  # , 'failed test'