try:
    working_hours = float(input("Please input your working hours:"))
    rate = float (input("Please input the rate:")) 
except ValueError:
    print ("Input is invalid, it has to be numeric input")
    exit()

if working_hours <= 40:
    payment = working_hours * rate
else:
    payment_regular = 40 * rate

    overtime = working_hours - 40
    payment_over = 1.5 * rate * overtime

    payment = payment_regular + payment_over
  

print (f"totle payment should be: {payment}") 


 
