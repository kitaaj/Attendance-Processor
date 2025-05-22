try:
    #step 1: read the file and count lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = line(lines)
        print(f"number of lines in the file: {lines_count}")
        
