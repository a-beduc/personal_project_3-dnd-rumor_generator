import tkinter as tk
from src.extractor import RumorGenerator
import os


class GUI:
    def __init__(self, root, init_file_path=None, memory_file_path=None):
        self.root = root
        self.root.configure(bg='#2b2d30')
        self.root.geometry('500x500')
        self.root.title("Rumor generator")
        self.root.resizable(False, False)

        self.init_file_path = init_file_path
        self.memory_file_path = memory_file_path

        self.frame = tk.Frame(root, padx=5, pady=5, bg="#1e1f22")
        self.frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.frame.columnconfigure(0, weight=2)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=2)
        self.frame.rowconfigure(1, weight=12)
        self.frame.rowconfigure(2, weight=1)

        self.rumors = RumorGenerator(self.init_file_path, self.memory_file_path)

        self.rumor_title = None
        self.rumor_id = None
        self.rumor_text = None

        self.create_widget()

    def create_widget(self):
        self.rumor_title = tk.Label(self.frame, text="", font=("Helvetica", 15), width=40, height=2, anchor="w",
                                    padx=10)
        self.rumor_title.grid(column=0, row=0, columnspan=2, sticky="nsew")

        self.rumor_id = tk.Label(self.frame, text="", font=("Helvetica", 10), width=20, height=1, anchor="e", padx=10)
        self.rumor_id.grid(column=2, row=0, columnspan=1, sticky="nsew")

        self.rumor_text = tk.Label(self.frame, text="", justify="left", wraplength=460, font=("Helvetica", 10),
                                   width=40, height=10, anchor="nw", padx=10)
        self.rumor_text.grid(column=0, row=1, columnspan=3, sticky="nsew")

        save_button = tk.Button(self.frame, text="Save", font=("Helvetica", 10), width=20, height=2,
                                command=self.save_memory)
        save_button.grid(column=0, row=2, sticky="nsew")

        shelf_button = tk.Button(self.frame, text="Archiver", font=("Helvetica", 10), width=20, height=2,
                                 command=self.archive_memory)
        shelf_button.grid(column=1, row=2, sticky="nsew")

        next_button = tk.Button(self.frame, text="Next", font=("Helvetica", 10), width=20, height=2,
                                command=self.update_rumor)
        next_button.grid(column=2, row=2, sticky="nsew")

    def update_rumor(self):
        self.rumors.get_random_rumor()
        current_rumor = self.rumors.current_rumor
        self.rumor_title.config(text=str(current_rumor.rumor_title))
        self.rumor_id.config(text=str(current_rumor.rumor_id))
        self.rumor_text.config(text=str(current_rumor.rumor_text))

    def archive_memory(self):
        self.rumors.update_memory()

    def save_memory(self):
        self.rumors.rumor_memory.save_memory()


def start_gui(data_directory, memory_file):
    root = tk.Tk()
    GUI(root, init_file_path=data_directory, memory_file_path=memory_file)
    root.mainloop()

