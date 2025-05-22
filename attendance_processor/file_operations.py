import os
from typing import List, Dict, Tuple
from .reporting import Reporter

def load_student_data(filepath: str, reporter: Reporter) -> Tuple[List[Dict], int]:
    """
    Loads student data from the namelist file.
    Each student is represented as a dictionary.
    Determines the number of actual mark columns from the file,
    correctly handling files previously updated with Total and Rate columns.
    If Total and Rate are present, they are loaded.

    Args:
        filepath (str): Path to the namelist.txt file.
        reporter (Reporter): Reporter instance for logging.

    Returns:
        Tuple[List[Dict], int]: A list of student data dictionaries and
                                the number of actual assignment mark columns found.
                                Returns an empty list and 0 if errors occur.
    """
    students = []
    num_assignment_mark_columns_expected = -1 

    if not os.path.exists(filepath):
        reporter.error(f"Namelist file not found: {filepath}")
        return [], 0

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            reporter.warning(f"Namelist file '{filepath}' is empty.")
            return [], 0

        first_valid_line_processed = False
        for i, line_content in enumerate(lines):
            line_content = line_content.strip()
            if not line_content: continue

            parts = line_content.split('\t')

            if len(parts) < 2:
                reporter.warning(f"Skipping malformed line {i+1} in '{filepath}': Not enough parts for ID and Name. Content: '{line_content}'")
                continue

            student_id = parts[0]
            name = parts[1]
            
            current_line_assignment_mark_strings = []
            current_line_num_assignment_marks = 0
            loaded_total = 0 # Default if not found or not in updated format
            loaded_rate = 0.0 # Default

            is_updated_format = False
            # Check if the line format includes Total and Rate (previously updated file)
            # Format: ID, Name, [AssignmentMarks...], Total, Rate. Minimum 4 parts.
            if len(parts) >= 4:
                try:
                    # Attempt to parse last two parts as Total (int) and Rate (float)
                    float(parts[-1])  # Potential Rate
                    int(parts[-2])    # Potential Total
                    is_updated_format = True
                except ValueError:
                    is_updated_format = False # Does not match Total/Rate format

            if is_updated_format:
                # Format: ID, Name, [AssignmentMarks...], Total, Rate
                current_line_assignment_mark_strings = parts[2:-2]
                current_line_num_assignment_marks = len(current_line_assignment_mark_strings)
                try:
                    loaded_total = int(parts[-2])
                    loaded_rate = float(parts[-1])
                except ValueError: # Should be rare due to prior check but as safeguard
                    reporter.warning(f"Line {i+1} in '{filepath}': Error parsing pre-existing Total/Rate despite format detection. Using defaults. Content: '{line_content}'")
                    is_updated_format = False # Treat as original format if parsing Total/Rate fails
                    current_line_assignment_mark_strings = parts[2:] # Re-evaluate assignment marks
                    current_line_num_assignment_marks = len(current_line_assignment_mark_strings)
                    loaded_total = 0
                    loaded_rate = 0.0
            else:
                # Original format: ID, Name, [AssignmentMarks...] or just ID, Name
                current_line_assignment_mark_strings = parts[2:]
                current_line_num_assignment_marks = len(current_line_assignment_mark_strings)
            
            if not first_valid_line_processed:
                num_assignment_mark_columns_expected = current_line_num_assignment_marks
                reporter.info(f"Namelist structure: Expecting {num_assignment_mark_columns_expected} assignment mark column(s).")
                if is_updated_format and num_assignment_mark_columns_expected >= 0:
                    reporter.info("Detected 'Total' and 'Rate' columns; these values will be loaded.")
                first_valid_line_processed = True
            elif current_line_num_assignment_marks != num_assignment_mark_columns_expected:
                reporter.warning(
                    f"Skipping line {i+1} in '{filepath}': Inconsistent number of assignment mark columns. "
                    f"Expected {num_assignment_mark_columns_expected}, found {current_line_num_assignment_marks}. Content: '{line_content}'"
                )
                continue
            
            try:
                # Parse only the actual assignment mark strings
                assignment_marks = [int(m_str) for m_str in current_line_assignment_mark_strings]
            except ValueError:
                reporter.warning(f"Skipping malformed line {i+1} in '{filepath}' due to non-integer value in assignment mark columns. Content: '{line_content}'")
                continue
            
            final_assignment_marks = assignment_marks[:num_assignment_mark_columns_expected] + \
                                     [0] * (num_assignment_mark_columns_expected - len(assignment_marks))

            students.append({
                "id": student_id,
                "name": name,
                "marks": final_assignment_marks,
                "total": loaded_total, # Store loaded total
                "rate": loaded_rate    # Store loaded rate
            })

        if not first_valid_line_processed and lines:
            reporter.error(f"Could not determine a consistent assignment mark column structure from '{filepath}'. All lines may be malformed.")
            return [], 0
        
        if not students and first_valid_line_processed:
             reporter.warning(f"No valid student data loaded from '{filepath}' after initial structure detection.")
        elif not students:
            reporter.warning(f"No student data could be loaded from '{filepath}'.")

    except Exception as e:
        reporter.error(f"An unexpected error occurred while reading or parsing namelist file '{filepath}': {e}")
        return [], 0
    
    return students, num_assignment_mark_columns_expected if num_assignment_mark_columns_expected != -1 else 0

def discover_assignment_folders(root_dir: str, reporter: Reporter) -> List[str]:
    """
    Discovers assignment subfolders in the root directory.
    Folders are sorted alphabetically to ensure consistent processing order.

    Args:
        root_dir (str): The root directory containing assignment subfolders.
        reporter (Reporter): Reporter instance for logging.

    Returns:
        List[str]: A sorted list of assignment folder names.
    """
    if not os.path.isdir(root_dir):
        reporter.error(f"Submissions root directory not found or is not a directory: {root_dir}")
        return []
    try:
        folders = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
        folders.sort() # Ensure consistent order
        if not folders:
            reporter.warning(f"No subfolders found in submissions directory: {root_dir}")
        return folders
    except Exception as e:
        reporter.error(f"Error accessing submissions directory '{root_dir}': {e}")
        return []

def get_submission_files_in_folder(assignment_folder_path: str, file_extension: str, reporter: Reporter) -> List[str]:
    """
    Gets all files with the specified extension from an assignment folder,
    searching recursively through its subdirectories.

    Args:
        assignment_folder_path (str): Path to the specific assignment folder
                                     (e.g., './exercises/2025-03-03_01.04.57').
        file_extension (str): The file extension to look for (e.g., '.py').
        reporter (Reporter): Reporter instance for logging.

    Returns:
        List[str]: A list of full file paths for submission files found within
                   this assignment folder and its subdirectories.
    """
    submission_files = []
    if not os.path.isdir(assignment_folder_path):
        reporter.warning(f"Assignment folder path is not a valid directory: {assignment_folder_path}")
        return submission_files

    reporter.info(f"Searching for '{file_extension}' files in and under '{assignment_folder_path}'...")
    try:
        for dirpath, dirnames, filenames in os.walk(assignment_folder_path):
            # dirpath is the current directory being walked
            # dirnames is a list of subdirectories in dirpath
            # filenames is a list of files in dirpath
            for filename in filenames:
                if filename.endswith(file_extension):
                    full_file_path = os.path.join(dirpath, filename)
                    submission_files.append(full_file_path)
                    # reporter.info(f"  Found: {full_file_path}") # Can be too verbose, remove if not needed for detailed logs
        
        if not submission_files:
            reporter.info(f"  No '{file_extension}' files found in or under '{assignment_folder_path}'.")
        else:
            reporter.info(f"  Found {len(submission_files)} '{file_extension}' file(s) in/under '{assignment_folder_path}'.")

    except Exception as e:
        reporter.error(f"Error walking through directory '{assignment_folder_path}': {e}")
    
    return submission_files

def save_student_data(filepath: str, students: List[Dict], reporter: Reporter, num_assignment_marks_to_write: int):
    """
    Saves the updated student data back to the namelist file, overwriting it.
    Includes assignment marks, total submissions, and submission rate.

    Args:
        filepath (str): Path to the namelist.txt file.
        students (List[Dict]): List of student data dictionaries.
        reporter (Reporter): Reporter instance for logging.
        num_assignment_marks_to_write (int): The number of individual assignment mark columns to write.
                                       This should be the number of mark columns determined at load time.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            for student in students:
                line_parts = [student['id'], student['name']]
                
                # Ensure student's marks list for output is exactly num_assignment_marks_to_write long
                marks_for_output = student['marks'][:num_assignment_marks_to_write]
                if len(marks_for_output) < num_assignment_marks_to_write:
                    marks_for_output.extend([0] * (num_assignment_marks_to_write - len(marks_for_output)))
                
                line_parts.extend(str(m) for m in marks_for_output)
                line_parts.append(str(student['total']))
                line_parts.append(f"{student['rate']:.2f}") # Format rate to 2 decimal places
                f.write("\t".join(line_parts) + "\n")
        reporter.info(f"Successfully saved updated student data to {filepath}")
    except Exception as e:
        reporter.error(f"Failed to save student data to '{filepath}': {e}")