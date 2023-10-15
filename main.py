import sys
import openai
import time
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import (
    QApplication,
)
from app.utils.config_manager import load_config
from app.utils.keyboard_manager import listen_for_shortcut
from app.utils.tray_icon_manager import setup_tray_icon
from app.utils.theme_manager import set_dark_theme

import threading

STOP_EVENT = threading.Event()


def clean_exit():
    STOP_EVENT.set()
    time.sleep(0.5)
    app.quit()


if __name__ == "__main__":
    config = load_config()
    openai.api_key = config["api_key"]
    app = QApplication(sys.argv)

    set_dark_theme(app)

    app.setQuitOnLastWindowClosed(False)
    tray_icon = setup_tray_icon(clean_exit)

    threading.Thread(
        target=listen_for_shortcut, args=(tray_icon, config, STOP_EVENT)
    ).start()
    sys.exit(app.exec())
