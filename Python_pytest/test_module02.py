

class TestMyStuff():
    def test_type(self):
        assert type(1) == int

    def test_starts(self):
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'