hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate:"))

regular_hors = 0
overtime_hours= 0
pay = 0

if hours > 40:
    regular_hours = 40
    overtime_hours = hours - 40
    pay = (regular_hours * rate)+(overtime_hours * rate * 1.5)

else:
    regular_hours = hours
    pay = regular_hours * rate

print("pay:", pay)
 

if overtime_hours >0:
     print(f"{pay} = {regular_hours}* {rate} + {overtime_hours} * {rate * 1.5}")
