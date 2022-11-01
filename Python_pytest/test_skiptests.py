import sys
import pytest
pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason='Not work on py version above 3.6')

def test_case01():
    assert 5 ** 2 == 25

def test_case02():
    assert 1


@pytest.mark.skip(reason='This is an negative test')
def test_case03():
    assert False

@pytest.mark.skipif((sys.version_info) > (3,6), reason='Not work on py version above 3.6')
def test_case04():
    5 // 2 == 2

@pytest.mark.skipif()
def test_case05():
    1 in divmod(9, 5)