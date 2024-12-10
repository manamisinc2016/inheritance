class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False



class Mammal(Animal):
    def eat(self, food):
        """Метод для поедания пищи"""
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        """Метод для поедания пищи"""
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False



class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True





a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик


print(a1.alive)  # True (изначально все животные живы)
print(a2.fed)    # False (изначально все животные голодны)


a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин


print(a1.alive)  # False (волк умер, так как съел несъедобное растение)
print(a2.fed)    # True (Хатико насытился, так как съел съедобный фрукт)
