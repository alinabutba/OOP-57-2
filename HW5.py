# Декоратор в Python — это функция, которая изменяет поведение другой функции,
# не меняя её исходный код. Это мощный инструмент для добавления логики к существующим функциям "обёрткой"

# 1. Декоратор uppercase
def uppercase_decorator(func):
    def wrapper(name_wrap):
        res = name_wrap.upper()
        print(res)
    return wrapper

@uppercase_decorator
def print_word(word):
   return print(word)

# print_word("hello")
# print_word("moscow")


# 2. Декоратор require_admin
def require_admin_decorator(func):
    def wrapper(name_wrap):
        if name_wrap == "admin":
            func(name_wrap)
        else:
            print("access denied")
    return wrapper

@require_admin_decorator
def delete_database(name):
    print(f"{name} has deleted the database")

# delete_database("admin")
# delete_database("user1")
