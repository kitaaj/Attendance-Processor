n=127
m=0
while n>0:
    digit=n%10
    m=m*10+digit
    n//=10
print(m)

