hours=float(input("Please input the working hours:")
pay_rate =float(input("please input the payment rate:"))
if hours<=40:
    payment_hours*pay_rate
else:
    payment_regular=40*pay_rate
    overtime=hours-40
    payment_over=1.5*pay_rate* overtime
    payment=payment_regular+ payment_over
print(f"total payment should be:(payment)")
