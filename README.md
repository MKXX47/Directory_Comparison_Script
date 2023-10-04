# Directory Comparison Script

This Python script allows you to compare two directories and identify modified, created, or deleted files between them. It calculates MD5 hashes of files to determine changes in content.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3.x
- hashlib (usually included with Python)
- pathlib (usually included with Python)

## Usage

1. Clone the repository or download the script file.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script with the following command:

   ```bash
   python3 script_diff.py <Path version 1> <Path version 2>

5. Replace <Path version 1> and <Path version 2> with the paths of the directories you want to compare.
6. The script will display the results in the terminal, including modified, created, and deleted files.
## Example
python3 script_diff.py /path/to/directory/old /path/to/directory/new

## Acknowledgments
This script uses the MD5 hashing algorithm to compare file content.
It leverages the hashlib and pathlib Python libraries for file hashing and directory traversal.
