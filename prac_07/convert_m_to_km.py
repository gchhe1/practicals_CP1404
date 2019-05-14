"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesConverterApp(App):
    """ convert miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def get_input(self):
        try:
            user_input = float(self.root.ids.input_miles.text)
            return user_input
        except ValueError:
            return 0.0

    def handle_calculate(self):
        """ handle calculation, output result to label widget """
        miles = self.get_input()
        kilometers = miles * 1.60934
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, increment):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param : the amount to change
        """
        display = self.get_input() + increment
        self.root.ids.input_miles.text = str(display)
        self.handle_calculate()


MilesConverterApp().run()
