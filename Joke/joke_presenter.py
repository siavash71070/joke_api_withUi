from PyQt5.QtWidgets import QWidget

from Joke.joke_view import JokeView


class JokePresenter:
    def __init__(self):
        self.view = JokeView()
        self.show_dialog()

    def set_jokes(self, val_1: str, val_2: str, val_3: str):
        self.view.get_joke_1().setText(val_1)
        self.view.get_joke_2().setText(val_2)
        self.view.get_joke_3().setText(val_3)

    def show_dialog(self) -> QWidget:
        return self.view.show_dialog()