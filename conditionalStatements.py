# if else, switch

student_list = ['harish','vamshi','roopa','preetam','kirtan']

student = input("Enter the student name:\t")

student = student.lower()

if student in student_list:
	print("Yes ",student.title(), " belongs to our class")

else:
	print("No ",student.title(), " does not belong to our class")
