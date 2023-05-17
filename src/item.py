class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = None
        self.name = name

        self.__price = None
        self.price = price

        self.__quantity = None

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Наименование должно быть строкой")
        elif len(name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) not in (int, float):
            raise Exception("Цена должна быть числом")
        else:
            self.__price = float(price)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if type(quantity) is not int:
            raise Exception("Количество должно быть выражено целым числом")
        else:
            self.__quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        if not isinstance(self.pay_rate, float):
            raise ValueError("Размер скидки задан неверно!")
        elif self.pay_rate > 1:
            raise ValueError("Размер скидки задан неверно!")
        else:
            self.price *= self.pay_rate
