
"""
Configuration constants for the attendance processing application.
"""

# Regular expression to extract an 8-digit student ID from a filename.
# It looks for a sequence of 8 digits that forms a whole word (bounded by non-alphanumeric characters or start/end of string).
STUDENT_ID_REGEX = r'(?<!\d)(\d{8})(?!\d)'

# Default file extension to look for in submission folders (e.g., '.py', '.zip', '.txt')
DEFAULT_FILE_EXTENSION = '.py'

# Default name for the student list file
DEFAULT_NAMELIST_FILE = 'namelist.txt'

# Default name for the root directory containing assignment subfolders
DEFAULT_SUBMISSIONS_DIR = 'submissions'