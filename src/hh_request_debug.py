from src.user_form import UserForm


class HHRequestDebug(UserForm):
    """
    Отладка всех возможных ошибок во время запроса пользователя
    """
    search_query = None
    top_n = None

    def user_input_int(self):
        """
        Отладка ошибок при вводе запроса топа вокансий
        :return: корректный запрос пользователя, либо вид ошибки
        :rtype: integer
        """
        self.top_n = input("Введите количество вакансий для вывода в топ N: ")
        if self.top_n.isalpha():
            raise ValueError('Количество не может быть строкой')
        if self.top_n == '':
            raise AttributeError('Количество не может быть пустым')
        if int(self.top_n) > 100:
            self.top_n = 100
        return int(self.top_n)

    def user_input_value_str(self):
        """
        Отладка ошибок при вводе запроса пользователя
        :return: корректный запрос пользователя, либо вид ошибки
        :rtype: string
        """
        self.search_query = input("Введите поисковый запрос: ")
        if self.search_query == '':
            raise ValueError('Запрос не может быть пустым')
        if self.search_query.isdigit():
            raise TypeError('Запрос не может быть числом')
        else:
            return self.search_query


if __name__ == '__main__':
    r = HHRequestDebug()
    r.user_input_value_str()
