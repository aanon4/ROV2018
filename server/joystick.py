from typing import List, Tuple

import pygame


class JoystickData:
    """Container for data read from the joystick"""

    def __init__(self, axes: List[float], buttons: List[bool], hat: Tuple[int, int]) -> None:
        self.axes = axes
        self.buttons = buttons
        self.hat = hat


class Joystick:
    """Wrapper for a Pygame joystick connection"""

    def __init__(self) -> None:
        self.joystick = None

    def is_connected(self) -> bool:
        """Return whether the joystick is connected"""
        return self.joystick is not None

    def connect(self) -> bool:
        """Attempt to connect to the joystick"""
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.read_values()
            return True
        return False

    def disconnect(self) -> None:
        """Close the connection to the joystick"""
        self.joystick.quit()
        self.joystick = None

    def read_values(self) -> JoystickData:
        """Read the values of the joystick's axes, buttons, and hat, and return a JoystickData"""
        axes = [self.joystick.get_axis(i) for i in range(self.joystick.get_numaxes())]
        buttons = [self.joystick.get_button(i) for i in range(self.joystick.get_numbuttons())]
        hat = self.joystick.get_hat(0)
        return JoystickData(axes, buttons, hat)
