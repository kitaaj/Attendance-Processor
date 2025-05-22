file_path ="your_file.txt" # Replace with your actual file path

# open the file , count lines
with open(file_path, 'r')as f:
    lines + f.readlines()

print("Line Count:",len(lines))
# Add your ID and name at the end
with open(file_path,'a')as f:
    f. write("\n123456_JohnDoe") # Replace with your actual ID and name
