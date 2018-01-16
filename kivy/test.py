from kivy.app import App
from kivy.uix.label import Label


from kivy.lang import Builder

Builder.load_string('''
<MyLabel>:
    text: 'Hello World'
''')

class MyLabel(Label): pass
class AwesomeApp(App):
    def build(self):
        return MyLabel()

if __name__ == "__main__":
    AwesomeApp().run()
