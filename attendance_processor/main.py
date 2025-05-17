# attendance_processor/main.py

import argparse
import os
from . import file_operations
from . import processing
from .reporting import Reporter, display_student_details, display_attendance_table # Updated import
from .config import DEFAULT_FILE_EXTENSION, DEFAULT_NAMELIST_FILE, DEFAULT_SUBMISSIONS_DIR

def handle_process_action(args, reporter: Reporter):
    """Handles the 'process' action: update records based on submissions."""
    reporter.info("Action: Process Submissions")
    reporter.info(f"Namelist file: {args.namelist_file}")
    reporter.info(f"Submissions directory: {args.submissions_root_dir}")
    reporter.info(f"Processing file extension: {args.ext}")

    # Load student data. num_assignment_cols is the number of actual mark columns.
    students_list, num_assignment_cols = file_operations.load_student_data(args.namelist_file, reporter)
    
    if num_assignment_cols == -1 and not students_list: # Indicates a failure to determine structure from load_student_data
        reporter.error("Failed to determine namelist structure or load data. Cannot process.")
        return
    if not students_list: # General case for empty or fully unparseable after structure attempt
        reporter.error("No student data loaded. Exiting process action.")
        return


    students_dict = {student['id']: student for student in students_list}
    assignment_folders = file_operations.discover_assignment_folders(args.submissions_root_dir, reporter)

    if not assignment_folders:
        reporter.warning(f"No assignment subfolders found in '{args.submissions_root_dir}'. No new submissions will be processed.")
        # Proceed to calculate stats based on loaded marks and save, effectively re-saving if no changes.
    
    num_assignment_folders_found = len(assignment_folders)
    if assignment_folders: # Only log if folders were found
        reporter.info(f"Found {num_assignment_folders_found} assignment folder(s): {', '.join(assignment_folders)}")

    # Cap processing by the number of assignment columns in the namelist
    num_assignments_to_process = min(num_assignment_folders_found, num_assignment_cols)

    if num_assignment_folders_found > num_assignment_cols:
        reporter.warning(
            f"Found {num_assignment_folders_found} assignment folders, but namelist "
            f"only supports {num_assignment_cols} assignment marks. "
            f"Only the first {num_assignment_cols} assignments (folders) will be actively processed for marking."
        )
    
    overall_files_found_in_relevant_folders = 0
    overall_successful_marks_count = 0 # Tracks new '1's set in this run
    
    # Process submissions from folders up to num_assignments_to_process
    for assignment_index in range(num_assignments_to_process):
        folder_name = assignment_folders[assignment_index]
        reporter.info(f"Processing folder: '{folder_name}' (Assignment {assignment_index + 1})")
        assignment_path = os.path.join(args.submissions_root_dir, folder_name)
        submission_files = file_operations.get_submission_files_in_folder(assignment_path, args.ext, reporter)

        folder_files_found_count = len(submission_files)
        overall_files_found_in_relevant_folders += folder_files_found_count
        folder_successful_marks_count = 0
        folder_errors_this_folder_count = 0

        if not submission_files:
            reporter.info(f"No '{args.ext}' files found in '{folder_name}'.")
        
        for file_path in submission_files:
            filename = os.path.basename(file_path)
            student_id = processing.extract_student_id(filename, reporter)

            if student_id:
                if student_id in students_dict:
                    student_record = students_dict[student_id]
                    if processing.mark_submission(student_record, assignment_index, num_assignment_cols, reporter):
                        folder_successful_marks_count +=1
                else:
                    reporter.log_file_error(filename, f"Student ID '{student_id}' not found in namelist.", folder_name)
                    folder_errors_this_folder_count +=1
            else:
                reporter.log_file_error(filename, "Could not extract student ID.", folder_name)
                folder_errors_this_folder_count += 1
        
        overall_successful_marks_count += folder_successful_marks_count
        reporter.folder_summary(
            folder_name,
            folder_files_found_count,
            folder_successful_marks_count,
            folder_errors_this_folder_count,
            args.ext
        )

    # Recalculate final statistics for ALL students based on their marks arrays
    # The number of assignments for rate calculation is num_assignment_cols (the capacity of the sheet)
    # or num_assignments_to_process if we only want to rate based on folders we could process.
    # Let's use num_assignment_cols, as the sheet is structured for that many.
    processing.calculate_final_statistics(students_list, num_assignment_cols, num_assignment_cols, reporter)
    
    file_operations.save_student_data(args.namelist_file, students_list, reporter, num_assignment_cols)

    reporter.overall_summary(
        total_folders_processed=num_assignments_to_process, # Folders we actually looped through for marking
        total_files_found=overall_files_found_in_relevant_folders, # Files matching ext in those folders
        total_marks_recorded=overall_successful_marks_count, # New marks set in this run
        total_error_files=len(reporter.error_files_details)
    )

    if args.view_after_process:
        reporter.info("Displaying table after processing...")
        display_attendance_table(students_list, num_assignment_cols, reporter)

    reporter.info("Processing action complete.")


def handle_query_action(args, reporter: Reporter):
    """Handles the 'query' action: display details for a specific student."""
    reporter.info("Action: Query Student")
    reporter.info(f"Namelist file: {args.namelist_file}")
    reporter.info(f"Querying for: '{args.identifier}'")

    students_list, num_assignment_cols = file_operations.load_student_data(args.namelist_file, reporter)
    
    if num_assignment_cols == -1 and not students_list:
        reporter.error("Cannot query: Failed to determine namelist structure or load data.")
        return
    if not students_list :
        reporter.error("Cannot query: No student data loaded.")
        return

    found_student_list = []
    query_term_lower = args.identifier.lower()

    for student in students_list:
        if student['id'].lower() == query_term_lower:
            found_student_list.append(student)
            # ID should be unique, so we can break if an exact ID match is found.
            # If allowing multiple matches for ID (though unlikely), remove break.
            break 
        # Check for name match only if ID didn't match first for this student
        if not found_student_list and query_term_lower in student['name'].lower():
            found_student_list.append(student) # Could find multiple by name fragment

    if found_student_list:
        if len(found_student_list) > 1:
            reporter.info(f"Found {len(found_student_list)} students matching '{args.identifier}'. Displaying all:")
        for s in found_student_list:
            # Ensure total/rate are calculated for display if they weren't perfectly loaded or are from an old run
            # Note: load_student_data now loads total/rate. This re-calc is for consistency or if source was raw.
            temp_list_for_calc = [s] # Calculate for this student only
            processing.calculate_final_statistics(temp_list_for_calc, num_assignment_cols, num_assignment_cols, reporter)
            display_student_details(s, num_assignment_cols, reporter)
    else:
        reporter.warning(f"No student found with ID or name matching '{args.identifier}'.")
    reporter.info("Query action complete.")


def handle_view_action(args, reporter: Reporter):
    """Handles the 'view' action: display all student data as a table."""
    reporter.info("Action: View Table")
    reporter.info(f"Namelist file: {args.namelist_file}")

    students_list, num_assignment_cols = file_operations.load_student_data(args.namelist_file, reporter)

    if num_assignment_cols == -1 and not students_list:
        reporter.error("Cannot view table: Failed to determine namelist structure or load data.")
        return
    if not students_list:
        reporter.error("Cannot view table: No student data loaded.")
        return

    # Ensure totals/rates are fresh for display, especially if `load_student_data`
    # might not have perfectly loaded them or if they are from an old calculation.
    # `load_student_data` now loads them, but re-calculating ensures consistency for view.
    processing.calculate_final_statistics(students_list, num_assignment_cols, num_assignment_cols, reporter)

    display_attendance_table(students_list, num_assignment_cols, reporter)
    reporter.info("View action complete.")

def main():
    parser = argparse.ArgumentParser(
        description="Student Submission Processor CLI.",
        formatter_class=argparse.RawTextHelpFormatter # For better help text formatting
    )
    subparsers = parser.add_subparsers(dest="action", required=True, help="Action to perform. Use <action> -h for more help.")

    # --- Process Subparser ---
    parser_process = subparsers.add_parser(
        "process", 
        help="Process submissions, update records, and save to namelist file.",
        description=(
            "Reads student data from the namelist, scans submission folders for files,\n"
            "extracts student IDs, updates their submission marks, calculates totals/rates,\n"
            "and overwrites the namelist file with the updated records."
        )
    )
    parser_process.add_argument(
        "namelist_file",
        nargs='?', # Optional, will use default
        default=DEFAULT_NAMELIST_FILE,
        help=f"Path to the student namelist text file (default: {DEFAULT_NAMELIST_FILE})."
    )
    parser_process.add_argument(
        "submissions_root_dir",
        nargs='?', # Optional, will use default
        default=DEFAULT_SUBMISSIONS_DIR,
        help=f"Root directory containing assignment subfolders (default: {DEFAULT_SUBMISSIONS_DIR})."
    )
    parser_process.add_argument(
        "--ext",
        default=DEFAULT_FILE_EXTENSION,
        help=f"File extension of submission files to look for (e.g., '.py', '.txt') (default: {DEFAULT_FILE_EXTENSION})."
    )
    parser_process.add_argument(
        "--view",
        action="store_true",
        dest="view_after_process",
        help="Display the updated attendance table in the console after processing is complete."
    )
    parser_process.set_defaults(func=handle_process_action)

    # --- Query Subparser ---
    parser_query = subparsers.add_parser(
        "query",
        help="Query and display details for a specific student from the namelist.",
        description=(
            "Loads the specified namelist file and searches for a student by ID or name.\n"
            "Displays their current submission marks, total, and rate as found in the file."
        )
    )
    parser_query.add_argument(
        "namelist_file",
        help="Path to the student namelist text file to query."
    )
    parser_query.add_argument(
        "identifier",
        help="Student ID (exact match) or name (case-insensitive, partial match) to query."
    )
    parser_query.set_defaults(func=handle_query_action)

    # --- View Subparser ---
    parser_view = subparsers.add_parser(
        "view",
        help="Display the entire student namelist as a formatted table in the console.",
        description=(
            "Loads the specified namelist file and displays all student records, including\n"
            "submission marks, totals, and rates, in a tabular format."
        )
    )
    parser_view.add_argument(
        "namelist_file",
        help="Path to the student namelist text file to view."
    )
    parser_view.set_defaults(func=handle_view_action)
    
    args = parser.parse_args()
    reporter = Reporter() # Instantiate Reporter once
    
    # reporter.info("Starting Student Submission Processor CLI...") # Moved to specific handlers for context

    if hasattr(args, 'func'):
        args.func(args, reporter)
    else:
        # This case should ideally not be reached if 'action' is required and subparsers are set up.
        # If no action is provided, argparse itself will show an error.
        parser.print_help() 

if __name__ == '__main__':
    main()