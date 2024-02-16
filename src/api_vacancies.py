from abc import ABC, abstractmethod


class APIVacancies(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass
