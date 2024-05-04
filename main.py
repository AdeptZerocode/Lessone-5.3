#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о
# животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут
# иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке
#в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle
class Animal():
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def make_sound(self):
         pass
     def eat(self):
         pass

class Bird(Animal):
    def make_sound(self):
        print("чик чирик")

class Mammal(Animal):
    def make_sound(self):
        print("РРрык")

class Reptile(Animal):
    def make_sound(self):
        print("Ттссс")

animals = [Bird("Воробьи", "2"), Mammal("Звери", "10"), Reptile("Змеи", "1")]
for animal in animals:
    animal.make_sound()

class Zoo():
    def __init__(self):
        self.staff = []
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal} добавлено")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} добавлен")

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            print(f"Зоопарк сохранен в файл {filename}")

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
            print(f"Зоопарк загружен из файла {filename}")
            return zoo


class Zookeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник покормил {animal.name}")

class Veterinarian():
    def heal_animal(self, animal):
        print(f"Сотрудник вылечил {animal.name}")

bird1 = Bird("Воробьи", "2")
mammal1 = Mammal("Звери", "10")
reptile1 = Reptile("Змеи", "1")

zoo = Zoo()
keeper = Zookeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

keeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)

zoo.save_zoo('zoo_state.pkl')
new_zoo = Zoo.load_zoo('zoo_state.pkl')




