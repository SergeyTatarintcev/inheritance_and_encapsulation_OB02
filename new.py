import json

# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод должен быть переопределен в подклассе")

    def eat(self):
        print(f"{self.name} ест.")

# 2. Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} говорит: Чирик-чирик!")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} говорит: Ррррр!")

class Reptile(Animal):
    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_sound(self):
        print(f"{self.name} говорит: Шшшшш!")

# 3. Полиморфизм: функция animal_sound
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# 4. Класс Zoo с композицией
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк.")

    def save_to_file(self, filename):
        data = {
            "name": self.name,
            "animals": [
                {"type": type(animal).__name__, "name": animal.name, "age": animal.age}
                for animal in self.animals
            ],
            "staff": [
                {"type": type(staff).__name__, "name": staff.name}
                for staff in self.staff
            ]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Информация о зоопарке сохранена в файл {filename}.")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        self.name = data["name"]
        self.animals = []
        self.staff = []

        for animal_data in data["animals"]:
            if animal_data["type"] == "Bird":
                self.animals.append(Bird(animal_data["name"], animal_data["age"], "unknown"))
            elif animal_data["type"] == "Mammal":
                self.animals.append(Mammal(animal_data["name"], animal_data["age"], "unknown"))
            elif animal_data["type"] == "Reptile":
                self.animals.append(Reptile(animal_data["name"], animal_data["age"], "unknown"))

        for staff_data in data["staff"]:
            if staff_data["type"] == "ZooKeeper":
                self.staff.append(ZooKeeper(staff_data["name"]))
            elif staff_data["type"] == "Veterinarian":
                self.staff.append(Veterinarian(staff_data["name"]))

        print(f"Информация о зоопарке загружена из файла {filename}.")

# 5. Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Пример использования
if __name__ == "__main__":
    # Создание животных
    bird = Bird("Попугай", 5, "50 см")
    mammal = Mammal("Лев", 8, "Золотистый")
    reptile = Reptile("Змея", 3, "Черный")

    # Демонстрация полиморфизма
    animals = [bird, mammal, reptile]

    animal_sound(animals)

    # Создание зоопарка
    zoo = Zoo("Центральный зоопарк")
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Создание сотрудников
    keeper = ZooKeeper("Иван")
    vet = Veterinarian("Мария")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Действия сотрудников
    print("\nДействия сотрудников:")
    keeper.feed_animal(bird)
    vet.heal_animal(mammal)

    # Сохранение и загрузка данных
    zoo.save_to_file("zoo_data.json")
    new_zoo = Zoo("Новый зоопарк")
    new_zoo.load_from_file("zoo_data.json")