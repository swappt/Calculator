from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, BoundedNumericProperty, ReferenceListProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class CalculatorMain(Widget):
    def build(self):
        pass

class CalculatorApp(App):
    def build(self):
        return CalculatorMain()

CalculatorApp().run()





