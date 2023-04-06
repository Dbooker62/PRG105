student_list = []


num_students = int(input("How many students are in your class? "))


for i in range(num_students):
    
    student_name = input("Enter the name of student {}: ".format(i + 1))
    
    
    final_grade = input("Enter the final grade of student {}: ".format(i + 1))
    
    
    student_info = [student_name, final_grade]
	    
    
    student_list.append(student_info)


print("List of students and their final grades:")
for student_info in student_list:
    print("Student Name: {}, Final Grade: {}".format(student_info[0], student_info[1]))


with open("grades.txt", "w") as file:
    for student_info in student_list:
        file.write(f'"{student_info[0]}", "{student_info[1]}"\n')
        
print("Student information has been written to grades.txt file.")
