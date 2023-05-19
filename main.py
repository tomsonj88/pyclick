from pynput import keyboard, mouse
from enum import Enum
import json
import time

from accesories import Mouse, Keyboard


def wait(delay:dict):
    time.sleep(delay["time_to_wait"])


mouse_device = Mouse()
keyboard_device = Keyboard()
event_mapper = {
    "move_mouse_to_position": mouse_device.move_to_position,
    "click_mouse": mouse_device.click,
    "type": keyboard_device.type,
    "wait": wait,
    "tap_key": keyboard_device.tap_key
}

with open("config_file.json") as file:
    data = json.load(file)
    print(data)