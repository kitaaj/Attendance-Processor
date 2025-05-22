file_path = "C:/users/WendyLicussa/Desktop/example.txt"
your_id = 20241314
your_name = "Wendy Angelina"
with open(file_path, 'r') as file:
    lines = file.readliness()
    line_count = len(lines)

new_line = f"{your_id} - {your_name}/n"
with open(file_path, 'a')as file:
    file.write(new_line)
print(f"Number of lines in the file: {line_count}")    
