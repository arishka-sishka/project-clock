import sys

from PyQt5.QtWidgets import QApplication

from App import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
