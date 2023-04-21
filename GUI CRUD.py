# This program implements a simple CRUD (Create, Read, Update, Delete) GUI program
# Code is included to change font size for accessibility
import tkinter
import tkinter.messagebox
import tkinter.font as tkfont
import pickle


# main (root) GUI menu
class CrudGUI:
	def __init__(self, master):
		# the primary window (master) was initialized in the main() program
		#  -- save the master parameter in an instance variable to make it available throughout the class
		self.master = master
		self.master.title('Welcome Menu')

		# these statements tell Tkinter what font size to use for the default font
		default_font = tkfont.nametofont("TkDefaultFont")
		# TODO: change the size to use a larger value for better visibility
		default_font.configure(size=18)

		# create two frames -- one for the menu, one for the buttons
		self.top_frame = tkinter.Frame(self.master)
		self.bottom_frame = tkinter.Frame(self.master)

		# the menu uses Radiobuttons so that only one option is selected at any time -- start by selecting option 1
		self.radio_var = tkinter.IntVar()
		self.radio_var.set(1)

		# create the radio buttons
		self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
		                                variable=self.radio_var, value=1)
		self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
		                               variable=self.radio_var, value=2)
		self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
		                                  variable=self.radio_var, value=3)
		self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
		                                  variable=self.radio_var, value=4)

		# for visibility at a larger scale, you can turn off the radiobutton indicator (icon)
		#  -- resulting in a push-button look (set indicatoron to False)
		#  -- (Tkinter also provides an option to provide custom images for the icons)
		self.look.configure(indicatoron=False)
		self.add.configure(indicatoron=False)
		self.change.configure(indicatoron=False)
		self.delete.configure(indicatoron=False)

		# pack the radio buttons
		self.look.pack(anchor='w', padx=20)
		self.add.pack(anchor='w', padx=20)
		self.change.pack(anchor='w', padx=20)
		self.delete.pack(anchor='w', padx=20)

		# create ok and quit buttons
		self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu, width=10)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, width=10)

		# pack the buttons
		self.ok_button.pack(side='left')
		self.quit_button.pack(side='left')

		# pack the frames
		self.top_frame.pack()
		self.bottom_frame.pack()

	# this method is called to process the menu choice when the OK button is pressed
	# TODO: you will need to modify this method to add more menu options based on the radio button selection
	#  -- each menu item should be instantiated as an appropriate class similar to the example provided
	#  -- you will add classes to Add/Create, Update, and Delete entries (the Read/Look class is provided)
	def open_menu(self):
		if self.radio_var.get() == 1:
			_ = LookGUI(self.master)
		elif self.radio_var.get() == 2:
			_ = CreateGUI(self.master)
		elif self.radio_var.get() == 3:
			_ = UpdateGUI(self.master)
		elif self.radio_var.get() == 4:
			_ = DeleteGUI(self.master)
		else:
			tkinter.messagebox.showinfo('Function', 'still under construction')


# This example class processes the first user choice -- to look for a name (the Read option)
class LookGUI:
	def __init__(self, master):

		# open the file, load to customers, close file. Do this in each class
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		# tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
		# when the Toplevel window is closed, it returns focus to the master window
		self.look = tkinter.Toplevel(master)
		self.look.title('Search for customer')

		# create Frames for this Toplevel window
		self.top_frame = tkinter.Frame(self.look)
		self.middle_frame = tkinter.Frame(self.look)
		self.bottom_frame = tkinter.Frame(self.look)

		# widgets for top frame - label and entry box for name
		self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
		# Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
		self.search_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		# pack top frame
		self.search_label.pack(side='left')
		self.search_entry.pack(side='left')

		# middle frame - label for results
		self.info_string = tkinter.StringVar()
		self.info = tkinter.Label(self.middle_frame, text='Results: ')
		self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string)

		# pack Middle frame
		self.info.pack(side='left')
		self.result_label.pack(side='left')

		# buttons for bottom frame
		self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		# pack bottom frame
		self.search_button.pack(side='left')
		self.back_button.pack(side='left')

		# pack frames into the Toplevel window
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

	# this method is called by the Search button
	def search(self):
		# get the data from the entry box
		name = self.search_entry.get()
		# look for the name in the dictionary
		result = self.customers.get(name, 'Not Found')
		# display the result in the info label by setting its associated StringVar
		self.info_string.set(result)

	# this method is called by the Main Menu button to destroy the current window and return to the primary
	def go_back(self):
		self.look.destroy()


# TODO: you need to create classes similar to the LookGUI class for the other tasks: Create, Update, Delete
#  -- the logic to process each choice for the OK button should be
#  -- similar to the logic used in your Name and Email Address program
# TODO: Remember to pickle your data file after each change to the dictionary
class CreateGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.create = tkinter.Toplevel(master)
        self.create.title('Add a customer')

        self.top_frame = tkinter.Frame(self.create)
        self.middle_frame = tkinter.Frame(self.create)
        self.bottom_frame = tkinter.Frame(self.create)

        self.name_label = tkinter.Label(self.top_frame, text='Enter customer name: ')
        self.name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

        self.balance_label = tkinter.Label(self.middle_frame, text='Enter balance: ')
        self.balance_entry = tkinter.Entry(self.middle_frame, width=15, font="TkDefaultFont")

        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add_customer, width=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.balance_label.pack(side='left')
        self.balance_entry.pack(side='left')
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add_customer(self):
        name = self.name_entry.get()
        balance = self.balance_entry.get()
        self.customers[name] = float(balance)
        self.save_customers()
        tkinter.messagebox.showinfo('Success', 'Customer added.')

    def go_back(self):
        self.create.destroy()

    def save_customers(self):
        output_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, output_file)
        output_file.close()


class UpdateGUI:
	def __init__(self, master):
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		self.update = tkinter.Toplevel(master)
		self.update.title('Update customer')

		self.top_frame = tkinter.Frame(self.update)
		self.middle_frame = tkinter.Frame(self.update)
		self.bottom_frame = tkinter.Frame(self.update)

		self.name_label = tkinter.Label(self.top_frame, text='Enter customer name to update: ')
		self.name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		self.phone_label = tkinter.Label(self.middle_frame, text='Enter new phone number: ')
		self.phone_entry = tkinter.Entry(self.middle_frame, width=15, font="TkDefaultFont")

		self.update_button = tkinter.Button(self.bottom_frame, text='Update', command=self.update_customer, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		self.name_label.pack(side='left')
		self.name_entry.pack(side='left')
		self.phone_label.pack(side='left')
		self.phone_entry.pack(side='left')
		self.update_button.pack(side='left')
		self.back_button.pack(side='left')

		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

	def update_customer(self):
		name = self.name_entry.get()
		phone = self.phone_entry.get()
		if name in self.customers:
			self.customers[name] = phone
			tkinter.messagebox.showinfo('Success', 'Customer updated successfully')
		else:
			tkinter.messagebox.showerror('Error', 'Customer not found')
		self.save_customers()

	def save_customers(self):
		try:
			output_file = open("customer_file.dat", 'wb')
			pickle.dump(self.customers, output_file)
			output_file.close()
		except (IOError, pickle.PickleError):
			tkinter.messagebox.showerror('Error', 'Could not save customer data')

	def go_back(self):
		self.update.destroy()


class UpdateGUI:
	def __init__(self, master):
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		self.update = tkinter.Toplevel(master)
		self.update.title('Update customer')

		self.top_frame = tkinter.Frame(self.update)
		self.middle_frame = tkinter.Frame(self.update)
		self.bottom_frame = tkinter.Frame(self.update)

		self.name_label = tkinter.Label(self.top_frame, text='Enter customer name to update: ')
		self.name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		self.phone_label = tkinter.Label(self.middle_frame, text='Enter new phone number: ')
		self.phone_entry = tkinter.Entry(self.middle_frame, width=15, font="TkDefaultFont")

		self.update_button = tkinter.Button(self.bottom_frame, text='Update', command=self.update_customer, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		self.name_label.pack(side='left')
		self.name_entry.pack(side='left')
		self.phone_label.pack(side='left')
		self.phone_entry.pack(side='left')
		self.update_button.pack(side='left')
		self.back_button.pack(side='left')

		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

	def update_customer(self):
		name = self.name_entry.get()
		phone = self.phone_entry.get()
		if name in self.customers:
			self.customers[name] = phone
			tkinter.messagebox.showinfo('Success', 'Customer updated successfully')
		else:
			tkinter.messagebox.showerror('Error', 'Customer not found')
		self.save_customers()

	def save_customers(self):
		try:
			output_file = open("customer_file.dat", 'wb')
			pickle.dump(self.customers, output_file)
			output_file.close()
		except (IOError, pickle.PickleError):
			tkinter.messagebox.showerror('Error', 'Could not save customer data')

	def go_back(self):
		self.update.destroy()

class DeleteGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete a customer')

        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        self.delete_label = tkinter.Label(self.top_frame, text='Enter customer name to delete: ')
        self.delete_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

        self.delete_label.pack(side='left')
        self.delete_entry.pack(side='left')

        self.delete_button = tkinter.Button(self.middle_frame, text='Delete', command=self.delete_customer, width=10)
        self.back_button = tkinter.Button(self.middle_frame, text='Main Menu', command=self.go_back, width=10)

        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        self.status_string = tkinter.StringVar()
        self.status_label = tkinter.Label(self.bottom_frame, textvariable=self.status_string)

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.status_label.pack()

    def delete_customer(self):
        name = self.delete_entry.get()
        if name in self.customers:
            del self.customers[name]
            self.status_string.set(f'{name} has been deleted.')
        else:
            self.status_string.set(f'{name} was not found.')

        try:
            output_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        except (FileNotFoundError, IOError):
            tkinter.messagebox.showerror('Error', 'Could not open file')

    def go_back(self):
        self.delete.destroy()

def main():
	# create a window and initialize the Tk library
	root = tkinter.Tk()
	# call the GUI and send it the root window
	# use _ as variable name because the variable will not be needed after instantiating GUI
	# the GUI itself will handle the remaining program logic
	_ = CrudGUI(root)
	# because the root window was initialized here, we control the mainloop from main instead of the class
	root.mainloop()


main()
