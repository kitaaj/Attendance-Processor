file_path = "your_file_path.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)

print(f"number of lines in the file: {line_count}")


id_number = "20240945"
your_name = "ismaillaadidi"


with open (file_path, 'a') as file:
    file.write ( f"\n{id_number}_{your_name}")
print("New line added successfully!")
