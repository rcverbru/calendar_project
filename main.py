from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spooky")
        button = QPushButton("Touch Me")

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(button)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()