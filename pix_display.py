from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def display_pattern(pattern):
    """
    Display a pattern on the hub using a visual representation.
    
    Args:
        pattern: List of strings where each string represents a row.
                 Use '■' or anything other than space or 0 to turn pixel on,
                 Use '0' or space to turn pixel off.
    
    Example:
        display_pattern([
            "■■■■■",
            "■   ■",
            "■   ■",
            "■   ■",
            "■■■■■"
        ])
    """
    hub.display.off()
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            if char not in ('0', ' '):
                hub.display.pixel(y, x)

def displayNumber(number: int):
    """
    Display a number (0-19) on the hub using a 5x5 pixel pattern.
    Args:
        number: An integer from 0 to 19.
    """
    if number < 0 or number > 19:
        raise ValueError("Number must be between 0 and 19")
    if number == 0:
        display_pattern([
            " ■■■ ",
            " ■ ■ ",
            " ■ ■ ",
            " ■ ■ ",
            " ■■■ "
        ])
    elif number == 1:
        display_pattern([
            "  ■  ",
            " ■■  ",
            "  ■  ",
            "  ■  ",
            " ■■■ "
        ])
    elif number == 2:
        display_pattern([
            " ■■■ ",
            "   ■ ",
            " ■■■ ",
            " ■   ",
            " ■■■ "
        ])
    elif number == 3:
        display_pattern([
            " ■■■ ",
            "   ■ ",
            " ■■■ ",
            "   ■ ",
            " ■■■ "
        ])
    elif number == 4:
        display_pattern([
            " ■ ■ ",
            " ■ ■ ",
            " ■■■ ",
            "   ■ ",
            "   ■ "
        ])
    elif number == 5:
        display_pattern([
            " ■■■ ",
            " ■   ",
            " ■■■ ",
            "   ■ ",
            " ■■■ "
        ])
    elif number == 6:
        display_pattern([
            " ■■■ ",
            " ■   ",
            " ■■■ ",
            " ■ ■ ",
            " ■■■ "
        ])
    elif number == 7:
        display_pattern([
            " ■■■ ",
            "   ■ ",
            "   ■ ",
            "   ■ ",
            "   ■ "
        ])
    elif number == 8:
        display_pattern([
            " ■■■ ",
            " ■ ■ ",
            " ■■■ ",
            " ■ ■ ",
            " ■■■ "
        ])
    elif number == 9:
        display_pattern([
            " ■■■ ",
            " ■ ■ ",
            " ■■■ ",
            "   ■ ",
            " ■■■ "
        ])
    elif number == 10:
        display_pattern([
            "■ ■■■",
            "■ ■ ■",
            "■ ■ ■",
            "■ ■ ■",
            "■ ■■■"
        ])
    elif number == 11:
        display_pattern([
            " ■  ■",
            "■■ ■■",
            " ■  ■",
            " ■  ■",
            " ■  ■"
        ])
    elif number == 12:
        display_pattern([
            "■ ■■■",
            "■   ■",
            "■ ■■■",
            "■ ■  ",
            "■ ■■■"
        ])
    elif number == 13:
        display_pattern([
            "■ ■■■",
            "■   ■",
            "■ ■■■",
            "■   ■",
            "■ ■■■"
        ])
    elif number == 14:
        display_pattern([
            "■ ■ ■",
            "■ ■ ■",
            "■ ■■■",
            "■   ■",
            "■   ■"
        ])
    elif number == 15:
        display_pattern([
            "■ ■■■",
            "■ ■  ",
            "■ ■■■",
            "■   ■",
            "■ ■■■"
        ])
    elif number == 16:
        display_pattern([
            "■ ■■■",
            "■ ■  ",
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■"
        ])
    elif number == 17:
        display_pattern([
            "■ ■■■",
            "■   ■",
            "■   ■",
            "■   ■",
            "■   ■"
        ])
    elif number == 18:
        display_pattern([
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■"
        ])
    elif number == 19:
        display_pattern([
            "■ ■■■",
            "■ ■ ■",
            "■ ■■■",
            "■   ■",
            "■ ■■■"
        ])

# Example usage - displays a smiley face
display_pattern([
    "     ",
    " ■ ■ ",
    "     ",
    "■   ■",
    " ■■■ "
])

selector = 0
hub_done = 0
hub.display.char('?')
while hub_done == 0:
    if Button.RIGHT in hub.buttons.pressed():
        while Button.RIGHT in hub.buttons.pressed():
            wait(0)
        selector = selector + 1
        if selector > 19:
            selector = 0
        displayNumber(selector)
        print(selector)
    elif Button.LEFT in hub.buttons.pressed():
        while Button.LEFT in hub.buttons.pressed():
            wait(0)
        selector = selector - 1
        if selector < 0:
            selector = 19
        displayNumber(selector)
        print(selector)

while True:
    wait(500)