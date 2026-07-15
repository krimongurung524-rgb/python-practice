dis = {}
name = input("Enter your name :")
age = int(input("Enter your age :"))
bp = int(input("Enter your blood pressure :"))

dis["Name"] = name
dis["Age"] = age
dis["Bp"] = bp

if dis["Age"] >= 18:
    print(dis["Name"], "is eligible you are adult")
else:
    print(dis["Name"], "is not eligible because you are a minor")
if dis["Bp"] > 120:
    print("High bp consult a doc")
elif dis["Bp"] < 90:
    print("Low bp consult a doc")
else:
    print("Normal bp")