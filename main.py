import random
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        damage = random.randint(5, 15)  # Урон от меча
        print(f"Воин атакует мечом и наносит {damage} урона.")
        return damage

class Bow(Weapon):
    def attack(self):
        damage = random.randint(2, 10)  # Урон от лука
        print(f"Воин стреляет из лука и наносит {damage} урона.")
        return damage

class Fighter:
    def __init__(self, health):
        self.health = health
        self.weapon = Sword()  # По умолчанию у бойца меч

    def change_weapon(self, weapon_type):
        if weapon_type == 1:
            self.weapon = Sword()
            print("Воин выбрал меч.")
        elif weapon_type == 2:
            self.weapon = Bow()
            print("Воин выбрал лук.")
        else:
            print("Неверный тип оружия. Операция отменена.")

    def attack(self):
        return self.weapon.attack()

class Monster:
    def __init__(self, health):
        self.health = health

    def attack(self):
        damage = random.randint(1, 10)
        print(f"Монстр атакует и наносит {damage} урона.")
        return damage

def fight():
    iterations = random.randint(5, 15)  # Случайное число итераций
    fighter = Fighter(health=50)
    monster = Monster(health=50)

    print(f"Бой начинается! Всего ходов: {iterations}")

    for _ in range(iterations):
        # Смена оружия (просто для примера, это может быть вызвано по желанию пользователя)
        if random.choice([True, False]):
            weapon_choice = random.choice([1, 2])
            fighter.change_weapon(weapon_choice)

        first_attacker = random.choice(['fighter', 'monster'])

        if first_attacker == 'fighter':
            damage = fighter.attack()
            monster.health -= damage
        else:
            damage = monster.attack()
            fighter.health -= damage

        print(f"Здоровье воина: {fighter.health}, Здоровье Монстра: {monster.health}")

        # Проверка на смерть
        if fighter.health <= 0 or monster.health <= 0:
            break

    if fighter.health <= 0:
        print("Воин погиб! Монстр победил!!")
    elif monster.health <= 0:
        print("Монстр погиб! Воин победил!")
    else:
        if fighter.health > monster.health:
            print("Воин победил (по здоровью)!")
        elif monster.health > fighter.health:
            print("Монстр победил (по здоровью)!")
        else:
            print("Ничья!")

# Запуск процедуры боя
fight()
