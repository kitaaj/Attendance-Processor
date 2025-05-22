file_path = "20241611_Alicia_Vita_Kurniawan_14.txt"

#open the file , count lines
with open(file_path, 'r') as f:
    lines + f.readlines()

print("Line Count:",len(lines))
# Add your Id and Name at the end
with open (file_path, 'a') as f:
    f.write("\n120241611_AliciaVitaKurniawan")
