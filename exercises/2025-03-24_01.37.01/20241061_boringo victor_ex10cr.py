def compute_pay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

# input hour and rate from the user
hours = float(input("enter hours:"))
rate = float(input("enter rate:"))

# calculate the pay
pay = compute_pay(hours, rate)

# print the result
print (f"pay: {pay}")
