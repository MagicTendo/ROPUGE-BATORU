import time
import sys
import pygame
import questionary
import settings
import resource_manager

from interface import Interface
from characters import *

COOLDOWN: int = 0.5
MAX_ROUNDS: int = 50
MAX_CHARACTERS: int = 15
MAX_SCORE_POINTS: int = 500
SCORE_PENALTY: int = 30
MIN_XP: int = 200
MAX_XP: int = 350
LEVEL_FOR_NEW_CHARACTER: int = 5
LEVEL_UP_EXTRA_HEALTH: int = 10
LEVEL_UP_EXTRA_DEFENSE: int = 5
LEVEL_UP_EXTRA_STRENGTH: int = 2

YES: str = "\u2705 Yes"
NO: str = "\u274C No"
SETTINGS: str = "\u2699\uFE0F Settings"
CHANGE_MUSIC_SETTING: str = "\U0001F50A Change music setting"
GO_BACK: str = "\U0001F519️ Go back"
QUIT: str = "\U0001F534 Quit"
MORE_HEALTH: str = f"+ {LEVEL_UP_EXTRA_HEALTH} HP \u2764\uFE0F"
MORE_DEFENSE: str = f"+ {LEVEL_UP_EXTRA_DEFENSE} DEF \U0001F6E1\uFE0F"
MORE_STRENGTH: str = f"+ {LEVEL_UP_EXTRA_STRENGTH} ATK \u2694\uFE0F"

is_music_on: bool = True


class Game:
    def __init__(self):
        self.score: int = 0
        self.round_number: int = 0
        self.wave_number: int = 0
        self.selected_characters: list = []
        self.enemies: list = []

        self.CHARACTERS_CLASSES: dict = {
            Korufuyuki().name: Korufuyuki(),
            Hinosako().name: Hinosako(),
            Kasenzan().name: Kasenzan(),
            Ekazenaya().name: Ekazenaya(),
            Tokinotsuki().name: Tokinotsuki(),
            Myujadena().name: Myujadena(),
            Ketsudan().name: Ketsudan(),
            Koseiden().name: Koseiden(),
            Reishikida().name: Reishikida(),
            Sayetsuri().name: Sayetsuri(),
            Tereya().name: Tereya(),
            Kuraisoki().name: Kuraisoki(),
            BakaTaida().name: BakaTaida(),
            Obusidyawa().name: Obusidyawa(),
            Suyataru().name: Suyataru(),
        }

    def main_screen(self) -> None:
        """Show the main menu composed of the logo and some options."""
        print(Text.SPACE)
        print(Interface.INTERFACE_SEPARATOR)
        print(Interface.LOGO)
        print(Interface.INTERFACE_SEPARATOR)
        print("\n")

        answer_start = questionary.select(
            "Start ?",
            choices=[YES, SETTINGS, QUIT]
        ).ask()

        if answer_start == YES:
            self.start()
        elif answer_start == SETTINGS:
            settings.show_settings()
        elif answer_start == QUIT:
            sys.exit(0)

    def start(self) -> None:
        """Ask the player which character he wants to start with, then launch the music and start the battle."""
        self.select_character()

        if is_music_on:
            pygame.mixer.init()
            pygame.mixer.music.load(resource_manager.get_resource("faitoyo.mp3"))
            pygame.mixer.music.play(-1)

        self.start_fight()

    def select_character(self) -> None:
        """Ask the user which character to add in his team."""
        answer_character = questionary.select(
            "Which character do you want to add in your team ?",
            choices=[
                (f"{Korufuyuki().name}\n    {Korufuyuki().health} HP {Korufuyuki().defense} DEF {Korufuyuki().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Korufuyuki) for x in self.selected_characters)],
                (f"{Hinosako().name}\n    {Hinosako().health} HP {Hinosako().defense} DEF {Hinosako().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Hinosako) for x in self.selected_characters)],
                (f"{Kasenzan().name}\n    {Kasenzan().health} HP {Kasenzan().defense} DEF {Kasenzan().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Kasenzan) for x in self.selected_characters)],
                (f"{Ekazenaya().name}\n    {Ekazenaya().health} HP {Ekazenaya().defense} DEF {Ekazenaya().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Ekazenaya) for x in self.selected_characters)],
                (f"{Tokinotsuki().name}\n    {Tokinotsuki().health} HP {Tokinotsuki().defense} DEF {Tokinotsuki().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Tokinotsuki) for x in self.selected_characters)],
                (f"{Myujadena().name}\n    {Myujadena().health} HP {Myujadena().defense} DEF {Myujadena().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Myujadena) for x in self.selected_characters)],
                (f"{Ketsudan().name}\n    {Ketsudan().health} HP {Ketsudan().defense} DEF {Ketsudan().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Ketsudan) for x in self.selected_characters)],
                (f"{Koseiden().name}\n    {Koseiden().health} HP {Koseiden().defense} DEF {Koseiden().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Koseiden) for x in self.selected_characters)],
                (f"{Reishikida().name}\n    {Reishikida().health} HP {Reishikida().defense} DEF {Reishikida().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Reishikida) for x in self.selected_characters)],
                (f"{Sayetsuri().name}\n    {Sayetsuri().health} HP {Sayetsuri().defense} DEF {Sayetsuri().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Sayetsuri) for x in self.selected_characters)],
                (f"{Tereya().name}\n    {Tereya().health} HP {Tereya().defense} DEF {Tereya().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Tereya) for x in self.selected_characters)],
                (f"{Kuraisoki().name}\n    {Kuraisoki().health} HP {Kuraisoki().defense} DEF {Kuraisoki().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Kuraisoki) for x in self.selected_characters)],
                (f"{BakaTaida().name}\n    {BakaTaida().health} HP {BakaTaida().defense} DEF {BakaTaida().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, BakaTaida) for x in self.selected_characters)],
                (f"{Obusidyawa().name}\n    {Obusidyawa().health} HP {Obusidyawa().defense} DEF {Obusidyawa().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Obusidyawa) for x in self.selected_characters)],
                (f"{Suyataru().name}\n    {Suyataru().health} HP {Suyataru().defense} DEF {Suyataru().strength} ATK",
                    Interface.EMPTY_CHARACTER)[any(isinstance(x, Suyataru) for x in self.selected_characters)],
            ]
        ).ask()

        if answer_character is None or answer_character == Interface.EMPTY_CHARACTER:
            self.select_character()
        else:
            self.selected_characters.append(self.CHARACTERS_CLASSES[str(answer_character).partition("\n")[0]])

    def win(self) -> None:
        """Update the score and give XP to each character in the user's team."""
        self.score += max(0, MAX_SCORE_POINTS - ((self.round_number - 1) * SCORE_PENALTY))

        print(f"\n{Text.BOLD}{Text.BLINK}{Text.YELLOW} >>  \U0001F4E3 You won ! Score : {self.score}{Text.END}\n\n\n\n")

        i = 0
        characters_number = len(self.selected_characters)

        for character in self.selected_characters:
            i += 1

            if i <= characters_number and character.is_alive():
                gained_xp = random.randint(MIN_XP, MAX_XP)
                real_level = math.floor((character.xp + gained_xp) / character.next_level) + 1
                real_current_xp = (character.xp + gained_xp - (character.next_level * character.level) + character.next_level) % character.next_level

                print(f"{character.name} is level {Text.GREEN}{real_level}{Text.END} ({real_current_xp} / {character.next_level}) and has earned {Text.GREEN}{gained_xp}{Text.END} XP !")

                character.give_xp(gained_xp)

        for character in self.selected_characters:
            if character.xp - (character.level * character.next_level) >= 0 and character.is_alive():
                self.level_up(character)

        self.start_fight()

    def level_up(self, character) -> None:
        """
        When a character levels up, either ask what to upgrade, or ask which character to add in the team if the
        character's level is a multiple of the value of [LEVEL_FOR_NEW_CHARACTER].
        :param character: The character class that has leveled up.
        """
        character.level += 1

        if character.xp > 0:
            if character.level % LEVEL_FOR_NEW_CHARACTER == 0 and len(self.selected_characters) < MAX_CHARACTERS:
                print("\n\n")

                self.select_character()
            else:
                print(f"\n\n{Text.ITALIC}{Text.LIGHT_WHITE}{character.name} has {character.health} HP ❤️, {character.defense} DEF 🛡️ and {character.strength} ATK ⚔️{Text.END}\n")

                answer_upgrade = questionary.select(
                    f"{character.name}  What do you want to upgrade ?",
                    choices=[MORE_HEALTH, MORE_DEFENSE, MORE_STRENGTH]
                ).ask()

                if answer_upgrade == MORE_HEALTH or answer_upgrade is None:
                    character.health += LEVEL_UP_EXTRA_HEALTH
                elif answer_upgrade == MORE_DEFENSE:
                    character.defense += LEVEL_UP_EXTRA_DEFENSE
                elif answer_upgrade == MORE_STRENGTH:
                    character.strength += LEVEL_UP_EXTRA_STRENGTH

    def start_fight(self) -> None:
        """
        Prepare the fight by setting the variable to their default values, incrementing the wave number, creating
        enemies depending on the wave number and then by sending the messages about the wave.
        """
        self.round_number = 0
        self.wave_number += 1
        self.enemies = []

        if self.wave_number == 100:
            self.enemies.append(Neramawa(self.wave_number))
            slf.enemies.append(Neruyano(self.wave_number))
            self.enemies.append(Nerunamen(self.wave_number))
        elif self.wave_number % 50 == 0:
            self.enemies.append(Neruyano(self.wave_number))
            self.enemies.append(Tamadama(self.wave_number))
            self.enemies.append(BuruCube(self.wave_number))
        elif self.wave_number % 30 == 0:
            self.enemies.append(Nerunamen(self.wave_number))
            self.enemies.append(Nerunamen(self.wave_number))
        elif self.wave_number % 20 == 0:
            self.enemies.append(Tamadama(self.wave_number))
            self.enemies.append(Tamadama(self.wave_number))
            self.enemies.append(BuruCube(self.wave_number))
            self.enemies.append(BuruCube(self.wave_number))
        elif self.wave_number % 10 == 0:
            self.enemies.append(Tamadama(self.wave_number))
            self.enemies.append(Tamadama(self.wave_number))
            self.enemies.append(BuruCube(self.wave_number))
        elif self.wave_number % 5 == 0:
            self.enemies.append(Tamadama(self.wave_number))
            self.enemies.append(BuruCube(self.wave_number))
        elif self.wave_number % 2 == 0:
            self.enemies.append(BuruCube(self.wave_number))
        else:
            self.enemies.append(Tamadama(self.wave_number))

        if self.wave_number != 1:
            time.sleep(COOLDOWN * 3)

        print(f"\n\n\n{Text.BOLD}{Text.CYAN}Wave {self.wave_number}\n")

        for character in self.selected_characters:
            is_dead = character.health <= 0

            print(f"{("", f"💀 {Text.CROSSED}{Text.ITALIC}")[is_dead]}{character.name} ({character.health} ❤️ | {character.defense} 🛡️ | {character.strength} ⚔️){("", f"{Text.END}{Text.BOLD}{Text.CYAN}")[is_dead]}")

        print(f"\n🆚\n")

        for enemy in self.enemies:
            print(f"{enemy.name} ({enemy.health} ❤️ | {enemy.defense} 🛡️ | {enemy.strength} ⚔️)")

        print(f"{Text.END}\n\n")

        time.sleep(COOLDOWN * 4)

        print(Interface.DIALOG_SEPARATOR)

        self.fight_loop()

    def fight_loop(self) -> None:
        """
        Start a loop that will either end if there have been 50 or more rounds, if all the character in the user's
        team are dead, or if all the enemies are dead. In each occurrence, each character will attack each enemy once,
        and then each enemy will attack each character once. If every enemy are dead, trigger the win method, if every
        character in the user's team are dead or if it's been 50 or more rounds, trigger the game_over function.
        """
        while not all(not instance.is_alive() for instance in self.enemies) and any(instance.is_alive() for instance in self.selected_characters):
            if self.round_number >= MAX_ROUNDS:
                print(f"\n\n{Text.BOLD}{Text.BLUE}It's been {MAX_ROUNDS} rounds... {Text.END}\n")
                game_over()

            self.round_number += 1

            for character in self.selected_characters:
                for enemy in self.enemies:
                    if enemy.is_alive() and character.is_alive():
                        character.attack(enemy)
                        enemy.show_health()

            time.sleep(COOLDOWN)
            print(Interface.DIALOG_SEPARATOR)

            for enemy in self.enemies:
                if enemy.is_alive():
                    for character in self.selected_characters:
                        if character.is_alive():
                            enemy.attack(character)
                            character.show_health()

            time.sleep(COOLDOWN)

            if any(not instance.is_alive() for instance in self.enemies) and not all(not instance.is_alive() for instance in self.enemies) and len(self.enemies) > 1:
                print(Interface.DIALOG_SEPARATOR)

            if all(instance.is_alive() for instance in self.enemies):
                print(Interface.DIALOG_SEPARATOR)

        if all(not instance.is_alive() for instance in self.enemies) and any(instance.is_alive() for instance in self.selected_characters):
            self.win()
        elif all(not instance.is_alive() for instance in self.selected_characters):
            game_over()

        self.fight_loop()


def game_over() -> None:
    """Stops the music, print the game over message, and ask the user if he wants to stop playing."""
    if is_music_on:
        pygame.mixer.music.stop()
        pygame.mixer.stop()

    print(f"\n\n{Text.BOLD}{Text.BLUE} >>  \u2620\uFE0F Game over...{Text.END}\n\n\n")

    answer_retry = questionary.select(
        "Do you want to retry ?",
        choices=[YES, NO]
    ).ask()

    print("\n")

    if answer_retry == NO:
        sys.exit(0)
    else:
        restart_game()


def restart_game() -> None:
    """Restart the game be creating a brand-new instance."""
    new_game = Game()
    new_game.main_screen()
