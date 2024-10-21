import sys
import os
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
        self.setGeometry(100, 100, 440, 100)  # Adjust width and height

        # Set window icon
        self.setWindowIcon(QIcon(os.path.join(basedir, 'icon.ico')))

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

        backspace_button = QPushButton('Backspace')
        backspace_button.setFixedSize(80, 40)  # Make the Backspace button twice the length
        backspace_button.clicked.connect(self.backspace_clicked)
        button_layout.addWidget(backspace_button)

        main_layout.addLayout(button_layout)

        enter_button = QPushButton('Enter')
        enter_button.setFixedSize(480, 40)  # Make the Enter button span the entire bottom row
        enter_button.clicked.connect(self.enter_clicked)

        main_layout.addWidget(enter_button)

        self.setLayout(main_layout)

        # Adjust window size to fit all buttons perfectly
        self.setFixedSize(480, 80)

    def focus_target_window(self):
        try:
            self.current_window = gw.getActiveWindow().title
            target_window = gw.getWindowsWithTitle('Warsim')[0]
            if target_window:
                target_window.activate()
                return True
            else:
                raise IndexError("Warsim window not found")
        except IndexError:
            self.show_error()
            return False
        except Exception as e:
            self.show_error(str(e))
            return False

    def return_to_gui(self):
        try:
            if hasattr(self, 'current_window') and self.current_window:
                gw.getWindowsWithTitle(self.current_window)[0].activate()
        except Exception:
            pass

    def show_error(self, message='Warsim: The Realm of Aslona is not open.'):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle('Error')
        msg.exec()

    def button_clicked(self):
        if self.focus_target_window():
            button = self.sender()
            pyautogui.write(button.text())
            self.return_to_gui()

    def enter_clicked(self):
        if self.focus_target_window():
            pyautogui.press('enter')
            self.return_to_gui()

    def backspace_clicked(self):
        if self.focus_target_window():
            pyautogui.press('backspace')
            self.return_to_gui()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'icon.ico')))  # Set the application icon
    window = Window()
    window.show()
    sys.exit(app.exec())
