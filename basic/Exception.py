try:
    result = 10/0
    
except:
    print("Error! Zero can't be divided")
    print("Program is running")
    
# Question 2
try:
    num = int(input("Enter the number: "))
    result = 10/num
    print(result)
    
except ZeroDivisionError:
    print("Zero can't be divided")
    
except ValueError:
    print("Enter the number! not text")
    
# Question 3
try:
    result = 10/0

except ZeroDivisionError as e:
    print("Error :" , e)
    
# Question 4
try:
    result = 10/0
except ZeroDivisionError:
    print("Error")
    
else:
    print("Everything good, result: ", result)