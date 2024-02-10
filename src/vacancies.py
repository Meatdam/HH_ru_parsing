import requests
from abc import ABC, abstractmethod
from pprint import pprint


class APIVacancies(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class Vacancy:
    def __init__(self, name, page, top_n):
        self.name = name
        self.page = page
        self.top_n = top_n

    def __repr__(self):
        return f"{self.name}"


class HeadHunter(Vacancy, APIVacancies):
    def __init__(self, name, page, top_n):
        super().__init__(name, page, top_n)
        self.url = 'https://api.hh.ru'

    def get_vacancies(self):
        """Выгрузка данных по 'HeadHunter' по запросам пользователя и
        возвращается словарь"""
        data = requests.get(f"{self.url}/vacancies",
                            params={'text': self.name,
                                    'page': self.page,
                                    'per_page': self.top_n}).json()
        return data


r = HeadHunter('python', 1, 40)
pprint(r.get_vacancies())
