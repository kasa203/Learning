
def test_a1():
    assert 4 != 5

def test_a2():
    assert 0
    assert False
    assert 1
    assert True

def test_a3():
    assert "abcd" == 'abcd'
    assert 0 == False

def test_a4():
    assert ((3-1)*4/2) == 4.0

def test_a5():
    assert 1 in divmod(9, 5) #(1,4) - '1' result of devision 9/5, 4 is the result remainder of this devision
    assert 'py' in 'this is pytest'
    assert 2 in [1,2,4]
    assert [1,2] < [1,2,4]