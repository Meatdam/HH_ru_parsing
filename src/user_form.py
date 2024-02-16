from abc import ABC, abstractmethod


class UserForm(ABC):
    """
    Форма пользователя
    """
    @abstractmethod
    def user_input_int(self):
        pass

    @abstractmethod
    def user_input_value_str(self):
        pass
