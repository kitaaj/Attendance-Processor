# Replace your actual file path
file_path = "C:/users/youruersname/documents/examle.txt"
# Replace with your actual ID number and name
id_number = 20241740
name = "Joy Kamrul Hasan"
# Read the filr and count the number of lines
with open(file_path,'r') as file:
    lines = file.readlines()
    lines_count = len(lines)

print(f"number of lines in the file: {line count}")

# Append the ID and name at the end
with open(file_path, 'a') as file:
    file.write(f"\n{ID_number}_{name}")
