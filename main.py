import sys
import os
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)

base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "style.qss")) as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()

sys.exit(app.exec())