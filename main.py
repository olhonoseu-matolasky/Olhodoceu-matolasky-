from kivy.app import App
from kivy.uix.label import Label
class OlhoApp(App):
    def build(self):
        return Label(text='Olho do Ceu - Matola Sky\n\nJupiter: Leste\nCruzeiro Sul: Sul\nLua: Oeste')
OlhoApp().run()
