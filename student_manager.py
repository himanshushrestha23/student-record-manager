# ===== Student Record Manager =====

# 1. Add Student
# 2. Search Student
# 3. Update Marks
# 4. Delete Student
# 5. Show All Students
# 6. Exit

# Choose an option:

def add_student():
    student_name=input("Enter student name: ")
    if student_name in students: # way to access key from a dictionary i.e. (if key in dictionary)
         print("Student already exists")
    else:
        student_marks=int(input("Enter student marks: "))
        students[student_name]=student_marks
        print("Student added successfully!")

def search_student():
     search=input("Enter student name: ")
     if search in students:
          print(f"{search}'s marks: {students[search]}")
     else:
          print("Student not found.")


def update_student():
    student_name=input("Enter student name: ")
    if student_name in students: 
         updated_marks=input("Enter new marks: ")
         students[student_name]=updated_marks
         print("Updated Successfully!")
    else:
        print("Student doesn't exist")     


def delete_students():
    student_name=input("Enter student name: ")
    if student_name in students: 
        students.pop(student_name)
        print("Deleted Successfully!")
    else:
        print("Student doesn't exist")   


def show_students():
    print("Students: ")
    for student in students:
          print(f"{student}: {students[student]}")
      



user_input=""
students={}
while user_input!="6":
  print("""===== Student Record Manager =====
          1. Add Student
          2. Search Student
          3. Update Marks
          4. Delete Student
          5. Show All Students
          6. Exit""")
  user_input=input("Choose an option: ")

  if user_input=="1":
      add_student()
     

  elif user_input=="2":
      search_student()
     

  elif user_input ==  "3":
      update_student()
   
  elif user_input =="4":
      delete_students()

  elif user_input=="5":
     show_students()
          

        
  elif user_input=="6":
       break
  else:
       print("Invalid option")



  


  


