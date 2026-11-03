from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        self.title = "My First App"
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        layout.add_widget(Label(text="Type your name:"))

        self.entry = TextInput(multiline=False)
        layout.add_widget(self.entry)

        layout.add_widget(Button(text="OK", on_press=self.say_hello))

        self.label = Label(text="")
        layout.add_widget(self.label)

        return layout

    def say_hello(self, instance):
        name = self.entry.text
        self.label.text = f"jiji {name}!"


MyApp().run()
