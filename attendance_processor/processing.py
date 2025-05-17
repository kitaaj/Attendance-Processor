

"""
Handles the core logic of processing submissions:
- Extracting student IDs from filenames.
- Updating student records with submission marks.
- Calculating total submissions and rates.
"""
import re
from typing import List, Dict, Optional
from .config import STUDENT_ID_REGEX
from .reporting import Reporter


def extract_student_id(filename: str, reporter: Reporter) -> Optional[str]:
    """
    Extracts an 8-digit student ID from a filename using regex.

    Args:
        filename (str): The filename to parse.
        reporter (Reporter): Reporter instance for logging (currently unused here but good practice).

    Returns:
        Optional[str]: The extracted student ID, or None if not found.
    """
    match = re.search(STUDENT_ID_REGEX, filename)
    if match:
        return match.group(1)
    return None

def mark_submission(student_record: Dict, assignment_index: int, max_mark_cols: int, reporter: Reporter):
    """
    Marks a submission for a student in their record.
    Assumes assignment_index is 0-based.

    Args:
        student_record (Dict): The student's data dictionary.
        assignment_index (int): The 0-based index of the assignment.
        max_mark_cols (int): Maximum number of mark columns available.
        reporter (Reporter): Reporter instance for logging.
    """
    if 0 <= assignment_index < max_mark_cols:
        if 0 <= assignment_index < len(student_record['marks']):
            if student_record['marks'][assignment_index] == 0: # Mark only if not already marked
                student_record['marks'][assignment_index] = 1
                # reporter.info(f"Marked assignment {assignment_index + 1} for student {student_record['id']}.") # Too verbose for here
                return True # Successfully marked
            else:
                # reporter.info(f"Assignment {assignment_index + 1} already marked for student {student_record['id']}.")
                return True # Already marked counts as success for this file
        else:
            # This should not happen if student_record['marks'] is initialized correctly
            reporter.warning(f"Student {student_record['id']} has fewer mark slots ({len(student_record['marks'])}) than expected ({max_mark_cols}). Cannot mark assignment {assignment_index + 1}.")
            return False
    else:
        reporter.warning(
            f"Assignment index {assignment_index + 1} is out of bounds for student {student_record['id']}. "
            f"Max assignment columns available: {max_mark_cols}. Submission not recorded for this assignment."
        )
        return False
    return False


def calculate_final_statistics(students_list: List[Dict], num_assignments_processed: int, max_mark_cols: int, reporter: Reporter):
    """
    Calculates total submissions and submission rate for each student.
    The rate is based on the number of assignments actually processed/considered.

    Args:
        students_list (List[Dict]): The list of student data dictionaries.
        num_assignments_processed (int): Number of assignment folders found and processed.
                        This defines the denominator for the rate.
        max_mark_cols (int): The number of available mark columns in student records.
        reporter (Reporter): Reporter instance for logging.
    """
    if not students_list:
        reporter.info("No students to calculate statistics for.")
        return

    # num_assignments_for_rate determines how many assignments are considered for the rate.
    # It should be the number of assignment folders, capped by available mark columns.
    num_assignments_for_rate = min(num_assignments_processed, max_mark_cols)

    if num_assignments_for_rate == 0:
        reporter.info("No assignments processed or no mark columns available; rates will be 0.")
    
    reporter.info(f"Calculating totals and rates based on {num_assignments_for_rate} assignment(s).")

    for student in students_list:
        # Calculate total based on marks up to num_assignments_for_rate
        # Student marks list should be at least max_mark_cols long.
        relevant_marks = student['marks'][:num_assignments_for_rate]
        student['total'] = sum(relevant_marks)

        if num_assignments_for_rate > 0:
            student['rate'] = student['total'] / num_assignments_for_rate
        else:
            student['rate'] = 0.0