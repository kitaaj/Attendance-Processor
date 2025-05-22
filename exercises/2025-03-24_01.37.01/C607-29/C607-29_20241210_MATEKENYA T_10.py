try:
    hour=float(input("hour work"))
except ValueError:
    print ('input again')
    exit()

hours = float(input("Enter Hours:"))
rate = float (input("Enter Rate:"))
if hours<=40:
    pay = hours*rate
else
    overtime_hours = hours - 40
    pay =(40*rate) + (overtime_hours * rate * 1.5)

print(f"pay:{pay}")
