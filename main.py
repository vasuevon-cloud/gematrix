from kivy.app import App
from kivy.uix.label import Label

class GematrixApp(App):
    def build(self):
        return Label(text="Gematrix is alive")

if __name__ == "__main__":
    GematrixApp().run()


