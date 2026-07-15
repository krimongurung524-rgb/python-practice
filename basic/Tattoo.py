# class dog:
#    species = "Canis Familaries" 
   
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
       
# d1 = dog("Rex", "12")
# d2 = dog("Divya", "21")
# print(d1.name, d2.name)
# print(d1.species, d2.species)

class tatoo:  
    def __init__(self, design, size, price):
        self.design = design
        self.size = size
        self.price = price
        
    def describe(self):
        return f"{self.design} ko price chei Rs {self.price} ho"

krimon = tatoo("Japanese sleeve", "full hand", "20k")
divya = tatoo("Worldcup", "Half sleeve", "20k")
print(krimon.describe())
print(divya.describe())

# Child class inheritance using super 
class colour_tatoo(tatoo):
    def __init__(self, design, size, price, colours):
       super().__init__(design, size, price)
       self.colours = colours
       
    def extra_cost(self):
        return len(self.colours) * 500
       
monika = colour_tatoo("Butterfly","Small", "5 thousand", ["Red", "Green"])
print(monika.describe())