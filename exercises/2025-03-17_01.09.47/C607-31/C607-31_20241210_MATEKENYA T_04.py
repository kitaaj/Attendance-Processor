a=5
b=11
c=20
a,b,c=a+b,b-c,a*b
print (a,b,c)

a=5
b=11
c=20
a=a+b
b=b-c
c=a*b
print (a,b,c)

num=127
reversed_num=0
while num >0:
    digit = num % 10
    reversed_num = reversed_num*10 + digit
    num //= 10
print (reversed_num)

n=input('280')
digit_first=n % 100

 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python36/20241210_MATEKENYA T_04.py 
16 -9 55
16 -9 -144
721
>>> 
