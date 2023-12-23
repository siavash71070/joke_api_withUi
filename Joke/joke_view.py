from PyQt5.QtWidgets import QWidget, QApplication, QLabel

from ui.joke_ui import Ui_Form


class JokeView(QWidget):

    def __init__(self):
        super(JokeView, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def show_dialog(self):
        self.show()

    def get_joke_1(self) -> QLabel:
        return self.ui.joke_1

    def get_joke_2(self) -> QLabel:
        return self.ui.joke_2

    def get_joke_3(self) -> QLabel:
        return self.ui.joke_3
