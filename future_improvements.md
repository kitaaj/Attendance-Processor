# Future Improvements for the Student Submission Processor

This document outlines potential future enhancements for the Student Submission Processor CLI tool. These improvements aim to enhance usability, provide richer insights, and offer more flexible processing options.

## 1. Enhanced Console Output & Visualization

*  [x] **Formatted Table Views:** ---------> **DONE**
    *   **Current State:** The current views for all student data and individual student queries are functional but present information in a basic line-by-line format.
    *   **Proposed Improvement:** Implement well-structured, aligned tables for displaying:
        *   The full student attendance/submission list (similar to a spreadsheet view).
        *   The detailed breakdown of an individual student's marks and summary.
    *   **Benefit:** Significantly improves readability and makes it easier to quickly scan and understand the data.
    *   **Technical Note:** This could be achieved using Python libraries like `tabulate` or by implementing custom table formatting logic.
    *
    * How to run:

```bash
        python -m attendance_processor.main view namelist.txt
```

*  [] **Color-Coded Output (Optional):**
    *   **Proposed Improvement:** Use different colors in the console output to highlight:
        *   Errors (e.g., red).
        *   Warnings (e.g., yellow).
        *   Successful operations or key summary figures (e.g., green).
    *   **Benefit:** Makes it easier to spot critical information in the processing logs.

## 2. More Advanced Querying & Filtering
*  [X] Query a single student details

```bash
        python -m attendance_processor.main query namelist.txt 20240135
```

*  [] **Filter by Submission Rate:**
    *   **Proposed Improvement:** Add an option to the `view` or a new `filter` command to display only students whose submission rate is above or below a certain threshold.
    *   **Benefit:** Helps identify students who are falling behind or excelling.

*  [] **Filter by Specific Assignment Submission:**
    *   **Proposed Improvement:** Allow filtering to show students who have (or have not) submitted a particular assignment.
    *   **Benefit:** Useful for targeted follow-ups for specific assignments.

*  [] **Sortable Table Views:**
    *   **Proposed Improvement:** When displaying the full table view, allow sorting by columns (e.g., sort by student name, ID, total submissions, or submission rate).
    *   **Benefit:** Provides flexibility in how the data is analyzed and presented.

## 3. Enhanced File Processing Capabilities

*  [] **Processing Files within Archives (e.g., .zip, .tar.gz):**
    *   **Current State:** The tool can identify archive files (like `.zip`) if the student ID is in the archive's filename.
    *   **Proposed Improvement:** Add functionality to:
        1.  Identify student IDs from filenames *inside* a submitted archive (e.g., a `student_id.py` file within `submission_package.zip`).
        2.  Optionally, verify the presence of specific required files within an archive.
    *   **Benefit:** Supports more complex submission requirements where students bundle multiple files.
    *   **Technical Note:** This would involve using Python's `zipfile` or `tarfile` modules.

*  [] **Support for Multiple File Types per Assignment:**
    *   **Proposed Improvement:** Allow an assignment check-in to be satisfied if *any* of a list of specified file types are found for a student (e.g., `.py` OR `.ipynb`).
    *   **Benefit:** More flexibility for assignments where multiple submission formats are acceptable.

## 4. Configuration and Usability

* [] **Configuration File:**
    *   **Proposed Improvement:** Allow some default settings (like default namelist file, submissions directory, common file extensions) to be specified in a configuration file (e.g., `config.ini` or `config.yaml`) instead of only through command-line arguments.
    *   **Benefit:** Simplifies command usage for common scenarios.

*  [] **Interactive Mode (Optional):**
    *   **Proposed Improvement:** An optional interactive mode that guides the user through steps like selecting the namelist, submissions directory, and action to perform.
    *   **Benefit:** May be more user-friendly for users less comfortable with command-line arguments.

*  [] **More Granular Logging Levels:**
    *   **Proposed Improvement:** Allow users to specify a logging level (e.g., DEBUG, INFO, WARNING, ERROR) to control the verbosity of the console output.
    *   **Benefit:** DEBUG mode could help in troubleshooting, while a quieter mode might be preferred for standard runs.

## 5. Reporting and Exporting

* []  **Export to CSV/Excel:**
    *   **Proposed Improvement:** Add an option to export the final processed student data (the content of the updated `namelist.txt`) into a CSV or simple Excel format.
    *   **Benefit:** Allows for easier data sharing and further analysis in spreadsheet software.

*  [] **Summary Report File:**
    *   **Proposed Improvement:** Option to save the overall processing summary (currently printed to the console) to a text file.
    *   **Benefit:** Useful for record-keeping and automated report generation.
