import pytest
from middle import get_middle

def test_get_middle():
    assert get_middle("blue") == "lu"
    assert get_middle("red") == "e"
