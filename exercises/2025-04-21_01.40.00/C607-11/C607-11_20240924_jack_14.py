file_path="your_file.txt"
with open(file_path,'r') as f:
    lines = f. readlines()
    print("line count:",len(lines))
    with open(file_path,"a") as f:
        f.write("\n20240924_jack")
