from pynput import mouse, keyboard


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

    def move_to_position(self, coordinates: dict):
        position = (coordinates["pos_x"], coordinates["pos_y"])
        self.controller.position = position

    def click(self, click_button, clicks_number):
        self.controller.click(self.button[click_button], clicks_number)


class Keyboard:
    """
    Class for keyboard control
    """
    def __init__(self):
        self.controller = keyboard.Controller()

    def type(self, text: dict):
        self.controller.type(text["typing"])

    def tap_key(self, key: dict):
        # ToDo: think how to define enter key
        key_to_tap = keyboard.Key[key["key"]]
        self.controller.tap(key_to_tap)

