import tkinter as tk
from tkinter import ttk
from src.rumor import RumorGenerator


class GUI:
    """ Class that contains the GUI"""

    def __init__(self, root, init_file_path=None, memory_file_path=None):
        self.root = root
        self.root.configure(bg='#2b2d30')
        self.root.geometry('600x600')
        self.root.title("Rumor generator")
        self.root.resizable(False, False)

        self.init_file_path = init_file_path
        self.memory_file_path = memory_file_path

        self.frame = tk.Frame(root, padx=5, pady=5, bg="#1e1f22")
        self.frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=2)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.frame.columnconfigure(5, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)

        self.rumors = RumorGenerator(self.init_file_path, self.memory_file_path)

        self.rumor_title = None
        self.rumor_id = None
        self.rumor_text = None
        self.current_tags = []

        self.tag_all_var = tk.IntVar()
        self.tag_boi_var = tk.IntVar()
        self.tag_hou_var = tk.IntVar()
        self.tag_bre_var = tk.IntVar()
        self.tag_bry_var = tk.IntVar()
        self.tag_din_var = tk.IntVar()
        self.tag_kon_var = tk.IntVar()
        self.tag_hav_var = tk.IntVar()
        self.tag_tar_var = tk.IntVar()
        self.tag_ter_var = tk.IntVar()
        self.tag_dou_var = tk.IntVar()

        self.create_widget()

    def create_widget(self):
        """Method to create the widget ; initialize its values to nothing"""
        self.rumor_title = tk.Label(self.frame, text="", font=("Helvetica", 15), width=40, height=2, anchor="w",
                                    padx=10)
        self.rumor_title.grid(column=0, row=0, columnspan=4, sticky="nsew")

        self.rumor_id = tk.Label(self.frame, text="", font=("Helvetica", 10), width=20, height=1, anchor="e", padx=10)
        self.rumor_id.grid(column=4, row=0, columnspan=2, sticky="nsew")

        self.rumor_text = tk.Label(self.frame, text="", justify="left", wraplength=560, font=("Helvetica", 10),
                                   width=40, height=10, anchor="nw", padx=10)
        self.rumor_text.grid(column=0, row=1, columnspan=6, sticky="nsew")

        tag_all = ttk.Checkbutton(self.frame, text="all", variable=self.tag_all_var, command=self.check_all)
        tag_all.grid(column=0, row=2, rowspan=2, sticky="nsew")
        self.tag_all_var.set(1)

        tag_boi = ttk.Checkbutton(self.frame, text="boi", variable=self.tag_boi_var)
        tag_boi.grid(column=1, row=2, sticky="nsew")
        self.tag_boi_var.set(1)

        tag_hou = ttk.Checkbutton(self.frame, text="hou", variable=self.tag_hou_var)
        tag_hou.grid(column=2, row=2, sticky="nsew")
        self.tag_hou_var.set(1)

        tag_bre = ttk.Checkbutton(self.frame, text="bre", variable=self.tag_bre_var)
        tag_bre.grid(column=3, row=2, sticky="nsew")
        self.tag_bre_var.set(1)

        tag_bry = ttk.Checkbutton(self.frame, text="bry", variable=self.tag_bry_var)
        tag_bry.grid(column=4, row=2, sticky="nsew")
        self.tag_bry_var.set(1)

        tag_din = ttk.Checkbutton(self.frame, text="din", variable=self.tag_din_var)
        tag_din.grid(column=5, row=2, sticky="nsew")
        self.tag_din_var.set(1)

        tag_kon = ttk.Checkbutton(self.frame, text="kon", variable=self.tag_kon_var)
        tag_kon.grid(column=1, row=3, sticky="nsew")
        self.tag_kon_var.set(1)

        tag_hav = ttk.Checkbutton(self.frame, text="hav", variable=self.tag_hav_var)
        tag_hav.grid(column=2, row=3, sticky="nsew")
        self.tag_hav_var.set(1)

        tag_tar = ttk.Checkbutton(self.frame, text="tar", variable=self.tag_tar_var)
        tag_tar.grid(column=3, row=3, sticky="nsew")
        self.tag_tar_var.set(1)

        tag_ter = ttk.Checkbutton(self.frame, text="ter", variable=self.tag_ter_var)
        tag_ter.grid(column=4, row=3, sticky="nsew")
        self.tag_ter_var.set(1)

        tag_dou = ttk.Checkbutton(self.frame, text="dou", variable=self.tag_dou_var)
        tag_dou.grid(column=5, row=3, sticky="nsew")
        self.tag_dou_var.set(1)

        save_button = tk.Button(self.frame, text="Save", font=("Helvetica", 10), width=20, height=2,
                                command=self.save_memory)
        save_button.grid(column=0, row=4, columnspan=2, sticky="nsew")

        shelf_button = tk.Button(self.frame, text="Archiver", font=("Helvetica", 10), width=20, height=2,
                                 command=self.archive_memory)
        shelf_button.grid(column=2, row=4, columnspan=2, sticky="nsew")

        next_button = tk.Button(self.frame, text="Next", font=("Helvetica", 10), width=20, height=2,
                                command=self.update_rumor)
        next_button.grid(column=4, row=4, columnspan=2, sticky="nsew")

    def update_rumor(self):
        """Method to get a new rumor and update the content of the widgets"""
        self.check_current_tags()
        self.rumors.remove_by_tag(self.current_tags)
        self.rumors.get_random_rumor()
        current_rumor = self.rumors.current_rumor
        self.rumor_title.config(text=str(current_rumor.rumor_title))
        self.rumor_id.config(text=str(current_rumor.rumor_id))
        self.rumor_text.config(text=str(current_rumor.rumor_text))

    def archive_memory(self):
        """Method to add the current rumor_id to the active memory"""
        self.rumors.update_memory()

    def save_memory(self):
        """Method to write the active memory in the memory.csv file and allows it to be saved
            from one session to the next"""
        self.rumors.rumor_memory.save_memory()

    def check_all(self):
        if self.tag_all_var.get() == 0:
            self.tag_all_var.set(0)
            self.tag_boi_var.set(0)
            self.tag_hou_var.set(0)
            self.tag_bre_var.set(0)
            self.tag_bry_var.set(0)
            self.tag_din_var.set(0)
            self.tag_kon_var.set(0)
            self.tag_hav_var.set(0)
            self.tag_tar_var.set(0)
            self.tag_ter_var.set(0)
            self.tag_dou_var.set(0)

        else:
            self.tag_all_var.set(1)
            self.tag_boi_var.set(1)
            self.tag_hou_var.set(1)
            self.tag_bre_var.set(1)
            self.tag_bry_var.set(1)
            self.tag_din_var.set(1)
            self.tag_kon_var.set(1)
            self.tag_hav_var.set(1)
            self.tag_tar_var.set(1)
            self.tag_ter_var.set(1)
            self.tag_dou_var.set(1)

    def check_current_tags(self):
        self.current_tags = []
        if self.tag_boi_var.get() == 1:
            self.current_tags.append("tag_boi")

        if self.tag_hou_var.get() == 1:
            self.current_tags.append("tag_hou")

        if self.tag_bre_var.get() == 1:
            self.current_tags.append("tag_bre")

        if self.tag_bry_var.get() == 1:
            self.current_tags.append("tag_bry")

        if self.tag_din_var.get() == 1:
            self.current_tags.append("tag_din")

        if self.tag_kon_var.get() == 1:
            self.current_tags.append("tag_kon")

        if self.tag_hav_var.get() == 1:
            self.current_tags.append("tag_hav")

        if self.tag_tar_var.get() == 1:
            self.current_tags.append("tag_tar")

        if self.tag_ter_var.get() == 1:
            self.current_tags.append("tag_ter")

        if self.tag_dou_var.get() == 1:
            self.current_tags.append("tag_dou")


def start_gui(data_directory, memory_file):
    """Function to start the app"""
    root = tk.Tk()
    GUI(root, init_file_path=data_directory, memory_file_path=memory_file)
    root.mainloop()
