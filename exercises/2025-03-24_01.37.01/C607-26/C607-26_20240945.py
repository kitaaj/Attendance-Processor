try:
    hours= float(input("hours working:"))
except ValueError:
    print ('input again')
    exit()

# calculate the payment
if working_hours <= 40:
    payment = hours * pay_rate
else:
    payment_regular = 40 * pay_rate

    overtime = hours - 40
    payment_over = 1.5 * pay_rate * overtime

    payment = payment_regular + payment_over

# print out the result
print(f"totle payment should be: {paymenta}")
