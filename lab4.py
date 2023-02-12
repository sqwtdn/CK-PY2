if __name__ == "__main__":
    class Store:
        """ Базовый класс магазин. """

        def __init__(self, name: str, type_of_store: str):
            self.name = name
            self.type_of_store = type_of_store

        def __str__(self):
            return f"Магазин {self.name}. Это {self.type_of_store} магазин."

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, type_of_store={self.type_of_store!r})"

        @property
        def name(self) -> str:
            return self._name

        @property
        def type_of_store(self) -> str:
            return self._type_of_store


    class Electronics(Store):
        """ Дочерний класс DNS."""
        def __init__(self, name: str, type_of_store: str, rating: int):
            super().__init__(name, type_of_store)
            self._rating = None
            self._rating = rating

        @property
        def rating(self) -> float:
            return self._rating

        @rating.setter
        def rating(self, rating: int) -> None:
            if not isinstance(rating, float):
                raise TypeError
            if not rating == -1 and rating == 1:
                raise ValueError
            self._rating = rating

        def __str__(self):
            return f"Магазин {self.name}. Это {self.type_of_store} магазин."

        def add_stars(self):
            """
            Метод, позволяющий добавить Ваш рейтинг магазину
            Пример:
            >>>test_store = Electronics("DNS", "offline", 100)
            >>>test_store.add_stars(1)
            """
            self._rating += self

        def show_rating(self):
            """
            Метод, позволяющий показать рейтинг магазина
            :return: показывает рейтинг магазина
            Пример:
            >>>test_store = Electronics("DNS", "offline", 100)
            >>>test_store.add_stars(1)
            >>>test_store.show_rating()
            '101'
            """
            return self._rating
    pass
