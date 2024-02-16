from src.vacancies import Vacancy
import pytest


@pytest.fixture
def test_vacancies():
    return Vacancy('python', 1)


def test_repr_vacancies(test_vacancies):
    assert repr(test_vacancies) == "Vacancy('python', '1)"


def test_str_vacancies(test_vacancies):
    assert str(test_vacancies) == 'python'


def test_name_error(test_vacancies):
    with pytest.raises(AttributeError):
        test_vacancies.name = 'word'


def test_page_error(test_vacancies):
    with pytest.raises(AttributeError):
        test_vacancies.page = 1
