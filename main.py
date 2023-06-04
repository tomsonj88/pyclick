"""
PyClick - automated login to VPN
"""

import json
import logging
import time

from dotenv import load_dotenv

from accesories import Mouse, Keyboard

logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    level=logging.INFO
                    )


def wait(delay: float):
    """
    Method used for waiting number of seconds specified in parameters
    """
    time.sleep(delay)


def main():
    """
    Main function
    """
    load_dotenv()
    mouse_device = Mouse()
    keyboard_device = Keyboard()
    event_mapper = {
        "move mouse to position": mouse_device.move_to_position,
        "click mouse": mouse_device.click,
        "type": keyboard_device.type,
        "wait": wait,
        "tap key": keyboard_device.tap_key,
        "type from env variable": keyboard_device.type_text_from_env_variables,
        "paste": keyboard_device.type_paste
    }

    with open("actions.json", encoding="utf8") as file:
        data = json.load(file)["steps"]

    for step in data:
        for key, value in step.items():
            function = event_mapper[key]
            function(**value)
        logging.info(step)


if __name__ == '__main__':
    main()
