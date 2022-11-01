import pytest

pytestmark = [pytest.mark.smoke]

@pytest.mark.smoke
def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

#this is a failed test
@pytest.mark.str
def test_a2():
    assert 9//5 == 1.5, 'failed test'

@pytest.mark.str
@pytest.mark.sanity
def test_a3():
    assert 9//5 == 1 #, 'failed test'



#Running - pytest -v -m sanity
#Running - pytest -v -m 'sanity and not str'
#Running - pytest -v -m 'not str'
#Running - pytest -v -m 'sanity and str'
#Running - pytest -v -m 'sanity or str'