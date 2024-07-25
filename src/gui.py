import tkinter as tk
from src.gui_rumor import PageRumor
from src.gui_storepage import PageStore
import os


class MainView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.button_frame = tk.Frame(self, bg='#1e1f22')
        self.button_frame.pack(side="top", fill="x", expand=False)

        self.container = tk.Frame(self, bg='#2b2d30')
        self.container.pack(side="top", fill="both", expand=True)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path_to_data_rumor_directory = os.path.join(base_dir, "..", "data", "general_rumor.csv")
        path_to_memory_rumor_directory = os.path.join(base_dir, "..", "memory", "memory_rumor.csv")

        self.p1 = PageRumor(self.container,
                            path_to_data_rumor_directory,
                            path_to_memory_rumor_directory)
        self.p2 = PageStore(self.container)

        self.p1.place(x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_buttons()
        self.p1.show()

    def create_buttons(self):
        b1 = tk.Button(self.button_frame, text="Rumors", command=self.p1.show, bg='#2b2d30', fg='white')
        b1.pack(side="left")

        b2 = tk.Button(self.button_frame, text="Store", command=self.p2.show, bg='#2b2d30', fg='white')
        b2.pack(side="left")


def start_gui():
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x700")
    root.mainloop()
