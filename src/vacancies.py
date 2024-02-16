class Vacancy:
    """
    Форма для класса HeadHunter
    """
    def __init__(self, name, page):
        self.__name = name
        self.__page = page

    @property
    def name(self):
        return self.__name

    @property
    def page(self):
        return self.__page

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.__page})"

    def __str__(self):
        return f"{self.__name}"
