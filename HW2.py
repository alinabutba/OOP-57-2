# Тема: Наследование и работа с методами

class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return print("pass")

# obj1 = Hero("John", 10, 100)
# print(type(obj1))
# obj1.action()


# Дочерний класс 1
class HeroMage(Hero):

    def __init__(self, name, hp, mp, spell_book, lvl=1):
        super().__init__(name, lvl, hp)
        self.mp = mp
        self.spell_book = spell_book

    def action(self):
        return print("base action")

    def cast_spell(self):
        if self.mp == 0:
            return print("Сорят, маны нет, иди спать")
        else:
            self.mp -= 100
            return print("Огненный шар")

    def rest(self):
        self.mp += 50
        return print("Отдыхаю")

    def show_spells(self):
        return print(*self.spell_book)

# obj2 = HeroMage(lvl=100, mp=1000, name="Ardager", hp=100)


# Дочерний класс 2
class HeroWarrior(Hero):
    def __init__(self, name, lvl, hp, rage=0):
        super().__init__(name, lvl, hp)
        self.rage = rage

    def action(self):
        return print("Герой готов к атаке!")

    def attack(self):
        if self.rage >= 100:
            self.rage = 0
            # герой наносит мощную атаку и rage сбрасывается в 0
            return print(f"rage составляет {self.rage}")
        else:
            self.rage += 25
            # герой наносит обычную атаку и rage увеличивается на 25
            return print(f"rage составляет {self.rage}")

# obj3 = HeroWarrior(name="GGG", lvl=1, hp=10, rage=20)
# obj3.action()
# obj3.attack()

mage = HeroMage(name="Merlin", hp=80, mp=500, lvl=5, spell_book=["Fireball", "Teleport"])
warrior = HeroWarrior(name="Conan", lvl=8, hp=150)

mage.action()       # должно вывести: base action
mage.show_spells()  # должно вывести список заклинаний
warrior.action()    # должно вывести: Герой готов к атаке!
warrior.attack()    # должно прибавить ярость
