# try:
#     result = 10/0
    
# except:
#     print("Error! Zero can't be divided")
#     print("Program is running")
    

try:
    num = int(input("Enter the number: "))
    result = 10/num
    print(result)
    
except ZeroDivisionError:
    print("Zero can't be divided")
    
except ValueError:
    print("Enter the number! not text")