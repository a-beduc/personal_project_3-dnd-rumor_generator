import tkinter as tk
from src.page import Page


class PageStore(Page):
    # Just some placeholder to test if i can add multiple pages using tkinter
    def __init__(self, parent, *args, **kwargs):
        Page.__init__(self, parent, *args, **kwargs)
        label = tk.Label(self, text="Store")
        label.pack(side="top", fill="both", expand=True)
