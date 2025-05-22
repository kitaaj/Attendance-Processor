#get a number from user
num=int(input("enter a number:"))
#start from 2(first positive even number)
even=2
#use while loop to print all even numbers smaller than num
while even<num:
    print(even)
    even+=2
