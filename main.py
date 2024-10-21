import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aslona GUI')

        # Set window icon
        self.setWindowIcon(QIcon('icon.ico'))

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        main_layout.setSpacing(0)  # Remove spacing

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        button_layout.setSpacing(0)  # Remove spacing

        for i in "1234567890":
            button = QPushButton(i)
            button.setFixedSize(40, 40)  # Makes the buttons compact squares
            button_layout.addWidget(button)

        main_layout.addLayout(button_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        bottom_layout.setSpacing(0)  # Remove spacing

        enter_button = QPushButton('Enter')
        enter_button.setFixedSize(200, 40)  # Fixed size to match button height
        backspace_button = QPushButton('Backspace')
        backspace_button.setFixedSize(200, 40)  # Fixed size to match button height

        bottom_layout.addWidget(enter_button)
        bottom_layout.addWidget(backspace_button)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        # Set the fixed size to fit all buttons perfectly
        self.setFixedSize(400, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
