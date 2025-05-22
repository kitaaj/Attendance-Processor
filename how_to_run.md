
**1. Open Your Terminal or Command Prompt:**

*   **Windows:** Search for "Command Prompt" or "PowerShell".
*   **macOS:** Search for "Terminal" (usually in Applications > Utilities).
*   **Linux:** Usually Ctrl+Alt+T or search for "Terminal".

**2. Navigate to the Correct Directory:**

You need to navigate to the directory that **contains** the `attendance_processor` package. This is `your_project_root_directory`.

Use the `cd` (change directory) command. For example:
*   If your project is in `C:\Users\YourName\Documents\PythonProjects\AttendanceProcessor`, you would type:
    ```bash
    cd C:\Users\YourName\Documents\PythonProjects\AttendanceProcessor
    ```
*   If your project is in `/home/yourname/dev/attendance_processsor`, you would type:
    ```bash
    cd /home/yourname/dev/attendance_processsor
    ```

Once you are in `your_project_root_directory`, if you type `ls` (Linux/macOS) or `dir` (Windows), you should see `attendance_processor` (as a folder), `namelist.txt`, etc. listed.

**3. Run the Module:**

You will use Python's `-m` option, which tells Python to run a module as a script. The basic command structure is:

```bash
python -m attendance_processor.main <ACTION> [ACTION_ARGUMENTS...]
```
or if `python` defaults to Python 2 on your system, use `python3`:
```bash
python3 -m attendance_processor.main <ACTION> [ACTION_ARGUMENTS...]
```

**Available Actions and Examples:**

*   **`process`**: To process submissions, update marks, and save the namelist.
    *   **Basic usage (defaults to `namelist.txt`, `submissions/`, and `.py` files):**
        ```bash
        python -m attendance_processor.main process
        ```
    *   **Specify namelist and submissions directory:**
        ```bash
        python -m attendance_processor.main process my_students.txt course_work/
        ```
    *   **Specify file extension (e.g., for `.zip` files):**
        ```bash
        python -m attendance_processor.main process --ext .zip
        ```
    *   **Process and then view the table:**
        ```bash
        python -m attendance_processor.main process --view
        ```

*   **`query`**: To look up a specific student's details.
    *   **Query by student ID:**
        ```bash
        python -m attendance_processor.main query namelist.txt 20240135
        ```
    *   **Query by student name (case-insensitive, partial match):**
        ```bash
        python -m attendance_processor.main query namelist.txt "Thompson Joanna"
        ```
    *   **Specify a different namelist file:**
        ```bash
        python -m attendance_processor.main query alt_namelist.txt 20240924
        ```

*   **`view`**: To display the entire student list from a namelist file as a formatted table.
    *   **View default `namelist.txt`:**
        ```bash
        python -m attendance_processor.main view namelist.txt
        ```
    *   **View a specific namelist file:**
        ```bash
        python -m attendance_processor.main view processed_grades.txt
        ```

*   **Get Help:**
    *   For an overview of actions:
        ```bash
        python -m attendance_processor.main -h
        ```
    *   For help on a specific action (e.g., `process`):
        ```bash
        python -m attendance_processor.main process -h
        ```

**Summary of Steps:**
1.  Ensure Python and `tabulate` are installed.
2.  Open a terminal.
3.  `cd` into `your_project_root_directory` (the one containing the `attendance_processor` folder).
4.  Execute the desired command using `python -m attendance_processor.main <action> ...`.