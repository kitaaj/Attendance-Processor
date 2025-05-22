def compute_pay(hours, pay_rate):
    if hours <= 40:
        total_pay = hours * pay_rate
    else:
        payment_regular = 40 * pay_rate
        
        overtime_hourss = hours - 40
        payment_over = 1.5 * pay_rate * overtime

        payment = payment_regular + payment_over

# print out the result
print(f"totle payment should be: {payment}")
