# class student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
    
#     def display_info(self):
#         print(f"Roll no: {self.roll_number} | Name: {self.name}")
        
        
# class student_management_system:
#     def __init__(self):
#         self.students =[]
    
#     def add_student(self, student):
#         self.students.append(student)
#         print(f"'{student.name}' added.")
        
#     def remove_student(self, roll_number):
#         for student in self.students:
#             if student.roll_number == roll_number:
#                 self.students.remove(student)
#                 print(f"'{student.name}' remove.")
#                 return
#         print("Student not found")

# #student example
# system = student_management_system()

# s1 = student("Divya rai", 1)
# s2 = student("Krimon Gurung", 3)

# system.add_student(s1)
# system.add_student(s2)

# for s in system.students:
#     s.display_info()
    
# system.remove_student(1)

# print("After removal")
# for s in system.students:
#     s.display_info()


class people:
    def __init__(self, name, CID, age):
        self.name = name
        self.CID = CID
        self.age = age
        
class license:
    def __init__(self, category, phone_number, DateOfBirth, Blood_group, Gender):
        self.category = category
        self.phone_number = phone_number
        self.DateOfBirth = DateOfBirth
        self.Blood_group = Blood_group
        self.Gender = Gender
        
class lms:
    def __init__(self):
        self.management = {}
    
    def add_person(self, person_obj, license_obj):
        self.management[person_obj.CID] = {
            "person": person_obj,
            "license_obj": license_obj
        }
p1 = people("Krimon Gurung", "C182", 21)
l1 = license("K", "9820378634", "2062-4-28", "O+", "Male")
system = lms()

system.add_person(p1, l1)
print(system.management["C182"]["person"].name)  
print(system.management["C182"]["license_obj"].category)
     
  