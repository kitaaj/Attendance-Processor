#DEFINE THE FILE PATH
file_path = 'path to your file.txt'
search_string = ' content '
new_line = 'this is a new line of text' 



file_path ="C:\Users\Administrator\Downloads\20241091_CADET_LINCEY.txt"
your_id = "20241091"
your_name = "CADET LINCEY"

with open (file_pth, 'r') as f:
    lines = f.readlines()
    print("number of lines: (len(lines))")
    f.write(f"{your_id} {your_name}\n")
    print("added your id and name to the file")
