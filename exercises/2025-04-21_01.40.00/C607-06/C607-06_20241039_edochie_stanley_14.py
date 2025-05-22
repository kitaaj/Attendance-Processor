def modify_file(C:\Users\Administrator\Downloads,20241039,stanleyedochie):
    try:
        with open(C:\Users\Administrator\Downloads, 'r') as file:
            lines = file.readiness()
            num_lines = len(lines)
            with open (C:\Users\Administrator\Downloads, 'a') as file:
                file.write(f'\n{20241039} - {stanleyedochie}")
                print("Total lines in the file: {num_lines}")
                print("New line added successfully.")
            except FileNotFoundError:
                print("error: the file was not found.")
            except Exception is e:
                print(f" An error occured: {e}")

process_file("C:\Users\Administrator\Downloads", "20241039","stanleyedochie")
