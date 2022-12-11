import doctest


class Medicine:
    def __init__(self, dose_in_one_time: (int, float), times_per_day: int):
        """
        Создание и подготовка к работе объекта "Лечение"
        :param dose_in_one_time: доза приема за 1 раз
        :param times_per_day: количество приемов препаратов в день

        Примеры:
        >>> meds = Medicine(1.5, 2)
        """
        if not isinstance(dose_in_one_time, (int, float)):
            raise TypeError("Доза препарата должна быть типа int или float")
        if dose_in_one_time <= 0:
            raise ValueError("Доза препарата должна быть положительным числом")
        self.dose_in_one_time = dose_in_one_time

        if not isinstance(times_per_day, int):
            raise TypeError("Количество приемов препарата в день должно быть типа int")
        if times_per_day < 0:
            raise ValueError("Количество приемов препарата в день должно быть неотрицательным числом")
        self.times_per_day = times_per_day

    def you_r_very_sick(self, dose_up: (int, float)) -> None:
        """
        Человек еще сильнее заболел
        :param dose_up: увеличиваем дозу препаратов
        :return: дозу принимаемых препаратов

        Примеры:
        >>>meds = Medicine(1.5, 2)
        >>>meds.you_r_very_sick(0.5)
        """
        ...

    def you_r_healthy(self) -> bool:
        """
        Функция проверяет, здоров ли человек

        :return: Человек выздоровел

        Примеры:
        >>>meds = Medicine(1.5, 0)
        >>>meds.you_r_healthy()
        """
        ...


class Lessons:
    def __init__(self, lectures: int, practices: int):
        """
        Создание и подготовка к работе объекта "Занятия"
        :param lectures: количество лекций
        :param practices: количество практик

        Примеры:
        >>>course = Lessons(15, 7)
        """
        if not isinstance(lectures, int):
            raise TypeError("Количество лекций должно быть типа int")
        if lectures <= 0:
            raise ValueError("Количество лекций должно быть положительным числом")
        self.lectures = lectures

        if not isinstance(practices, int):
            raise TypeError("Количество практик должно быть типа int")
        if practices < 0:
            raise ValueError("Количество практик должно быть неотрицательным числом")
        self.practices = practices

    def only_lectures(self) -> bool:
        """
        Функция, которая показывает, что занятия состоят только из лекций
        :return: является ли курс только теоретическим

        Примеры:
        >>> course = Lessons(15, 7)
        >>> course.only_lectures()
        """
        ...

    def add_practice(self, more_practice: int) -> None:
        """
        Добавление практик на курсе
        :param more_practice: добавляемое количество занятий на курс

        :raise ValueError: Если количество добавляемых практик больше количества лекций

        Примеры:
        >>>course = Lessons(15, 7)
        >>>course.add_practice(7)
        """
        if not isinstance(more_practice, int):
            raise TypeError("Количество практик должно быть типа int")
        if more_practice < 0:
            raise ValueError("Количество практик должно быть неотрицательным числом")
        ...


class Party:
    def __init__(self, max_people: int, went_people: int):
        """
        Создание и подготовка к работе объекта "Вечеринка"
        :param max_people: максимально возможное количество человек на вечеринке
        :param practices: количество пришедших людей

        Примеры:
        >>>party = Party(100, 50)
        """
        if not isinstance(max_people, int):
            raise TypeError("Максимально возможное количество человек должно быть типа int")
        if max_people <= 0:
            raise ValueError("Максимально возможное количество человек должно быть положительным числом")
        self.max_people = max_people

        if not isinstance(went_people, int):
            raise TypeError("Количество пришедших людей должно быть типа int")
        if went_people < 0:
            raise ValueError("Количество пришедших людей должно быть неотрицательным числом")
        self.went_people = went_people

    def small_place(self, go_away: int) -> None:
        """
        Функция, которая показывает, что пришло очень много людей и надо кого-то выгнать
        :param go_away: количество ушедших людей

        :return: количество ушедших людей
        :raise ValueError: если количество ушедших людей превышает количсетво пришедших людей, то возвращается ошибка.

        Примеры:
        >>> course = Lessons(10, 17)
        >>> course.small_place(7)
        """
        if not isinstance(go_away, int):
            raise TypeError("Количество ушедших людей должно быть типа int")
        if go_away < 0:
            raise ValueError("Количество ушедших людей должно быть неотрицательным числом")
        ...

    def its_boring(self) -> bool:
        """
        Функция, которая показывает, что никто не пришел
        :return: не удалась ли вечеринка
        Примеры:
        >>>party = Party(15, 0)
        >>>party.its_boring()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
