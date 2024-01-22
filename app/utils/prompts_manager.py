
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QHBoxLayout, QInputDialog, QLineEdit, QLabel

class PromptsManager(QWidget):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setup_ui()

    def add_widget_pair(self, layout, label_text, widget):
        layout.addWidget(QLabel(label_text))
        layout.addWidget(widget)


    def setup_ui(self):
        layout = QVBoxLayout(self)

        prompt_edit_label = QLabel("Edit Prompt:", self)
        layout.addWidget(prompt_edit_label)
        self.prompt_edit = QLineEdit(self)
        layout.addWidget(self.prompt_edit)

        prompts_list_label = QLabel("Existing Prompts:", self)
        layout.addWidget(prompts_list_label)
        self.prompts_list = QListWidget(self)
        self.prompts_list.addItems(self.config["prompts"].keys())
        layout.addWidget(self.prompts_list)

        buttons_layout = QHBoxLayout()
        add_prompt_btn = QPushButton("Add", self)
        add_prompt_btn.clicked.connect(self.add_prompt)
        buttons_layout.addWidget(add_prompt_btn)

        remove_prompt_btn = QPushButton("Remove", self)
        remove_prompt_btn.clicked.connect(self.remove_prompt)
        buttons_layout.addWidget(remove_prompt_btn)
        remove_prompt_btn.setObjectName("removeButton")

        layout.addLayout(buttons_layout)

        self.prompts_list.currentItemChanged.connect(self.load_selected_prompt)

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