from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (
    QWidget
)


class CalendarView(QWidget):
    def __init__(self):
        super(CalendarView, self).__init__()
        self.setupUI()

    def setupUI(self):
        #Fun Area