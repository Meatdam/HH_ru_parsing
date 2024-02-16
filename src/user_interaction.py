from src.debug_user_json import DebugUserJson
from src.conection_head_hunter import HeadHunter
from src.hh_request_debug import HHRequestDebug
from src.sorted_vacancies import SortedVacancies


class UserInteractionHHunter(HHRequestDebug):
    """
    Класс взаимодействия с пользователем, отправка запроса в Head Hanter (Наследуется от класса формы HHRequestDebug)
    :return: json файл с данными
    """

    def hh_user_search(self):
        """
        Ввод пользователя поиска запроса и количество объявлений
        :return: json файл запроса
        :rtype: json
        """
        search_query = self.user_input_value_str()
        top_n = self.user_input_int()
        result_search = HeadHunter(search_query, top_n)
        result_search.to_json()


class UserInteractionJson(DebugUserJson):
    """
    Класс взаимодействия с пользователем, сортировка зарплаты и города (Наследуется от класса формы DebugUserJson)
    :return: Готовый рзультат запроса
    """

    def json_user_search(self):
        vacancies_list = []
        json_file = SortedVacancies()
        json_vacancies = json_file.sorted_vacancies_hh
        salary_from = self.user_input_int()
        user_city = self.user_input_value_str()

        for vacaincies in json_vacancies:
            if salary_from > vacaincies['salary_from']:
                continue
            if user_city == vacaincies['city']:
                vacancies_list.append(vacaincies)
            if user_city == '':
                vacancies_list.append(vacaincies)

        for result in vacancies_list:
            print(f"id: {result['id']}\nГород: {result['city']}\nДата публикации: {result['date']}\n"
                  f"Должность: {result['name']}\nТребование: {result['requirement']}\n"
                  f"Ответственность: {result['responsibility']}\nЗарплата от {result['salary_from']}\n")
        if len(vacancies_list) == 0:
            print(f'Резельтатов 0')


if __name__ == '__main__':
    r = UserInteractionJson()
    r.json_user_search()
