import keyboard
import time
from app.utils.config_manager import load_config
from app.utils.api_interaction import handle_api_response
from app.utils.logging_manager import custom_print
from app.constants import LOADING_ICON_PATH, NORMAL_ICON_PATH, ERROR_ICON_PATH
from config.constants import SHORTCUT_DELAY, SHORTCUT_KEYS
from PyQt6.QtGui import QIcon
import pyperclip

print = custom_print


def get_clipboard_content():
    return pyperclip.paste()


def handle_shortcut(tray_icon, config):
    try:
        config = load_config()
        gpt_api_key = config.get("gpt_api_key")
        mistral_api_key = config.get("mistral_api_key")
        model_name = config.get("model_name")
        clipboard_content = get_clipboard_content()
        if clipboard_content:
            print("Question from clipboard:", clipboard_content, color="blue")
            tray_icon.setIcon(QIcon(LOADING_ICON_PATH))

            answer = handle_api_response(
                model_name,
                mistral_api_key if "mistral" in model_name else gpt_api_key,
                clipboard_content,
                config,
            )

            print("Response:", answer, color="green")
            pyperclip.copy(answer)
            tray_icon.setIcon(QIcon(NORMAL_ICON_PATH))
        else:
            print("Clipboard is empty!")
    except Exception as e:
        print(f"Error: {e}", color="red")
        tray_icon.setIcon(QIcon(ERROR_ICON_PATH))


def listen_for_shortcut(tray_icon, config, STOP_EVENT):
    while not STOP_EVENT.is_set():
        if keyboard.is_pressed(SHORTCUT_KEYS[0]):
            if keyboard.read_event().name == SHORTCUT_KEYS[1]:
                while keyboard.is_pressed(SHORTCUT_KEYS[1]):
                    time.sleep(0.01)
                start_time = time.time()
                while time.time() - start_time < SHORTCUT_DELAY:
                    if keyboard.read_event().name == SHORTCUT_KEYS[
                        2
                    ] and keyboard.is_pressed(SHORTCUT_KEYS[0]):
                        handle_shortcut(tray_icon, config)
                        break
        time.sleep(0.1)
