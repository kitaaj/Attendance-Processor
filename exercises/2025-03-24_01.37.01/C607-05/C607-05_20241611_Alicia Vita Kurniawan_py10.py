def compute_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (ra
        regular_pay = 40 * rate
        total_pay = regular_pay + overtime_pay + overtime_hours
    else:
     total_pay = hours * rate
    return total_pay

# input from user
hours = float (input("Enter Hours: "))
rate = float 
