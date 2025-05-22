file_path = "C:\User=\Administrator\Downloads\20241118_NALEDI_TSHABALA_14py
your_id = "20241118"
your_name = " naledi tshabalala"


with open(file_path, 'r') as f:
    line= f.readlines()
    print("number of lines: (len(lines)}")
    f. write(f"{your_id} {your_name}\n")
    print("Added your id and name to the file")

    
