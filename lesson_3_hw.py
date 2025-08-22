class UserAccount:
    def __init__(self, username, password):
        self.username = username              # публичное поле
        self._balance = 0                     # защищённое поле
        self.__password = password            # приватное поле
        self.__is_logged_in = False           # внутреннее состояние авторизации

    def login(self, password):
        if password == self.__password:
            self.__is_logged_in = True
            print("Доступ разрешён")
        else:
            print("Доступ запрещён")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Счёт пополнен на {amount}.")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Недостаточно средств.")
        elif amount <= 0:
            print("Сумма должна быть положительной.")
        else:
            self._balance -= amount
            print(f"Снято {amount} со счёта.")

    def get_balance(self):
        if self.__is_logged_in:
            return f'Баланс: {self._balance}'
        else:
            return "Ошибка: пользователь не залогинен."


user = UserAccount("Ivan123", "qwerty123")
user.deposit(1000)
user.withdraw(200)
print(user.get_balance())  # Ошибка
user.login("wrongpass")    # Неверный пароль
user.login("qwerty123")    # Верный пароль
print(user.get_balance())  # Показать баланс



from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Transport):
    def move(self):
        return "Машина едет по дороге"

    def fuel_type(self):
        return "Бензин"


class Bike(Transport):
    def move(self):
        return "Велосипед едет по дороге"

    def fuel_type(self):
        return "Мускульная сила"


class Plane(Transport):
    def move(self):
        return "Самолёт летит в небе"

    def fuel_type(self):
        return "Керосин"


car = Car()
bike = Bike()
plane = Plane()


print(car.move())       # Машина едет по дороге
print(car.fuel_type())  # Бензин

print(bike.move())      # Велосипед едет по дороге
print(bike.fuel_type()) # Мускульная сила

print(plane.move())     # Самолёт летит в небе
print(plane.fuel_type())# Керосин

