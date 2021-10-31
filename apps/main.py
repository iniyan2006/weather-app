from kivy.app import App
import kivy
from kivy.uix.label import Label
import requests
class Main(App):
    def build(self):
        rq = requests.get("https://random.dog/woof.json").json()
        text = Label(text=rq["url"])
        return text

Main().run()
