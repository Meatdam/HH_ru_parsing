from src.user_form import UserForm


class DebugUserJson(UserForm):
    """
       Отладка всех возможных ошибок во время запроса пользователя
    """

    salary_from = None
    user_city = None

    def user_input_int(self):
        """
        Отладка ошибок при вводе запроса по зарплате
        :return: корректный запрос пользователя, либо вид ошибки
        :rtype: integer
        """
        self.salary_from = input("Введите минимальную зарплату: ")
        if self.salary_from.isalpha():
            raise ValueError('Не верно указана зарплата, убедитесь что вы вводите число!')
        if self.salary_from == '':
            self.salary_from = 0
        return int(self.salary_from)

    def user_input_value_str(self):
        """
        Отладка ошибок при вводе запроса города
        :return: корректный запрос пользователя, либо вид ошибки
        :rtype: str
        """
        self.user_city = input("Введите приоритетный город: ").title()
        if self.user_city.isdigit():
            raise ValueError('Город не может быть числом')
        return self.user_city


if __name__ == '__main__':
    r = DebugUserJson()
    print(r.user_input_int())
