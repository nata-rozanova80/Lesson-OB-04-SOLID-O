from abc import ABC, abstractmethod
import random
class Weapon(ABC):
    @abstractmethod
    def attack(self, health_fighter, health_monstr):

        pass

class Sword(Weapon):
    def attack(self, health_fighter, health_monstr):
        health_fighter += 2
        health_monstr -= 5


class Bow(Weapon):
    def attack(self, health_fighter, health_monstr):
        health_fighter += 1
        health_monstr -= 2



class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Поле для хранения оружия
    health_fighter = 0
    weapon = Weapon()
    def change_weapon(self, weapon_type):
        self.weapon = weapon_type
        print(f"{self.name} сменил оружие на {type(weapon_type).__name__}")
        if weapon_type = 1:
            # Смена оружия и атака
            fighter.change_weapon(sword)
            print(fighter.attack())  # Артур атакует мечом!
        elif weapon_type = 2:
            # Смена оружия и атака
            fighter.change_weapon(bow)
            print(fighter.attack())  # Артур атакует мечом!
    def attack(self):
        if self.weapon is not None:
            return self.weapon.attack()
        else:
            return f"{self.name} не имеет оружия для атаки."

class Monstr():
    health_monstr = 0
    def monster_attack(self):
        hit = 0
        for _in range(iterations):
            hit = random.randint(1, 5) # Случайное значение величины удара монстра
            health_fighter = health_fighter - hit
            health_monstr = health_monstr + 2

# Создаем бойца
fighter = Fighter("Артур")

# Создаем оружие
sword = Sword()
bow = Bow()

# Игра
print("Монстр преградил дорогу бойцу...")
trweapon_type = int(input("Боец выбирает оружие: меч - 1, лук - 2..."))
Fighter.change_weapon()
