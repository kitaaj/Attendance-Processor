try:
    Number= float(input("please input a number:"))
except:
    print ("Invalid input, has to be numeric input")
    exit()
current=1
while current <Number:
    print (current)
    current+=1


num = int(input("input a number:"))
i = 1
while i <num:
    i +=1
    if i % 2:
        continue
    print(i)
