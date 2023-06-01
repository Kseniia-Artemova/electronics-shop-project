from src.item import Item


class MixinLanguage:
    """Класс, реализующий дополнительный функционал хранения и смены раскладки клавиатуры."""

    AVAILABLE_LANGUAGES = ("EN", "RU")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> 'MixinLanguage':
        """Метод меняет язык клавиатуры на один из доступных"""

        language = self.AVAILABLE_LANGUAGES
        self.__language = language[self.__language == language[0]]
        return self


class Keyboard(MixinLanguage, Item):
    """Класс для представления клавиатуры в магазине"""

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
