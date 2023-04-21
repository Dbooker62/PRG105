import tkinter as tk

class GasMileageCalculator:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gas Mileage Calculator")
        self.root.geometry("300x200")

        self.gallons_label = tk.Label(self.root, text="Number of gallons of gas:")
        self.gallons_label.pack(pady=10)

        self.gallons_entry = tk.Entry(self.root)
        self.gallons_entry.pack(pady=5)

        self.miles_label = tk.Label(self.root, text="Number of miles on a full tank:")
        self.miles_label.pack(pady=10)

        self.miles_entry = tk.Entry(self.root)
        self.miles_entry.pack(pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate MPG", command=self.calculate_mpg)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.root.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())
            mpg = miles / gallons
            print(f"MPG: {mpg:.2f}")
            self.result_label.config(text=f"MPG: {mpg:.2f}")
            print(self.result_label.cget("text"))
        except ValueError:
            self.result_label.config(text="Please enter valid numbers.")
            print(self.result_label.cget("text"))



calculator = GasMileageCalculator()
