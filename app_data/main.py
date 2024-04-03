import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Click Example")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a frame in the center
        self.frame = QWidget(self.central_widget)
        self.frame.setGeometry(100, 100, 400, 400)

        # Create a layout for the frame
        self.layout = QVBoxLayout(self.frame)

        # Create a button with an icon
        self.button = QPushButton(self.frame)
        self.button.setIcon(QIcon('assets/icon.svg'))  # Put your icon path here
        self.button.setStyleSheet("qproperty-iconSize: 90px;")
        self.layout.addWidget(self.button)

        # Create an empty label
        self.label = QLabel(self.frame)
        self.layout.addWidget(self.label)

        # Connect button click to function
        self.button.clicked.connect(self.change_label_text)

    def change_label_text(self):
        # Replace text in the label
        temp = ""
        with open("assets/file.txt", "r") as file:
            temp = file.readlines()[0]
        self.label.setText(f'{temp}')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
