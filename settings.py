import questionary
import game

from interface import Text


def show_settings() -> None:
    """Show the user's current settings, and ask him if he wants to change something."""
    print(f"\n\n{Text.UNDERLINE}Current settings :{Text.END}\n    \U0001F50A Music : {("OFF", "ON")[game.is_music_on]}\n\n")

    answer_setting = questionary.select(
        "What do you want to do ? (it will be save only for this instance)",
        choices=[game.CHANGE_MUSIC_SETTING, game.GO_BACK]
    ).ask()

    if answer_setting == game.CHANGE_MUSIC_SETTING:
        game.is_music_on = not game.is_music_on
        show_settings()
    elif answer_setting == game.GO_BACK:
        game.restart_game()
