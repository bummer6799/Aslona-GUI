import sys, os
import pyautogui
import pygetwindow as gw
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aslona GUI (Unofficial)')
        self.setGeometry(100, 100, 400, 80)

        # Set window icon
        self.setWindowIcon(QIcon(os.path.join(basedir,'icon.ico')))

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        main_layout.setSpacing(0)  # Remove spacing

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        button_layout.setSpacing(0)  # Remove spacing

        for i in "1234567890":
            button = QPushButton(i)
            button.setFixedSize(40, 40)  # Makes the buttons compact squares
            button.clicked.connect(self.button_clicked)  # Connect button click to handler
            button_layout.addWidget(button)

        main_layout.addLayout(button_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        bottom_layout.setSpacing(0)  # Remove spacing

        backspace_button = QPushButton('Backspace')
        backspace_button.setFixedSize(200, 40)  # Fixed size to match button height
        backspace_button.clicked.connect(self.backspace_clicked)

        enter_button = QPushButton('Enter')
        enter_button.setFixedSize(200, 40)  # Fixed size to match button height
        enter_button.clicked.connect(self.enter_clicked)

        bottom_layout.addWidget(backspace_button)
        bottom_layout.addWidget(enter_button)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        # Set the fixed size to fit all buttons perfectly
        self.setFixedSize(400, 80)

    def focus_target_window(self):
        self.current_window = gw.getActiveWindow().title
        target_window = gw.getWindowsWithTitle('Warsim')[0]
        if target_window:
            target_window.activate()

    def return_to_gui(self):
        if self.current_window:
            gw.getWindowsWithTitle(self.current_window)[0].activate()

    def button_clicked(self):
        self.focus_target_window()
        button = self.sender()
        pyautogui.write(button.text())
        self.return_to_gui()

    def enter_clicked(self):
        self.focus_target_window()
        pyautogui.press('enter')
        self.return_to_gui()

    def backspace_clicked(self):
        self.focus_target_window()
        pyautogui.press('backspace')
        self.return_to_gui()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))  # Set the application icon
    window = Window()
    window.show()
    sys.exit(app.exec())
