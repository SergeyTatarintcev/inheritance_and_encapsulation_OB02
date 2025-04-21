from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

class MagicWand(Weapon):
    def attack(self):
        return "использует магическую атаку"

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self, monster):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
            monster.take_damage()
        else:
            print(f"{self.name} безоружен!")

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def take_damage(self):
        print(f"{self.name} побежден!")
        self.alive = False

# Шаг 4: Демонстрация боя
def main():
    fighter = Fighter("Боец")
    monster1 = Monster("Монстр 1")
    monster2 = Monster("Монстр 2")
    monster3 = Monster("Монстр 3")

    # Используем меч
    fighter.change_weapon(Sword())
    fighter.attack(monster1)
    print()

    # Используем лук
    fighter.change_weapon(Bow())
    fighter.attack(monster2)
    print()

    # Добавим новый тип оружия: волшебная палочка
    fighter.change_weapon(MagicWand())
    fighter.attack(monster3)

if __name__ == "__main__":
    main()
