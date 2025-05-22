file_path = "your_file.txt"

#Open the file, count lines
with open(file_path,'r'r) as f:
    lines = f.readlines()

print("Line count:",len(lines))
# Add your Id and name at the end
with open(file_path,"a") as f:
    f.write("\n123456_Johndoe")
