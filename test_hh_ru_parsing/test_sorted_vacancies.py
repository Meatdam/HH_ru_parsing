import pytest
from src.sorted_vacancies import SortedVacancies
from src.conection_head_hunter import HeadHunter


@pytest.fixture
def test_head_hunter():
    HeadHunter('python', 1)


def test_head_hunter_sorted():
    r = SortedVacancies()
    assert r.head_hunter_sorted == []
    assert r.date_format == None


def test_sorted_vacancies():
    r = SortedVacancies()
    assert r.sorted_vacancies_hh == [{'city': 'Оренбург',
                                      'date': '29.01.2024',
                                      'id': '92363159',
                                      'name': 'Стажер-разработчик Python',
                                      'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть '
                                                     'активным и внедрять эффективные решения.',
                                      'responsibility': 'Внедрять новые инженерные решения. Поддерживать текущий '
                                                        'проект. Разработка десктоп ПО по нашим лекалам.',
                                      'salary_from': 50000,
                                      'salary_to': 50000}]


def test_error_sorted_vacancies():
    with pytest.raises(TypeError):
        SortedVacancies(100)
