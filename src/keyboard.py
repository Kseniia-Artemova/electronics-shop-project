from src.item import Item


class Keyboard(Item):
    """Класс для представления клавиатуры в магазине"""

    AVAILABLE_LANGUAGES = ("EN", "RU")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название клавиатуры
        :param price: Цена за единицу
        :param quantity: Количество единиц товара в магазине
        :param language: Язык раскладки (по умолчанию EN), доступные варианты: RU, EN
        """
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает наименование товара.

        Проверки:

        наименование должно быть строкой
        """

        if not isinstance(name, str):
            raise ValueError("Наименование должно быть строкой")
        else:
            self.__name = name

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        """Метод меняет язык клавиатуры на один из доступных"""

        language = self.AVAILABLE_LANGUAGES
        self.__language = language[self.__language == language[0]]



