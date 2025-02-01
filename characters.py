import random
import math

from interface import Text

ENEMY_MAX_HEALTH = 1500
ENEMY_MAX_DEFENSE = 750
ENEMY_MAX_STRENGTH = 500

ENEMY_HEALTH_MULTIPLIER = 1.025
ENEMY_DEFENSE_MULTIPLIER = 1.0425
ENEMY_STRENGTH_MULTIPLIER = 1.0225

TAMADAMA_DEFAULT_HEALTH = 30
TAMADAMA_DEFAULT_DEFENSE = 1
TAMADAMA_DEFAULT_STRENGTH = 5

BURU_CUBE_DEFAULT_HEALTH = 50
BURU_CUBE_DEFAULT_DEFENSE = 5
BURU_CUBE_DEFAULT_STRENGTH = 5

NERUNAMEN_DEFAULT_HEALTH = 70
NERUNAMEN_DEFAULT_DEFENSE = 20
NERUNAMEN_DEFAULT_STRENGTH = 10

NERUNAYO_DEFAULT_HEALTH = 100
NERUNAYO_DEFAULT_DEFENSE = 30
NERUNAYO_DEFAULT_STRENGTH = 15

NERAMAWA_DEFAULT_HEALTH = 500
NERAMAWA_DEFAULT_DEFENSE = 50
NERAMAWA_DEFAULT_STRENGTH = 50


class Character:
    def __init__(self):
        self.name: str = ""
        self.health: int = 0
        self.defense: int = 0
        self.strength: int = 0
        self.xp: int = 0
        self.level: int = 1
        self.next_level: int = 1000

    def attack(self, enemy) -> None:
        """
        Lower the HP of the enemy depending on the opponent strength.
        :param enemy: Instance of a child of the Character class.
        """
        damage_amount: int = 0

        if self.strength != 0:
            damage_amount = max(0, round((self.strength / 1.5)) + round((self.strength * random.uniform(0.1, 1.05))) - enemy.defense)

        enemy.health -= damage_amount
        print(f"{self.name} attacks {enemy.name} and deals {Text.DARK_YELLOW}{damage_amount}{Text.END} damage(s) !")

    def is_alive(self) -> bool:
        """Verify if the character is alive, if it has more than 0 HP."""
        return self.health > 0

    def show_health(self) -> None:
        """Show the current statistics of the character (either his HP or a death message)."""
        if self.is_alive():
            print(f"{self.name} has now {Text.RED}{self.health}{Text.END} HP.")
        else:
            self.health = 0

            print(f"{self.name} is dead.")

    def give_xp(self, gained_xp: int) -> None:
        """
        Simply give XP.
        :param gained_xp: The amount of XP to give.
        """
        self.xp += gained_xp


class Korufuyuki(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F367 Kōrufuyuki"
        self.health: int = 75
        self.defense: int = 5
        self.strength: int = 10
        self.xp: int = 0
        self.level: int = 1


class Hinosako(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F525 Hinosako"
        self.health: int = 80
        self.defense: int = 15
        self.strength: int = 15
        self.xp: int = 0
        self.level: int = 1


class Kasenzan(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F333 Kasenzan"
        self.health: int = 50
        self.defense: int = 5
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Ekazenaya(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F390 Ekazenaya"
        self.health: int = 60
        self.defense: int = 15
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Tokinotsuki(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\u231A Tokinotsuki"
        self.health: int = 65
        self.defense: int = 5
        self.strength: int = 10
        self.xp: int = 0
        self.level: int = 1


class Myujadena(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F3B6 Myūjadena"
        self.health: int = 65
        self.defense: int = 10
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Ketsudan(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F50E Ketsudan"
        self.health: int = 50
        self.defense: int = 10
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Koseiden(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F30C Kōseiden"
        self.health: int = 100
        self.defense: int = 15
        self.strength: int = 10
        self.xp: int = 0
        self.level: int = 1


class Reishikida(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F56F\uFE0F Reishikida"
        self.health: int = 100
        self.defense: int = 30
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Sayetsuri(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F9EA Sayetsuri"
        self.health: int = 75
        self.defense: int = 20
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Tereya(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F90D Tereya"
        self.health: int = 100
        self.defense: int = 0
        self.strength: int = 25
        self.xp: int = 0
        self.level: int = 1


class Kuraisoki(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F5A4 Kuraisoki"
        self.health: int = 75
        self.defense: int = 40
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class BakaTaida(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\u2728 BakaTaida"
        self.health: int = 70
        self.defense: int = 10
        self.strength: int = 5
        self.xp: int = 0
        self.level: int = 1


class Obusidyawa(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\u26CF\uFE0F Obusidyawa"
        self.health: int = 50
        self.defense: int = 5
        self.strength: int = 30
        self.xp: int = 0
        self.level: int = 1


class Suyataru(Character):
    def __init__(self):
        super().__init__()
        self.name: str = "\U0001F4AB Suyataru"
        self.health: int = 75
        self.defense: int = 10
        self.strength: int = 10
        self.xp: int = 0
        self.level: int = 1


class Tamadama(Character):
    def __init__(self, wave_number):
        super().__init__()
        self.name: str = "\U0001F9CA Tamadama"
        self.health: int = calculate_stats(ENEMY_MAX_HEALTH, TAMADAMA_DEFAULT_HEALTH, ENEMY_HEALTH_MULTIPLIER, wave_number)
        self.defense: int = calculate_stats(ENEMY_MAX_DEFENSE, TAMADAMA_DEFAULT_DEFENSE, ENEMY_DEFENSE_MULTIPLIER, wave_number)
        self.strength: int = calculate_stats(ENEMY_MAX_STRENGTH, TAMADAMA_DEFAULT_STRENGTH, ENEMY_STRENGTH_MULTIPLIER, wave_number)


class BuruCube(Character):
    def __init__(self, wave_number):
        super().__init__()
        self.name: str = "\U0001F7E6 Buru Cube"
        self.health: int = calculate_stats(ENEMY_MAX_HEALTH, BURU_CUBE_DEFAULT_HEALTH, ENEMY_HEALTH_MULTIPLIER, wave_number)
        self.defense: int = calculate_stats(ENEMY_MAX_DEFENSE, BURU_CUBE_DEFAULT_DEFENSE, ENEMY_DEFENSE_MULTIPLIER, wave_number)
        self.strength: int = calculate_stats(ENEMY_MAX_STRENGTH, BURU_CUBE_DEFAULT_STRENGTH, ENEMY_STRENGTH_MULTIPLIER, wave_number)


class Nerunamen(Character):
    def __init__(self, wave_number):
        super().__init__()
        self.name: str = "\U0001F5E1\uFE0F Nerunamen"
        self.health: int = calculate_stats(ENEMY_MAX_HEALTH, NERUNAMEN_DEFAULT_HEALTH, ENEMY_HEALTH_MULTIPLIER, wave_number)
        self.defense: int = calculate_stats(ENEMY_MAX_DEFENSE, NERUNAMEN_DEFAULT_DEFENSE, ENEMY_DEFENSE_MULTIPLIER, wave_number)
        self.strength: int = calculate_stats(ENEMY_MAX_STRENGTH, NERUNAMEN_DEFAULT_STRENGTH, ENEMY_STRENGTH_MULTIPLIER, wave_number)


class Neruyano(Character):
    def __init__(self, wave_number):
        super().__init__()
        self.name: str = "\U0001F9E8 Neruyano"
        self.health: int = calculate_stats(ENEMY_MAX_HEALTH, NERUNAYO_DEFAULT_HEALTH, ENEMY_HEALTH_MULTIPLIER, wave_number)
        self.defense: int = calculate_stats(ENEMY_MAX_DEFENSE, NERUNAYO_DEFAULT_DEFENSE, ENEMY_DEFENSE_MULTIPLIER, wave_number)
        self.strength: int = calculate_stats(ENEMY_MAX_STRENGTH, NERUNAYO_DEFAULT_STRENGTH, ENEMY_STRENGTH_MULTIPLIER, wave_number)


class Neramawa(Character):
    def __init__(self, wave_number):
        super().__init__()
        self.name: str = "\U0001F9B4 Neramawa"
        self.health: int = NERAMAWA_DEFAULT_HEALTH
        self.defense: int = NERAMAWA_DEFAULT_DEFENSE
        self.strength: int = NERAMAWA_DEFAULT_STRENGTH


def calculate_stats(max_stat_value: int, default_stat: int, multiplier: int, current_wave: int) -> int:
    """
    Only useful for enemy classes, calculate the health, the defense or the strength value based of the current wave.
    :param max_stat_value: If the calculated stat is over that value, the final result will be this.
    :param default_stat: The default value that will be set in the first wave.
    :param multiplier: Decide of how much to increase for each wave.
    :param current_wave: The number of the wave.
    :return: An integer that's a multiple of 5 and based of the number of the wave.
    """
    return min(max_stat_value, round(5 * round(default_stat * (multiplier ** current_wave) / 5)))
