from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

def set_dark_theme(app):
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(52, 53, 65))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)

    app.setPalette(dark_palette)
    app.setStyleSheet(QSS_STYLE)


QSS_STYLE = """

QWidget {
    font-family: 'Segoe UI'; 
    font-size: 12px;
}


QDialog {
    background-color: #444654;
}

QTabWidget::pane {
    border: 1px solid #555;
}

QTabWidget::tab-bar {
    alignment: center;
}

QTabBar::tab {
    padding: 5px 15px;
    color: white;
    background-color: #444654;
    border: 1px solid #444;
    border-bottom: 0px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background-color: #343541;
    border-bottom-color: #333; 
}

QLineEdit {
    background-color: #343541;
    color: white;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 5px;
}

QComboBox {
    background-color: #343541;
    color: white;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 5px;
}

QSlider::groove:horizontal {
    border: 1px solid #555;
    background: #d9d9e3;
    height: 8px;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background: #10a37f;
    border: 1px solid #555;
    width: 18px;
    margin: -5px 0;
    border-radius: 4px;
}

QPushButton {
    background-color: #10a37f;
    color: white;
    border: 5px;
    padding: 5px 15px;
    border-radius: 4px;
    font-weight: bold;
    margin-top: 5px;
}

QPushButton:hover {
    background-color: #1a7f64;
}

QPushButton:pressed {
    background-color: #1a7f64;
}
QPushButton#removeButton {
    background-color: #444654; 
    color: white;
    border: 2px solid #10a37f;
    width: 50px; 
    height: 13px; 
}

QPushButton#removeButton:hover {
    background-color: #10a37f; 
}

QMenu {
    background-color: #444654;
    border-radius: 15px;
    margin: 5px;
    font-size: 10pt;
    padding: 5px;
}

QMenu::item {
    color: white;
    padding: 5px 10px;
    padding-right: 15px;
}

QMenu::item:selected {
    background-color: #343541;
}


# QCheckBox::indicator:checked {
#     image: url(path_to_checked_image);
# }

# QComboBox::down-arrow {
#     image: url(path_to_arrow_image);
# }


"""
