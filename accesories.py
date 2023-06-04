"""
Module contains procedures to control accesories: mouse and keyboard
"""
from os import getenv

from pynput import mouse, keyboard
from pyperclip import paste


class Mouse:
    """
    Class for mouse control
    """

    def __init__(self):
        self.controller = mouse.Controller()
        self.button = {
            "left": mouse.Button.left,
            "right": mouse.Button.right,
            "middle": mouse.Button.middle
        }

    def move_to_position(self, pos_x: int, pos_y: int):
        """
        Method moves cursor to position specified by coordinates
        x and y.
        """
        position = (pos_x, pos_y)
        self.controller.position = position

    def click(self, button: str, number_of_clicks: int):
        """
        Method is used for click mouse button. Button and number of
        clicks is specified in parameters
        """
        self.controller.click(mouse.Button[button], number_of_clicks)


class Keyboard:
    """
    Class for keyboard control
    """
    def __init__(self):
        self.controller = keyboard.Controller()

    def type(self, text: str):
        """
        Method is used for text typing. Text is specified in parameter.
        """
        self.controller.type(text)

    def tap_key(self, key: str):
        """
        Method is used for type key (press and release) specified in
        parameter.
        """
        key_to_tap = keyboard.Key[key]
        self.controller.tap(key_to_tap)

    def type_text_from_env_variables(self, take_from_env_var: str):
        """
        Method is used for type text placed in environment variables. Especially
        sensitive data are stored in environment variables.
        """
        env_variable = getenv(take_from_env_var)
        self.controller.type(env_variable)

    def type_paste(self):
        """
        Method used for paste text from clipboard.
        """
        self.controller.type(paste())
