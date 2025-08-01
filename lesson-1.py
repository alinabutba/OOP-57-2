# чертеж
class Hero:
    # конструктор класса __init__, self ссылка на объект kirito
    def __init__(self, name, lvl, hp):
        # атрибуты класса
        self.name_1 = name
        self.lvl_1 = lvl
        self.hp_1 = hp

    # метод
    def action(self):
        print(f"{self.name_1} base action")


# объект
kirito = Hero("Kirito", 100, 1000)
kirito.action()

print(kirito.hp_1)