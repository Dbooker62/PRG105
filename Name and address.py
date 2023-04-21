import tkinter as tk

class DialogBox:

    def __init__(self, name, street, city, state, zip_code):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

        self.root = tk.Tk()
        self.root.title("Dialog Box")
        self.root.geometry("300x200")

        self.label = tk.Label(self.root, text="Click the button to show info")
        self.label.pack(pady=10)

        self.show_info_button = tk.Button(self.root, text="Show info", command=self.show_info)
        self.show_info_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack(pady=10)

        self.root.mainloop()

    def show_info(self):
        info = f"{self.name}\n{self.street}\n{self.city}, {self.state}, {self.zip_code}"
        info_box = tk.Toplevel(self.root)
        info_box.title("Info")
        info_box.geometry("200x100")
        info_label = tk.Label(info_box, text=info)
        info_label.pack(pady=10)

name = "Dan"
street = "123 Main St"
city = "Chicago"
state = "CA"
zip_code = "12345"

dialog_box = DialogBox(name, street, city, state, zip_code)
