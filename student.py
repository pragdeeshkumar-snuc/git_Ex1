d={"1": {"Name": "Arun", "Age": 13, "Gender": "male"}}

def dis_students():
	for i in d.keys():
		print("\nStudent Details: ")
		print(f"Roll no.: {i}")
		for k,v in d[i].items():
			print(f"{k}: {v}")
	if d=={}:
		print("No student details found")
		
	print(d)

dis_students()

def add_stud():
	n = input("\nEnter the name of the student: ")
	r = input("Enter the roll no. of the student: ")
	a = int(input("Enter the age of the student: "))
	g= input("Enter the gender of the student: ")
	
	err = False
	
	if n == "":
		print("Invalid student name")
		return False
		err = True
	if a == None or a == 0:
		print("Invalid student age")
		return False
		err = True
	if r == "":
		print("Invalid student roll no.")
		return False
		err = True
	if g == "":
		print("Invalid student gender")
		return False
		err = True
	
	if err == False:
		d.update({ r: {"Name" : n, "Age": a, "Gender": g}})
	else:
		print("Invalid student details")
	
	dis_students()
	
def search_stud():
	user_in = input("Enter the students name: ")
	
	print("\nStudents Details: ")
	for i in d.keys():
		if user_in == d[i]["Name"]:
			print(f"Roll no.: {i}")
			for k,v in d[i].items():
				print(f"{k}: {v}")
	else:
		print("Student not found")
		
		
def del_stud():
	user_in = input("Enter the roll no. of the student: ")
	
	if user_in in d.keys():
		d.pop(user_in)
	else:
		print("Student not found")
		
def val_stud():
	user_in = input("Enter the roll no. of the student to validate: ")
	
	for k,v in d[user_in].items():
		err = False
		if d[user_in]["Name"] == "":
			print("Invalid student name")
			return False
			err = True
		if d[user_in]["Age"] == None or d[user_in]["Age"] == 0:
			print("Invalid student age")
			return False
			err = True
		if d[user_in] == "":
			print("Invalid student roll no.")
			return False
			err = True
		if d[user_in]["Gender"] == "":
			print("Invalid student gender")
			return False
			err = True
	if err == False:
		print("Student details are correct")
				
				

			
	
