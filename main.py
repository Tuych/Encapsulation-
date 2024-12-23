from uuid import uuid4


class UserData:
    __count = 0

    def __init__(self, firstname, lastname, age):
        self.verify_name(firstname)
        self.verify_name(lastname)
        self.verify_age(age)
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        UserData.__count += 1

    def __str__(self):
        return f"{self.__firstname} {self.__lastname} {self.__age} года"

    @staticmethod
    def verify_name(name):
        if not isinstance(name, str):
            raise TypeError(f"{name} должно быть в формате str.")

    @staticmethod
    def verify_age(age):
        if not isinstance(age, int) or age < 18 or age > 120:
            raise TypeError(f"Возраст должен быть указан в целочисленном формате и в диапазоне 18...120.")

    @property
    def get_count(self):
        return self.__count

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, new_firstname):
        self.verify_name(new_firstname)
        self.__firstname = new_firstname

    @firstname.deleter
    def firstname(self):
        del self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self.verify_name(new_lastname)
        self.__lastname = new_lastname

    @lastname.deleter
    def lastname(self):
        del self.__lastname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.verify_age(new_age)
        self.__age = new_age

    @age.deleter
    def age(self):
        del self.__age


class Automobile:
    __num__auto = 0

    def __init__(self, make, model, color, price, km=0):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Automobile.__num__auto += 1

    @classmethod
    def get_num_auto(cls):
        return cls.__num__auto

    def get_km(self):
        return self.__km

    def add_km(self, value):
        if value > 0:
            self.__km += value
        else:
            print("Пробег не может быть уменьшен")

    def get_id(self):
        return self.__id
