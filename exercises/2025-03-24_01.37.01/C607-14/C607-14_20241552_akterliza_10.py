# get working hours and payment rate from user
hours = float(input("please input the working hours:"))
pay_rate = float(input("please input the payment rate:"))

# calculate the payment
if hours <= 40:
    payment = hours * pay_rate
else:
    payment_regular = 40 * pay_rate

    overtime = hourse - 40
    payment_over = 1.5 * pay_rate * overtime

    payment = payment_regular + payment_over

# print out the result
print(f"total payment should be: {payment}")
