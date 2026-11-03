import student

user_inp = ""
while user_inp!="exit":
	if user_inp!="exit":
		print("\n1 for Add student: ")
		print("2 for Display students: ")
		print("3 for Search student")
		user_inp = input("\nEnter the choice of function to do: ")
		if user_inp!="exit":
			if int(user_inp) == 1:
				student.add_stud()
			elif int(user_inp) == 2:
				student.dis_students()
			elif int(user_inp) == 3:
				student.search_stud()
			else:
				print("Invalid choice")
