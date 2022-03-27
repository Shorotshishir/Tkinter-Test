import tkinter as tk

from control_frame import ControlFrame


# from tabbed_frame import TabbedFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry("400x400")
        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1
        # cols = rows
        # nums = [str(x) for x in range(100)]
        # count = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         label = ttk.Label(self, text=nums[count])
        #         label.grid(row=i, column=j)
        #         count += 1
        # ttk.Style().theme_use("black")
        self.resizable(False, False)


if __name__ == '__main__':
    app = App()  # Create a new App

    ControlFrame(app)  # create a control frame as a child of App
    # TabbedFrame(app)
    app.mainloop()  # run the apps main loop
