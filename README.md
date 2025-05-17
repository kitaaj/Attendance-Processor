

# Student Submission Processor

This Python CLI application automates the process of tracking student submissions/attendance based on files submitted in a structured directory.
It reads a list of students, scans submission folders, extracts student IDs from filenames, updates their records, calculates totals and rates, and writes the updated information back to the student list file.

## Project Structure

```
.
├── attendance_processor/
│   ├── __init__.py
│   ├── config.py           # Configuration constants (regex, defaults)
│   ├── file_operations.py  # Handles reading/writing files, discovering submissions
│   ├── main.py             # CLI entry point and main orchestration logic
│   ├── processing.py       # Core data processing (ID extraction, marking, stats)
│   └── reporting.py        # Handles console output and logging
├── namelist.txt            # Input student list file
├── submissions/            # Root directory for assignment subfolders
│   ├── assignment1/
│   │   └── 20240135_assign1.py
│   │   └── ...
│   └── assignment2/
│       └── ...
├── requirements.txt        # Project dependencies (currently none external)
└── README.md               # This file
```

## Prerequisites

*   Python 3.6 or higher.

## Setup

No special setup is required beyond having Python installed.
In case needed:

```bash
pip install -r requirements.txt
```

## `namelist.txt` Format

The `namelist.txt` file should be a tab-separated values (TSV) file with the following format for each student on a new line:

```
StudentID\tFullName\tMark1\tMark2\t...\tMarkN
```

Example:
```bash
20240135	THOMPSON JOANNA B	0	0	0	0	0	0	0	0	0
20240222	AMPURIRE LISAR CLARKSON	0	0	0	0	0	0	0	0	0
```
The initial `0`s are placeholders for submission marks. The program will determine the number of mark columns from the first valid line of this file. The output file will append two new columns: `TotalSubmissions` and `SubmissionRate`.

## `submissions` Directory Structure

The `submissions` directory should contain subfolders, each representing a distinct assignment or check-in. The subfolders will be processed in alphabetical order.

Example:
```bash
submissions/
├── lab01/
│   ├── 20240135_thompson_lab1.py
│   ├── 20240222_clarkson_lab1.py
│   └── some_other_file.txt
├── lab02/
│   ├── 20240135_lab2_submission.py
│   └── student_20240924_lab02.py
└── weekly_quiz_01/
│       └── (example files for quiz)
```
The program will look for files with a specific extension (default `.py`) within these subfolders. Student IDs (assumed to be 8-digit numbers) will be extracted from the filenames.

## How to Run

Navigate to the directory containing the `attendance_processor` package (i.e., the directory where `namelist.txt` and `submissions/` would typically reside, or one level above the `attendance_processor` folder).

Run the script from your terminal:

```bash
python -m attendance_processor.main [namelist_file] [submissions_root_dir] [--ext FILE_EXTENSION]
```

**Arguments:**

*   `namelist_file` (optional): Path to the student list file. Defaults to `namelist.txt` in the current directory.
*   `submissions_root_dir` (optional): Path to the root directory containing assignment subfolders. Defaults to `submissions/` in the current directory.
*   `--ext FILE_EXTENSION` (optional): The file extension to look for (e.g., `.py`, `.txt`). Defaults to `.py`.

**Examples:**

1.  Run with default file/directory names (`namelist.txt`, `submissions/`, `.py` files):

```bash
    python -m attendance_processor.main
```

2.  Specify a different namelist file and submissions directory:

```bash
    python -m attendance_processor.main my_students.txt course_assignments/
```

3.  Process `.zip` files instead of `.py`:
```bash
    python -m attendance_processor.main --ext .zip
```

## Output

*   **Console Logs**: The program will print detailed logs to the console during processing, including:
    *   Current folder being processed.
    *   Files found and student IDs extracted.
    *   Successful markings.
    *   Errors (e.g., ID not found, ID not extracted).
    *   Summary statistics for each folder.
    *   Overall processing statistics.

*   **`namelist.txt` (Updated)**: The original `namelist.txt` file (or the specified one) will be overwritten with the updated records. Each student's line will include:
    *   Original ID and Name.
    *   Updated marks (0 or 1) for each processed assignment (within the capacity of the original mark columns).
    *   Any remaining original mark columns if fewer assignments were processed than columns available.
    *   A `TotalSubmissions` count.
    *   A `SubmissionRate` (formatted to two decimal places).

    Example output line (if 3 assignments processed and namelist had 9 mark columns):
    `20240135\tTHOMPSON JOANNA B\t1\t1\t0\t0\t0\t0\t0\t0\t0\t2\t0.67`
    (Here, 2 submissions out of 3 processed assignments, rate 2/3 = 0.67)