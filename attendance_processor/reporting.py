from tabulate import tabulate

"""
Handles all console output for the attendance processing application,
including informational messages, warnings, errors, and summaries.
"""

class Reporter:
    """
    A simple class to handle reporting messages to the console.
    """
    def __init__(self):
        self.error_files_details = []

    def info(self, message: str):
        """Prints an informational message."""
        print(f"[INFO] {message}")

    def warning(self, message: str):
        """Prints a warning message."""
        print(f"[WARNING] {message}")

    def error(self, message: str):
        """Prints an error message."""
        print(f"[ERROR] {message}")

    def log_file_error(self, filename: str, reason: str, folder_name: str = ""):
        """Logs a file-specific error and stores its details."""
        log_message = f"File '{filename}' in folder '{folder_name}': {reason}" if folder_name else f"File '{filename}': {reason}"
        self.warning(log_message)
        self.error_files_details.append(log_message)


    def folder_summary(self, folder_name: str, files_found: int, students_marked: int, error_files_count: int,file_extension: str):
        """Prints a summary for a processed folder."""
        print("\n" + "="*30)
        self.info(f"Summary for folder: {folder_name}")
        print(f"  Files found ({file_extension}): {files_found}")
        print(f"  Students successfully marked: {students_marked}")
        print(f"  File errors in this folder: {error_files_count}")
        print("="*30 + "\n")

    def overall_summary(self, total_folders_processed: int, total_files_found: int, total_marks_recorded: int, total_error_files: int):
        """Prints the overall processing summary."""
        print("\n" + "#"*40)
        self.info("Overall Processing Summary")
        print(f"  Total assignment folders processed: {total_folders_processed}")
        print(f"  Total submission files found: {total_files_found}")
        print(f"  Total submissions successfully recorded: {total_marks_recorded}")
        print(f"  Total file-related errors encountered: {total_error_files}")
        if self.error_files_details:
            print("  Error File Details:")
            for detail in self.error_files_details:
                print(f"    - {detail}")
        else:
            print("  No file-related errors encountered.")
        print("#"*40 + "\n")



def display_student_details(student: dict, num_assignment_cols: int, reporter: Reporter):
    """
    Displays details for a single student in a readable format using tabulate.

    Args:
        student (dict): The student's data dictionary.
        num_assignment_cols (int): The number of assignment columns configured.
        reporter (Reporter): The reporter instance.
    """
    reporter.info(f"Student Details for ID: {student['id']}")
    print(f"  Name: {student['name']}")
    print("-" * 40)

    # Prepare data for assignment marks table
    if num_assignment_cols > 0 and 'marks' in student:
        marks_table_data = []
        student_marks = student.get('marks', [])
        if student_marks: # Only show table if there are marks
            for i in range(num_assignment_cols):
                mark_value = str(student_marks[i]) if i < len(student_marks) else 'N/A'
                marks_table_data.append([f"Assignment {i+1}", mark_value])
            
            print("Assignment Marks:")
            try:
                print(tabulate(marks_table_data, headers=["Assignment", "Mark"], tablefmt="pretty", stralign="left", colalign=("left", "center")))
            except Exception as e:
                reporter.error(f"Failed to generate marks table with tabulate: {e}")
                # Fallback or simple print if needed
                for assignment_name, mark_val in marks_table_data:
                    print(f"  {assignment_name}: {mark_val}")
        elif num_assignment_cols > 0: # Marks list might be empty but columns are configured
             print("  Assignment Marks: No marks recorded for the configured assignments.")

    elif num_assignment_cols == 0:
        print("  Assignment Marks: No assignment columns are configured in the namelist.")
    else: # 'marks' key missing or other unexpected state
        print("  Assignment Marks: Data not available or namelist structure issue.")
    
    print("-" * 40)

    # Prepare data for summary table
    summary_table_data = []
    total_submissions = student.get('total', 'N/A')
    submission_rate = student.get('rate', None)

    summary_table_data.append(["Total Submissions", str(total_submissions)])
    summary_table_data.append(["Submission Rate", f"{submission_rate:.2f}" if submission_rate is not None else 'N/A'])
    
    print("Overall Summary:")
    try:
        # You can choose different table formats like "grid", "fancy_grid", "pipe", "orgtbl", "rst", etc.
        print(tabulate(summary_table_data, tablefmt="pretty", colalign=("left", "left")))
    except Exception as e:
        reporter.error(f"Failed to generate summary table with tabulate: {e}")
        # Fallback
        print(f"  Total Submissions: {total_submissions}")
        print(f"  Submission Rate: {f'{submission_rate:.2f}' if submission_rate is not None else 'N/A'}")

    print("— " * 40 + "Bottom Line" + " —" * 40)
    


def display_attendance_table(students_list: list, num_assignment_cols: int, reporter: Reporter):
    """
    Displays the full student list as a formatted table using the tabulate module.
    (This function remains the same as the previous version using tabulate)
    """
    if not students_list:
        reporter.info("No student data to display in table.")
        return

    reporter.info("Attendance/Submission Analysis Table:")

    headers = ["ID", "Name"]
    if num_assignment_cols > 0:
        headers.extend([f"A{i+1}" for i in range(num_assignment_cols)])
    headers.extend(["Total", "Rate"])

    table_data = []
    for student in students_list:
        row = [student['id'], student['name']]
        if num_assignment_cols > 0:
            student_marks = student.get('marks', [])
            for i in range(num_assignment_cols):
                row.append(str(student_marks[i]) if i < len(student_marks) else '0')
        
        row.append(str(student.get('total', 0)))
        row.append(f"{student.get('rate', 0.0):.2f} ({student.get('rate', 0.0)*100:.0f} %)")
        table_data.append(row)

    # Print the table using tabulate
    # You can choose different table formats like "grid", "fancy_grid", "pipe", "orgtbl", "pretty", "rst", etc.
    # "fancy_grid" is a good default.

    try:
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left", numalign="center"))
    except Exception as e:
        reporter.error(f"Failed to generate table with tabulate: {e}")
        reporter.warning("Falling back to basic print (if implemented) or no table.")
        # I can implement a very basic fallback print here if tabulate fails for some reason.
        # For now, I'll just log the error.

    print("— " * 40 + "Bottom Line" + " —" * 40)


# Import DEFAULT_FILE_EXTENSION for use in Reporter, or pass it as an argument.
# For simplicity, I am assuming that it's known or Reporter methods get it if needed.
from .config import DEFAULT_FILE_EXTENSION