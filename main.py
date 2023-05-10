from pynput import keyboard, mouse
from enum import Enum
import json
import time

from accesories import Mouse, Keyboard

mouse_device = Mouse()
keyboard_device = Keyboard()
event_mapper = {
    "move_mouse_to_position": mouse_device.move_to_position,
    "click_mouse": mouse_device.click,
    "type": keyboard_device.type,
    "wait": lambda a, b: time.sleep(b),
    "tap_key": keyboard_device.tap_key
}
