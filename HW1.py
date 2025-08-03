class Animal:

    def __init__(self, pet, weight, has_passport):
        self.pet = pet
        self.weight = weight
        self.has_passport = has_passport

    """
    Метод can_travel_by_plane проверяет, можно ли перевозить питомца на самолете 
    На самолете можно перевозить только кошек и собак, у которых есть ветеринарный паспорт 
    Если животное 8 кг или меньше, можно перевозить в салоне самолета 
    Если животное больше 8 кг, разрешена перевозка в багажном отсеке
    """
    def can_travel_by_plane(self):
        if self.pet not in ["cat", "dog"]:
            return f"Your {self.pet} cannot be transported"
        
        if not self.has_passport:
            return f"Your {self.pet} cannot be transported without a passport"
        
        if self.weight <= 8:
            return f"Your {self.pet} can be transported in the cabin"
        else:
            return f"Your {self.pet} can be transported in the luggage compartment"


cat = Animal("cat", 3, True)
dog_1 = Animal("dog", 15, True)
dog_2 = Animal("dog", 7, False)
snake = Animal("snake", 1, False)


print(cat.can_travel_by_plane())
# print(dog_1.can_travel_by_plane())
# print(dog_2.can_travel_by_plane())
# print(snake.can_travel_by_plane())