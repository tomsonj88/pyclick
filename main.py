from pynput import keyboard, mouse
from enum import Enum
from dotenv import load_dotenv
import json
import time

from accesories import Mouse, Keyboard


def wait(delay: dict):
    time.sleep(delay["time_to_wait"])


load_dotenv()
mouse_device = Mouse()
keyboard_device = Keyboard()
event_mapper = {
    "move_mouse_to_position": mouse_device.move_to_position,
    "click_mouse": mouse_device.click,
    "type": keyboard_device.type,
    "wait": wait,
    "tap_key": keyboard_device.tap_key,
    "type_from_env_variable": keyboard_device.type_text_from_env_variables
}

with open("config_file.json") as file:
    data = json.load(file)

    for step in data["steps"]:
        event = step["event"]
        print(f"event: {step['event']}")
        print(f"payload: {step['payload']}\n")
        function = event_mapper[event]
        function(step["payload"])
