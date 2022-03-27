from tkinter import ttk


class TabbedFrame(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)

        frame1 = ttk.Frame(self)
        frame2 = ttk.Frame(self)
        ttk.Label(frame1, text="I am tab 1").grid(column=0, row=0, padx=5, pady=5)

        self.add(frame1, text="Tab 1")
        self.add(frame2, text="Tab 2")

        self.grid(columnspan=10, row=0, padx=5, pady=5, sticky="nsew")
