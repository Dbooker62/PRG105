"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
print("Name: ", name)
print("Characters in name: ")
for char in name:
    print(char)
# 2) Use the index value to access and print the capital s in Schmidt from the variable name
index = name.index("Schmidt")
print("Capital 'S' in 'Schmidt': ",name[index])
# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
last_name = name[-7:]
print("Last Name: ", last_name)

# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
# 2) Print middle
middle =name[5:10]
print("Middle: ", middle)

# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result
print("Is 'Jacob' in name? ", "Jacob" in name)
# 2) Test to see if the string "Michael" is in name, print the result
print("Is 'Michael' in name? ", "Michael" in name)
# 3) Test to see if name contains only digits, print the result
#    Hint: Use the built-in string testing methods
print("Does name contain only digits? ", name.isdigit())
# 4) Test to see if name is lowercase, print the result
print("Is name lowercase? ", name.islower())
# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print
name_with_replacement = name.replace("J", "j")
print("Name with 'J' replaced by 'j': ", name_with_replacement)
# 6) Split the string name into the variable name_list below (replace the ""), print the result
name_list = name.split()
print("Name list: ", name_list)
