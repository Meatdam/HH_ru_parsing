import pytest
from src.conection_head_hunter import HeadHunter


@pytest.fixture
def test_conection_head_hunter():
    return HeadHunter('python', 1)


def test_str(test_conection_head_hunter):
    assert str(test_conection_head_hunter) == 'python'


def test_repr(test_conection_head_hunter):
    test_repr_conection = test_conection_head_hunter
    assert repr(test_repr_conection) == 'HeadHunter(python, 1)'


def test_url(test_conection_head_hunter):
    assert test_conection_head_hunter.url == 'https://api.hh.ru'


def test_error_conecction():
    with pytest.raises(TypeError):
        HeadHunter()
