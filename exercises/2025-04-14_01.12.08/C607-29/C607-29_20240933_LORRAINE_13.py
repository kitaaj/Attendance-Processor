correct_name="Raymond"
user_name= input(" guess my name:")

if user_name.lower() == correct_name.lower():
    print("correct!")
else:
       print("wrong! the correct name is", correct_name)
