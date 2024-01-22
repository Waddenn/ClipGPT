from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
)
from app.utils.config_manager import load_config
from app.constants import LOG_FILE_PATH

LOG_CONTENT = []

def custom_print(*args, color="black"):
    message = " ".join(map(str, args))
    colored_message = f'<font color="{color}">{message}</font>'
    print(message)
    LOG_CONTENT.append(colored_message)
    if len(LOG_CONTENT) > 100:
        del LOG_CONTENT[0]

    config = load_config()
    if config["save_logs_to_file"]:
        save_logs_to_file()

def save_logs_to_file():
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
        last_log = LOG_CONTENT[-1]
        log_text = (
            last_log.replace('<font color="blue">', "")
            .replace('<font color="green">', "")
            .replace('<font color="red">', "")
            .replace('<font color="black">', "")
            .replace("</font>", "")
        )
        file.write(log_text + "\n")


class LogDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.log_display = QTextEdit(self)
        self.log_display.setHtml("<br>".join(LOG_CONTENT))
        self.log_display.setFontFamily("Courier New")
        self.log_display.setReadOnly(True)

        save_logs_button = QPushButton("Save Logs to File", self)
        save_logs_button.clicked.connect(save_logs_to_file)

        layout.addWidget(QLabel("Logs:"))
        layout.addWidget(self.log_display)
        layout.addWidget(save_logs_button)

        self.resize(600, 400)
