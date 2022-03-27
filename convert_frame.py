import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class ConvertFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter
        # Grid
        self.grid(columnspan=10, row=0, padx=5, pady=5, sticky="nsew")
        options = {'padx': 10, 'pady': 10}

        # label
        self.result_label = ttk.Label(self)
        self.result_label.grid(column=0, row=0, **options)

        # Temperature Label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)

        # Temperature Entry Label
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature, foreground='red2')
        self.temperature_entry.grid(column= 1, columnspan=7, row=0, **options)
        self.temperature_entry.focus()

        # Convert Button
        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=10, row=0, sticky=tk.W, **options)

        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # # Grid
        # self.grid(columnspan=10, row=0, padx=5, pady=5, sticky="nsew")

    def convert(self) -> None:
        """
        handles button click
        :return:
        """
        try:
            input_value = float(self.temperature.get())
            result = self.converter(input_value)

            self.result_label.config(text=result)
        except ValueError as err:
            showerror(title="Error", message=str(err))

    def reset(self) -> None:
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''
