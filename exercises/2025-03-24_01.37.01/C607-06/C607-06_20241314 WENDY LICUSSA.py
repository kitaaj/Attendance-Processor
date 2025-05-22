def convert_to_grade(SCORE):
    if 90 <= X <= 100:
        return "A"
    elif 80 <= X < 90:
        return "B"
    elif 70 <= X < 80:
        return "C"
    elif 60 <= X < 70
     return "D"
    elif 0 <= X < 60:
        return "F"
    else:
        return "Invalid score"
    # Test the function
    X=85
    grade= convert_to_grade (X)
    print (f" score: (X), grade: (grade)")
