try:
    hours= float(input("working hours:"))
    rate= float(input("enter rate:"))
except ValueError:
    print('input again')
    exit()

if working_hours<=40:
   payment = hours * rate
else:
    payment_reguler = 40 * rate

    overtime = hours - 40
    payment_over = 1.5 * pay_rate * overtime
    payment = 
