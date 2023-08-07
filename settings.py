from pathlib import Path
import sys

# Get the absoulute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent