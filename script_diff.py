import os
import sys
import hashlib
from pathlib import Path


# Function to calculate the MD5 hash of a file
def get_file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


# Function to create a dictionary of file hashes for all files in a directory
def get_files_directory(path):
    files_hash_dict = {}
    for root, dirs, files in os.walk(path):
        for f in files:
            file_path = os.path.join(root, f)
            if not os.path.islink(file_path):
                files_hash_dict[f] = [get_file_hash(file_path), file_path]
    return files_hash_dict


# Function to compare two directories and identify modified, created, and deleted files
def compare_hashes(dir1, dir2):
    files_deleted = []
    files_created = []
    files_changed = []
    files_hash_1 = get_files_directory(dir1)
    files_hash_2 = get_files_directory(dir2)

    # Compare file hashes between the two directories
    for key, value in files_hash_2.items():
        if key in files_hash_1:
            if value[0] != files_hash_1[key][0]:
                files_changed.append(key + ' -> (' + value[1] + ')')
        else:
            files_created.append(key + ' -> (' + value[1] + ')')

    # Identify deleted files
    for k, v in files_hash_1.items():
        if k not in files_hash_2:
            files_deleted.append(k + ' -> (' + v[1] + ')')

    return files_changed, files_created, files_deleted


if __name__ == "__main__":
    # Check if the script is provided with two directory paths as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 script_diff.py <Path version 1> <Path version 2>")
        sys.exit(1)

    # Get the directory paths from command-line arguments
    directory1 = Path(sys.argv[1])
    directory2 = Path(sys.argv[2])

    # Compare the two directories and get lists of modified, created, and deleted files
    modified_files, created_files, deleted_files = compare_hashes(directory1, directory2)

    # Print the results
    if modified_files:
        print("****** Modified Files ******")
        for file in modified_files:
            print('> ' + file)
    else:
        print("@@ No Files Changed @@")

    if created_files:
        print("\n****** Created Files ******")
        for file in created_files:
            print('> ' + file)
    else:
        print("\n@@ No Files Created @@")

    if deleted_files:
        print("\n****** Deleted Files ******")
        for file in deleted_files:
            print('> ' + file)
    else:
        print("\n@@ No Files Deleted @@")
