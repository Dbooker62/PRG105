"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2
class MyGUI2:
    def _init_(self):
        self.main_window = tkinter.Tk()

        tkinter.mainloop()

my_gui=MyGUI2()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2



class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.name_label = tkinter.Label(self.main_window, text="John Doe")
        self.name_label.pack()

        tkinter.mainloop()


my_gui=MyGUI2()
import tkinter as tk
# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3
class MyGUI3:
    def __init__(self, master):
        self.master = master
        master.title("MyGUI3")

        # Create top frame and add labels with name and major
        top_frame = tk.Frame(master)
        top_frame.pack(side=tk.TOP)
        tk.Label(top_frame, text="Name: Your Name").pack()
        tk.Label(top_frame, text="Major: Your Major").pack()

        # Create bottom frame and add labels with classes
        bottom_frame = tk.Frame(master)
        bottom_frame.pack(side=tk.BOTTOM)
        tk.Label(bottom_frame, text="Classes this semester:").pack()
        tk.Label(bottom_frame, text="Class 1").pack()
        tk.Label(bottom_frame, text="Class 2").pack()
        tk.Label(bottom_frame, text="Class 3").pack()

root = tk.Tk()
my_gui = MyGUI3(root)
root.mainloop()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI

class JokeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Joke GUI")

        self.joke_label = tk.Label(master, text="Why did the chicken cross the road?")
        self.joke_label.pack(pady=10)

        self.punchline_button = tk.Button(master, text="Show Punchline", command=self.show_punchline)
        self.punchline_button.pack(pady=10)

    def show_punchline(self):
        messagebox.showinfo("Punchline", "To get to the other side!")


root = tk.Tk()
joke_gui = JokeGUI(root)
root.mainloop()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters

class InchesToCmConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Inches to Centimeters Converter")

        self.inches_label = tk.Label(master, text="Inches:")
        self.inches_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.inches_entry = tk.Entry(master)
        self.inches_entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.cm_label = tk.Label(master, text="")
        self.cm_label.pack(side=tk.LEFT, padx=10, pady=10)

    def convert(self):
        try:
            inches = float(self.inches_entry.get())
            cm = inches * 2.54
            self.cm_label.config(text=f"{inches:.2f} inches = {cm:.2f} cm")
        except ValueError:
            self.cm_label.config(text="Invalid input, please enter a number")


root = tk.Tk()
converter = InchesToCmConverter(root)
root.mainloop()
