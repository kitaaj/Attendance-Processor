my_name = "Raymond"
user_name = input("Guess the name: ")
if len(user_name) != len(my_name):
    print("Not the same length, so not the same name.")
else:
        match = True
        for i in range(len(my_name)):
            if my_name[i] != user_name[i]:
                print(f"Letter {i+1} is different: {user_name[i]} vs {my_name[i]}")
                match = False
            else:
                    print(f"Letter {i+1} matches: {user_name[i]}")
                    if match:
                            print("Congratulations! You guessed the name correctly.")
                    else:
                            print("Nice try, but its not the same name.")
                    
