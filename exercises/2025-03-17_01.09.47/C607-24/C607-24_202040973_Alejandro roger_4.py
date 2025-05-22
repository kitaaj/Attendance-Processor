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

