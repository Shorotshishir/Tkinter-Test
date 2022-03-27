import tkinter as tk
from tkinter import ttk

from convert_frame import ConvertFrame
from converter.temperature import TemperatureConverter


class ControlFrame(ttk.LabelFrame):

    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'  # name of this LabelFrame Instance
        self.selected_value = tk.IntVar()  # to store Radio Button's value as int
        ttk.Radiobutton(self, text='F to C', value=0,
                        variable=self.selected_value,
                        command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(self, text='dummy', value=9,
                        variable=self.selected_value,
                        command=self.do_nothing).grid(column=1, row=0, padx=5, pady=5)

        ttk.Radiobutton(self, text='C to F', value=1,
                        variable=self.selected_value,
                        command=self.change_frame).grid(column=3, row=0, padx=5, pady=5)

        self.grid(columnspan=10, row=2, padx=5, pady=5, sticky='ew')
        self.frames = {
            0: ConvertFrame(
                container,
                'Fahrenheit',
                TemperatureConverter.fahrenheit_to_celsius),
            1: ConvertFrame(
                container,
                'Celsius',
                TemperatureConverter.celsius_to_fahrenheit)
        }

        self.change_frame()

    def change_frame(self) -> None:
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()

    def do_nothing(self):
        pass
