class PersonalData:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number


my_data = PersonalData("Your Name", "Your Address", 30, "Your Phone Number")
friend1_data = PersonalData("Friend 1 Name", "Friend 1 Address", 25, "Friend 1 Phone Number")
friend2_data = PersonalData("Friend 2 Name", "Friend 2 Address", 28, "Friend 2 Phone Number")

my_data = PersonalData("Your Name", "Your Address", 30, "Your Phone Number")

friend1_data = PersonalData("Friend 1 Name", "Friend 1 Address", 25, "Friend 1 Phone Number")
friend2_data = PersonalData("Friend 2 Name", "Friend 2 Address", 28, "Friend 2 Phone Number")

print("My Personal Data:")
print("Name:", my_data.get_name())
print("Address:", my_data.get_address())
print("Age:", my_data.get_age())
print("Phone Number:", my_data.get_phone_number())

print("\nFriend 1 Personal Data:")
print("Name:", friend1_data.get_name())
print("Address:", friend1_data.get_address())
print("Age:", friend1_data.get_age())
print("Phone Number:", friend1_data.get_phone_number())

print("\nFriend 2 Personal Data:")
print("Name:", friend2_data.get_name())
print("Address:", friend2_data.get_address())
print("Age:", friend2_data.get_age())
print("Phone Number:", friend2_data.get_phone_number())
