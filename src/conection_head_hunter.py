import json
from config import FILE
import requests
from src.api_vacancies import APIVacancies
from src.vacancies import Vacancy


class HeadHunter(Vacancy, APIVacancies):
    """
    Класс для коннекта пользователя с сайтом Head Hunter
    """

    def __init__(self, name, top_n):
        super().__init__(name, top_n)
        self.top_n = top_n
        self.url = 'https://api.hh.ru'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.top_n})"

    @property
    def get_vacancies(self):
        """Выгрузка данных по 'HeadHunter' по запросам пользователя и
        возвращается словарь"""
        try:
            data = requests.get(f"{self.url}/vacancies",
                                params={'text': self.name,
                                        'area': 113,
                                        'enable_snippets': "true",
                                        'only_with_salary': "true",
                                        'per_page': self.top_n}).json()
            return data
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])

    def to_json(self):
        """Создает json файл с данными о канале"""
        with open(FILE, "w", encoding='utf-8') as file:
            file.write(json.dumps(self.get_vacancies, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    r = HeadHunter('python', 1)
    print(r.to_json())
