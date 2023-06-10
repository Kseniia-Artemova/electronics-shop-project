class InstantiateCSVError(Exception):
    """Класс ошибок, возникающих при работе с CSV"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка."

    def __str__(self):
        return self.message