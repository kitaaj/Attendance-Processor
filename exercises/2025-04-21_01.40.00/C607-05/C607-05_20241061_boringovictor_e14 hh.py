file_path ="C:\Users\Administrator\Downloads\20241061_boringo victor.txt"
your_id = "20241061"
your_name = "victor boringo"

with open(file_path, 'r') as f:
    lines= f.readlines()
    print("number of lines: {len(lines)}")
    f.write(f"{your_id}{your_name}\n")
    print("Added your id and name to the file")
