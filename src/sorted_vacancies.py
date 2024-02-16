from datetime import datetime
from pprint import pprint

from config import FILE
import json


class SortedVacancies:
    """
    Работа с Json файлом, сортировка
    :return: Корректные данные по запросу пользователя
    """

    def __init__(self):
        self.head_hunter_sorted = []
        self.date_format = None

    @property
    def sorted_vacancies_hh(self):
        """
        Сортировка Json файла в корректные данные, даты и основной информации
        :return: str[{id, name, salary_from, salary_to, requirement, responsibility, data}]
        :rtype: str
        """

        with open(FILE, encoding='utf-8') as file:
            content = json.load(file)
        for i in content['items']:
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                date = datetime.strptime(i["published_at"], "%Y-%m-%dT%H:%M:%S+%f")
                self.date_format = f"{date:%d.%m.%Y}"
            self.head_hunter_sorted.append({
                "id": i["id"],
                "name": i["name"],
                "city": i["area"]["name"],
                "salary_from": i["salary"]["from"],
                "salary_to": i["salary"]["to"],
                "requirement": i["snippet"]["requirement"],
                "responsibility": i["snippet"]["responsibility"],
                "date": self.date_format
            })

        return self.head_hunter_sorted


if __name__ == '__main__':
    r = SortedVacancies()
    pprint(r.sorted_vacancies_hh)
