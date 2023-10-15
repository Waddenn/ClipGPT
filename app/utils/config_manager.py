import json
import os
from tkinter.ttk import Combobox
from PyQt6.QtWidgets import (
    QDialog,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QCheckBox,
    QListWidget,
    QInputDialog,
    QHBoxLayout,
    QTabWidget,
    QWidget,
    QComboBox,
    QSlider,
)
from PyQt6.QtCore import Qt

from config.constants import DEFAULT_CONFIG, AVAILABLE_MODELS, MODEL_TOKEN_RANGES
from app.constants import CONFIG_FILE_PATH


def load_config():
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_CONFIG


def save_config(config):
    with open(CONFIG_FILE_PATH, "w") as f:
        json.dump(config, f)


class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config = load_config()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.tab_widget = QTabWidget(self)
        layout.addWidget(self.tab_widget)

        self.setup_general_config()
        self.setup_prompts_management()

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_and_close)
        layout.addWidget(save_button)

        # self.setFixedSize(304, 441)

    def add_widget_pair(self, layout, label_text, widget):
        layout.addWidget(QLabel(label_text))
        layout.addWidget(widget)

    def setup_general_config(self):
        general_tab, tab_layout = self.create_tab("General")

        self.api_key_edit = QLineEdit(self.config["api_key"], self)
        self.add_widget_pair(tab_layout, "API Key:", self.api_key_edit)

        self.model_name_combo = QComboBox(self)
        self.model_name_combo.addItems(AVAILABLE_MODELS)
        self.model_name_combo.setCurrentText(self.config["model_name"])
        self.add_widget_pair(tab_layout, "Model Name:", self.model_name_combo)

        self.token_value_label = QLabel(
            f"Max Tokens: {self.config['max_tokens']}", self
        )

        self.token_slider = QSlider(Qt.Orientation.Horizontal, self)

        self.update_slider_range(self.config["model_name"])
        self.token_slider.setValue(self.config["max_tokens"])

        self.model_name_combo.currentTextChanged.connect(self.update_slider_range)

        self.token_slider.valueChanged.connect(self.update_token_value)

        self.update_token_value(self.token_slider.value())

        tab_layout.addWidget(self.token_value_label)
        tab_layout.addWidget(self.token_slider)

        self.temperature_value_label = QLabel(
            f"Temperature: {self.config['temperature']}", self
        )
        self.temperature_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.temperature_slider.setRange(0, 20)
        self.temperature_slider.setValue(int(self.config["temperature"] * 10))
        self.temperature_slider.setSingleStep(1)
        self.temperature_slider.valueChanged.connect(self.update_temperature_value)
        tab_layout.addWidget(self.temperature_value_label)
        tab_layout.addWidget(self.temperature_slider)

        self.save_logs_checkbox = QCheckBox("Save logs to file", self)
        self.save_logs_checkbox.setChecked(self.config["save_logs_to_file"])
        tab_layout.addWidget(self.save_logs_checkbox)

    def setup_prompts_management(self):
        prompts_tab, tab_layout = self.create_tab("Prompts")

        self.prompt_edit = QLineEdit(self)
        self.add_widget_pair(tab_layout, "Edit Prompt:", self.prompt_edit)

        self.prompts_list = QListWidget(self)
        self.prompts_list.addItems(self.config["prompts"].keys())
        self.add_widget_pair(tab_layout, "Existing Prompts:", self.prompts_list)

        buttons_layout = QHBoxLayout()
        add_prompt_btn = QPushButton("Add", self)
        add_prompt_btn.clicked.connect(self.add_prompt)
        buttons_layout.addWidget(add_prompt_btn)

        remove_prompt_btn = QPushButton("Remove", self)
        remove_prompt_btn.clicked.connect(self.remove_prompt)
        buttons_layout.addWidget(remove_prompt_btn)

        tab_layout.addLayout(buttons_layout)

        self.prompts_list.currentItemChanged.connect(self.load_selected_prompt)

    def create_tab(self, name):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.tab_widget.addTab(tab, name)
        return tab, layout

    def add_prompt(self):
        text, ok = QInputDialog.getText(self, "Add Prompt", "Enter Prompt Name:")
        if ok:
            self.config["prompts"][text] = ""
            self.prompts_list.addItem(text)

    def remove_prompt(self):
        current_item = self.prompts_list.currentItem()
        if current_item:
            del self.config["prompts"][current_item.text()]
            self.prompts_list.takeItem(self.prompts_list.row(current_item))

    def load_selected_prompt(self, current_item):
        if current_item:
            prompt_content = self.config["prompts"][current_item.text()]
            self.prompt_edit.setText(prompt_content)
        else:
            self.prompt_edit.clear()

    def save_and_close(self):
        from app.utils.tray_icon_manager import refresh_prompts_submenu

        self.config["api_key"] = self.api_key_edit.text()
        self.config["model_name"] = self.model_name_combo.currentText()
        self.config["max_tokens"] = self.token_slider.value()
        self.config["temperature"] = self.temperature_slider.value() / 10.0
        self.config["save_logs_to_file"] = self.save_logs_checkbox.isChecked()
        current_item = self.prompts_list.currentItem()
        if current_item:
            self.config["prompts"][current_item.text()] = self.prompt_edit.text()
        save_config(self.config)
        refresh_prompts_submenu()

    def update_slider_range(self, model_name):
        min_val, max_val = MODEL_TOKEN_RANGES.get(model_name, (0, 4096))
        self.token_slider.setRange(min_val, max_val)
        self.update_token_value(self.token_slider.value())

    def update_token_value(self, value):
        self.token_value_label.setText(f"Max Tokens: {value}")

    def update_temperature_value(self, value):
        real_value = value / 10.0
        self.temperature_value_label.setText(f"Temperature: {real_value:.1f}")
