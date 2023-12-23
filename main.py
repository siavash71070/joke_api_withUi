from PyQt5.QtWidgets import QApplication
from Joke.joke_presenter import JokePresenter
from JokeAPI.joke_api import A, B, C


class MainProject:

    def __init__(self):
        self.view = JokePresenter()
        self.connections()
        self.joke_1 = A(api_token="/76aLMzJPQwehEwmOcLkXg==LmJNLpxZgVKGWShN")
        self.joke_2 = B()
        self.joke_3 = C()

    def connections(self):
        self.view.view.ui.get_jokes_button.clicked.connect(self.show_jokes)

    def run_dialog(self):
        self.view.show_dialog()

    def show_jokes(self):
        text_1 = self.joke_1.get_random()
        text_2 = self.joke_2.get_random()
        text_3 = self.joke_3.get_random()
        self.view.set_jokes(text_1, text_2, text_3)


if __name__ == '__main__':
    app = QApplication([])
    window = MainProject()
    window.run_dialog()
    app.exec_()
