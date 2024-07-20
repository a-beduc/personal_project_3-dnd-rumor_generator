import tkinter as tk

# class GUI:
#     def __init__(self, root):
#         self.root = root


def main():
    root = tk.Tk()
    root.configure(bg='#2b2d30')
    root.geometry('500x500')
    root.title("Rumor generator")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=10, pady=10, bg="#1e1f22")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    frame.columnconfigure(0, weight=3)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=12)
    frame.rowconfigure(2, weight=1)

    title = tk.Label(frame, text="Rumor_title", font=("Helvetica", 15))
    title.grid(column=0, row=0, columnspan=1, sticky="nsew")

    rumor_id = tk.Label(frame, text="Rumor_ID", font=("Helvetica", 10))
    rumor_id.grid(column=1, row=0, columnspan=1, sticky="nsew")

    rumor_text = tk.Label(frame, text="Rumor_text", font=("Helvetica", 10))
    rumor_text.grid(column=0, row=1, columnspan=2, sticky="nsew")

    shelf_button = tk.Button(frame, text="Archiver", font=("Helvetica", 10))
    shelf_button.grid(column=0, row=2, columnspan=2, sticky="nsew")





    root.mainloop()


if __name__ == '__main__':
    main()