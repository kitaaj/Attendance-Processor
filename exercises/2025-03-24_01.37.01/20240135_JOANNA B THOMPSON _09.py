percentage=float(input("Enter percentage; "))
if percentage>=90:
    grade = "A"
elif percentage >= 75:
     grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
     grade = "D"
else:
    grade = "F"
print("Grade:", grade)
