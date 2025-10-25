from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait


def display_pattern(hub, pattern):
    """
    Display a pattern on the hub using a visual representation.
    
    Args:
        hub: PrimeHub instance to display on.
        pattern: List of strings where each string represents a row.
                 Use '■' or anything other than space or 0 to turn pixel on,
                 Use '0' or space to turn pixel off.
    
    Example:
        display_pattern(hub, [
            "     ",
            " ■ ■ ",
            "     ",
            "■   ■",
            " ■■■ "
        ])
    """
    hub.display.off()
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            if char not in ('0', ' '):
                hub.display.pixel(y, x)

def display_number(hub, number: int):
    """
    Display a number (0-99) on the hub using a 5x5 pixel pattern.
    
    Args:
        hub: PrimeHub instance to display on.
        number: An integer from 0 to 99.
    """
    if number < 0 or number > 99:
        raise ValueError("Number must be between 0 and 99")
    
    if number == 0:
        display_pattern(hub, [
            " ■■■ ",
            " ■ ■ ",
            " ■ ■ ",
            " ■ ■ ",
            " ■■■ "
        ])
    elif number == 1:
        display_pattern(hub, [
            "  ■  ",
            " ■■  ",
            "  ■  ",
            "  ■  ",
            " ■■■ "
        ])
    elif number == 2:
        display_pattern(hub, [
            " ■■■ ",
            "   ■ ",
            " ■■■ ",
            " ■   ",
            " ■■■ "
        ])
    elif number == 3:
        display_pattern(hub, [
            " ■■■ ",
            "   ■ ",
            " ■■■ ",
            "   ■ ",
            " ■■■ "
        ])
    elif number == 4:
        display_pattern(hub, [
            " ■ ■ ",
            " ■ ■ ",
            " ■■■ ",
            "   ■ ",
            "   ■ "
        ])
    elif number == 5:
        display_pattern(hub, [
            " ■■■ ",
            " ■   ",
            " ■■■ ",
            "   ■ ",
            " ■■■ "
        ])
    elif number == 6:
        display_pattern(hub, [
            " ■■■ ",
            " ■   ",
            " ■■■ ",
            " ■ ■ ",
            " ■■■ "
        ])
    elif number == 7:
        display_pattern(hub, [
            " ■■■ ",
            "   ■ ",
            "   ■ ",
            "   ■ ",
            "   ■ "
        ])
    elif number == 8:
        display_pattern(hub, [
            " ■■■ ",
            " ■ ■ ",
            " ■■■ ",
            " ■ ■ ",
            " ■■■ "
        ])
    elif number == 9:
        display_pattern(hub, [
            " ■■■ ",
            " ■ ■ ",
            " ■■■ ",
            "   ■ ",
            " ■■■ "
        ])
    elif number == 10:
        display_pattern(hub, [
            "■ ■■■",
            "■ ■ ■",
            "■ ■ ■",
            "■ ■ ■",
            "■ ■■■"
        ])
    elif number == 11:
        display_pattern(hub, [
            " ■  ■",
            "■■ ■■",
            " ■  ■",
            " ■  ■",
            " ■  ■"
        ])
    elif number == 12:
        display_pattern(hub, [
            "■ ■■■",
            "■   ■",
            "■ ■■■",
            "■ ■  ",
            "■ ■■■"
        ])
    elif number == 13:
        display_pattern(hub, [
            "■ ■■■",
            "■   ■",
            "■ ■■■",
            "■   ■",
            "■ ■■■"
        ])
    elif number == 14:
        display_pattern(hub, [
            "■ ■ ■",
            "■ ■ ■",
            "■ ■■■",
            "■   ■",
            "■   ■"
        ])
    elif number == 15:
        display_pattern(hub, [
            "■ ■■■",
            "■ ■  ",
            "■ ■■■",
            "■   ■",
            "■ ■■■"
        ])
    elif number == 16:
        display_pattern(hub, [
            "■ ■■■",
            "■ ■  ",
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■"
        ])
    elif number == 17:
        display_pattern(hub, [
            "■ ■■■",
            "■   ■",
            "■   ■",
            "■   ■",
            "■   ■"
        ])
    elif number == 18:
        display_pattern(hub, [
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■"
        ])
    elif number == 19:
        display_pattern(hub, [
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■",
            "■   ■",
            "■ ■■■"
        ])
    else:
        hub.display.number(number)


def run_number_selector():
    """
    Run an interactive number selector on the hub.
    Use LEFT/RIGHT buttons to cycle through numbers 0-25.
    Press CENTER button to exit.
    """
    hub = PrimeHub()
    selector = 0
    hub.display.char('?')
    selector_increment = 0
    
    while True:
        if hub.buttons.pressed() & {Button.RIGHT, Button.LEFT}:
            if Button.RIGHT in hub.buttons.pressed():
                selector_increment = 1
            elif Button.LEFT in hub.buttons.pressed():
                selector_increment = -1
            while any(hub.buttons.pressed()):
                wait(10)
            selector = (selector + selector_increment) % 26
            display_number(hub, selector)
        wait(10)


if __name__ == "__main__":
    # Run the interactive number selector when this file is executed directly
    run_number_selector()