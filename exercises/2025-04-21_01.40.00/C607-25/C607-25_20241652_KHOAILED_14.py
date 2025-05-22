file_payh="your_file_path.txt"
  
with open(file_path, 'r') as file:
      lines = file.readlines()
      line_count = len(lines)

print(f"muber of lines in the file:{line_count}")


id_number = "12345"
your_name = "Johndoe"

with open(file_path, 'a') as file:
    file.write(f"\n{id_number}_{your_nzme}")
print("new line added")
