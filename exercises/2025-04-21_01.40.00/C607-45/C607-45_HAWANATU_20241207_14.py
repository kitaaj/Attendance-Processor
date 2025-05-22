#Define the file path
file_path ='path/to/your/file.txt'  # Replace with your actual file path
search_string = 'content' # The string you want to search for
new_line = 'this is a new line of text.' # the new line you want to add



# count lines containing the search string

lines = file.readlines()

  count = sum(1 for line in line if search_string in line)
print(f'Number of lines containing "{search_string}":{count})


# write a new line to the file
 with open(file_path,'a')as file:
      file.write(new_line +'\n')
    
