def modify_file(C:\Users\Administrator\Downloads,20241095,ShahSayedRohullah):
    try:
        with open(C:\Users\Administrator\Downloads, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            with open(C:\Users\Administrator\Downloads, 'a') as file:
                file.write(f"\n{20241095} - {ShahSayedRohullah}")
                print(f"Total lines in the file: {num_lines}")
                print("New line added successfully.")
                
             except FileNotFoundError:
                 print("error: the file was not found.")
             except Exception as e:
                 print(f"An error ocurred: {e}")
                 

process_file("C:\Users\Administrator\Downloads", "20241095","ShahSayedRohullah")              
