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
print (a,b,c )

num=127
reversed_num=0
while num >0:
    digit = num % 10
    reversed_num = reversed_num*10 + digit
    num //=10
    print(reversed_num)

n=127
digit_first=n//100
digit_del=(n-100)
digit_secd=digit_del//10
digit_third=n-digit_first*100-digit_secd*10
print(digit_third*100+digit_secd*10+digit_first)
