# 1.get working hours and payment rate from user
hours = float(input("Please input the working hours:"))
pay_rate = float(input("Please input the payment rate:"))

# 2.calculate the payment
if hours  <= 40:
    payment = hours * pay_rate
else:
    payment_regular = 40 * pay_eate

    overtime = hours - 40
    payment_over = 1.5 * pay_rate * overtime

    payment = payment_regular + payment_over

# 3.print out the result
print(f"totle payment shold be: {payment}")
