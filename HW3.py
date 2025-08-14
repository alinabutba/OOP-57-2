# 1. Инкапсуляция
class UserAccount:

    def __init__(self, username, balance, password):
        self.username = username  # публичное поле
        self._balance = balance  # защищённое поле, баланс защищен
        self.__password = password  # приватное поле, пароль совсем скрыт
        self.__is_logged_in = False  # флаг авторизации

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
        else:
            print("Ошибка: Недостаточно средств или неверная сумма")

    def login(self, password):
        if self.__password == password:
            self.__is_logged_in = True
            print("Доступ разрешен")
        else:
            print("Доступ запрещен")

    def get_balance(self):
        if self.__is_logged_in:
            return self._balance
        else:
            print("Ошибка: Требуется авторизация")


user_1 = UserAccount("Adele", 2000, "123")
user_1.login("123")
user_1.deposit(100)
#print(user_1.get_balance())
user_1.withdraw(1100)
#print(user_1.get_balance())
user_1.withdraw(1000000)
print(user_1.get_balance())
