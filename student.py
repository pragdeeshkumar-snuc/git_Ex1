d={"1": {"Name": "Arun", "Age": 13, "Gender": "male"}}

def dis_students():
	for i in d.keys():
		print("\nStudent Details: ")
		print(f"Roll no.: {i}")
		for k,v in d[i].items():
			print(f"{k}: {v}")

dis_students()

def add_stud():
	n = input("\nEnter the name of the student: ")
	r = int(input("Enter the roll no. of the student: "))
	a = int(input("Enter the age of the student: "))
	g= input("Enter the gender of the student: ")
	
	d.update({ r: {"Name" : n, "Age": a, "Gender": g}})
	
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
				
				

			
	
