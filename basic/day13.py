class person:
    def __init__(self, height, weight, face_shape):
        self.height = height
        self.weight = weight
        self.face_shape = face_shape
        
    def player(self, skills, rank, stamina):
        self.skills = skills
        self.rank = rank
        self.stamina = stamina



person1 = person("5.7 ft", "69 kg", "Oval")
person2 = person("6.2 ft", "82 kg", "Round")

person1.player("95", "1ST", "Average")
person2.player("80","2nd", "Low")
print(person1.height, person1.weight, person1.face_shape, person1.skills, person1.rank, person1.stamina)
print(person2.height, person2.weight, person2.face_shape, person2.skills, person2.rank, person2.stamina)




        
