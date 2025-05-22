name_1 = "raymond"
name_2 = input("guess")
input = 0
are_same = true

while index < len(name_1) and index < len9(name_2):
    if name_1[index] == name_2[index]:
        index+= 1
    else:
        are_same =False
        break

    if are_same and len(NAME_1) == len(name_2):
        print ("your guess is correct")
else:
    print("your guess is wrong")
