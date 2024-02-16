from abc import ABC, abstractmethod


class APIVacancies(ABC):
    """
    Абстрактный класс для получения API
    """

    @abstractmethod
    def get_vacancies(self):
        pass
