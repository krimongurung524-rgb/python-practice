class student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade
        self.sports ={}
        
    def info(self):
        print(f"{self.name} - Roll: {self.roll_no} - Grade: {self.grade}")
        
class faculty:
    def __init__(self):
        self.commerce = []
        self.science = []
        self.arts = []
        self.hotel_management = []
        
class sports:
    def __init__(self):
        self.voilet = []
        self.yellow = []
        self.blue = []
        self.green = []

student1 = student("Krimon Gurung", "20", "21", "A")
student2 = student("Divya Rai", "12", "20", "B")
student3 = student("Diwash Adhikari", "11", "21", "C")
student4 = student("Peshal Karki", "26", "21", "C")

fac = faculty()
fac.commerce.append(student1)
fac.science.append(student2)
fac.arts.append(student3)
fac.hotel_management.append(student4)

print("Commerce:", [s.name for s in fac.commerce])
print("Science:", [s.name for s in fac.science])
print("Arts:", [s.name for s in fac.arts])
print("Hotel Management:", [s.name for s in fac.hotel_management])

category = sports()
category.voilet.append(student1)
category.yellow.append(student2)
category.blue.append(student3)
category.green.append(student4) 

