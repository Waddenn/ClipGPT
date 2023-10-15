from PyQt6.QtWidgets import (
    QSystemTrayIcon,
    QMenu,
)
from PyQt6.QtGui import QIcon

from app.utils.config_manager import load_config, save_config, ConfigDialog
from app.utils.logging_manager import LogDialog
from app.constants import NORMAL_ICON_PATH

prompts_submenu = None


def setup_tray_icon(clean_exit_callback):
    global prompts_submenu

    tray_icon = QSystemTrayIcon(QIcon(NORMAL_ICON_PATH))
    menu = QMenu()

    logs_action = menu.addAction("Logs")
    logs_action.triggered.connect(lambda: LogDialog().exec())

    settings_action = menu.addAction("Settings")
    settings_action.triggered.connect(lambda: ConfigDialog().exec())

    prompts_submenu = QMenu("Select Prompt", menu)
    populate_prompts_submenu(prompts_submenu)
    menu.addMenu(prompts_submenu)

    quit_action = menu.addAction("Quit")
    quit_action.triggered.connect(clean_exit_callback)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    return tray_icon


def populate_prompts_submenu(submenu):
    submenu.clear()
    for prompt_name in load_config()["prompts"].keys():
        action = submenu.addAction(prompt_name)
        action.triggered.connect(
            lambda checked, name=prompt_name: set_active_prompt(name)
        )


def refresh_prompts_submenu():
    global prompts_submenu
    if prompts_submenu:
        populate_prompts_submenu(prompts_submenu)


def set_active_prompt(name):
    config = load_config()
    config["prompt"] = config["prompts"][name]
    save_config(config)
