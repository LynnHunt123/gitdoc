from script import Meownir
import pytest

@pytest.fixture
def my_cat():
    return Meownir()

def test_meownir_behavior(my_cat):
    assert my_cat.purr() == "purrrr"
    assert my_cat.meow() == "WrrMeow"
