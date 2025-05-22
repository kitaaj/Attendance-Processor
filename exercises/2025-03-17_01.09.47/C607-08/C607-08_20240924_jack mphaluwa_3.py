a=5
b=11
c=20
a=a=b
b=b-c
c=a*b
print (a,b,c)

a=5
b=11
c=20
a,b,c= a+b, b-c, a*b
print(a,b,c)



num=127
reversed_num=int(str(num)[::-1])
print(reversed_num)


n=127
m=0
while n>0:
    digit=n%10
    m=m*10+digit
    n//=10
print(m)


digit_first=n%100
digit_secd=n%10
digit_third=n-digit_first*100-digit_secd*10
print=digit_third*100+digit_secd*10+digit_first






digit_first=n%100
digit_secd=n%10
digit_third=n-digit_first*100-digit_secd*10
print=digit_third*100+digit_secd*10+digit_first



value=123
val_1=value//100
print(val_1)
val_n=(value-100)
val_2=val_n//10
print(val_2)
val_3=value-val_1*100-val_2*10
print(val_3*100+val_2*10+val_1)
