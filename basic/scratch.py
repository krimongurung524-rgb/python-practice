# List
fruits = ["Apple", "Banana", "Mango"]
# (append) method le last ma items thapne kam garcha
fruits.append("Grapes") 

# (insert) le chei hamilai man lageko thau ma items add garna sakchum
fruits.insert(2, "Kiwi")

# (extend) le chei dherai items haru ekaichoti add garna milcha
fruits.extend(["Pineapple","Dragon fruit", "Litchi"])

# (remove) le chei hamilai man lageko item remove garna sakchum
fruits.remove("Mango")

# (pop) le chei indexing bata jun items hatauna man lagcha tesle hataidincha yedi empty rakhe ma end ko item hataidincha
fruits.pop(1)
fruits.pop()

# (del) le chei index or purai list lai hataune kam garcha
del fruits [1]

# clear
fruits.clear
print(fruits)


# (sort) le chei ascending milaune kam garcha 
# reverse le chei ulto bata print garne kam garcha

numbers = [5,3,4,2,8,9,6]
numbers.sort()
numbers.sort(reverse = True)
print(numbers)
print(len(numbers))


# coditional 

temperature = 1

if temperature > 40:
    print("The temperature is too hot")
    
elif temperature >= 40:
    print("The temperature is mild")
    
elif temperature >= 20:
    print(" Dherai sittal cha")
    
else:
    print("Too cold")
