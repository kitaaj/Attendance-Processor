#1.get a percentage value first
perc_grd = float(input("Please input a number:"))

#2.convert the percentage value into grade
grade ="F" # default grade
if perc_grd >=90:
    grade = "A"
if perc_grd >=80:
    grade = "B"
if perc_grd >=70:
    grade = "C"
 if perc_grd >=60:
     grade = "D"

#3.Print out the result
print(grade)     
