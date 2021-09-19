import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Root(BoxLayout):
    def __init__(self):
        super(Root, self).__init__()

    def generate_pokemon(self):
        if self.text.text == '':
            self.title.text = 'Enter a valid location'
        elif self.text.text != '':
            try:
                re = requests.get('http://api.weatherapi.com/v1/current.json?key=a57b868d6b31402ebb2131108211709&q={}&aqi=no'.format(self.text.text)).json()
                data = re['current']
                self.title.text = str(data['condition']['text'])
                self.image.source = 'https:{}'.format(str(data['condition']['icon']))
                self.temp.text = 'Temprature : {}C ({}F)'.format(str(data['temp_c']), str(data['temp_f']))
                self.windkm.text = 'wind speed: {} kph'.format(data['wind_kph'])
                self.uv.text = 'uv rays: {}'.format(data['uv'])
                self.humidity.text = 'humidity : {}%'.format(data['humidity'])
                self.feel.text = 'feels like : {}C {}F '.format(data['feelslike_c'], data['feelslike_f'])
            except:
                self.title.text = 'Enter a valid city'
class Rand(App):
    def build(self):
        return Root()

rand_num = Rand()
rand_num.run()
