"""
Example driver program demonstrating how to use the Menu class.

This shows how to import and use the menu system in your own programs.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
from menu import Menu


def beep_function():
    """Function that makes the hub beep."""
    hub = PrimeHub()
    hub.speaker.beep(440, 200)  # Beep at 440Hz for 200ms


def light_show():
    """Function that creates a light pattern on the hub."""
    hub = PrimeHub()
    # Create a simple light animation
    for i in range(3):
        for color in [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]:
            hub.light.on(color)
            wait(100)
    hub.light.off()


def motor_demo():
    """Function that runs a motor if one is connected to Port A."""
    try:
        motor = Motor(Port.A)
        motor.run_angle(360, 360)  # Run 360 degrees at 360 deg/sec
        motor.stop()
    except:
        # If no motor is connected, just beep instead
        hub = PrimeHub()
        hub.speaker.beep(200, 100)  # Lower pitch beep to indicate no motor


def countdown_demo():
    """Function that shows a countdown on the display."""
    from pix_display import display_number
    hub = PrimeHub()
    
    for i in range(5, 0, -1):
        display_number(hub, i)
        wait(1000)
    
    # Show completion
    hub.display.char('!')
    wait(500)


def main():
    """Main function that sets up and runs the menu."""
    hub = PrimeHub()
    menu = Menu(hub)
    
    # Add menu items with different numbers and functions
    menu.add_item(1, beep_function, "Beep Sound")
    menu.add_item(2, light_show, "Light Show") 
    menu.add_item(3, motor_demo, "Motor Demo")
    menu.add_item(5, countdown_demo, "Countdown")
    
    # Print menu info for debugging (won't show on hub, but useful in IDE)
    print("Menu created with the following items:")
    print(menu)
    print("\nControls:")
    print("- LEFT/RIGHT: Navigate through menu items")
    print("- CENTER: Execute selected function")
    print("- BLUETOOTH: Exit menu")
    print("\nStarting menu...")
    
    # Run the menu system
    menu.run()
    
    print("Menu exited.")


if __name__ == "__main__":
    main()