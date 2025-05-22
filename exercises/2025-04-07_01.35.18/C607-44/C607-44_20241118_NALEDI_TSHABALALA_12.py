try:
    Number= float(input("Please input a number:"))
except:
    print ("Invalid input, has to be numeric input")
    exit()

current=1
while current <Number:
    print (current)
    current+=1

num = int(input(" enter 5 number:"))
i = num - 1
while i > 0:
    print (i)
    i-=1
num = int(input("enter a number:"))
i = 2
while i < num:
    print (i)
    i +=2

num = int(input("input a number:"))
i = 1
while i < num:
    i =+1
    if i % 2:

        continue
    print(i)


    
