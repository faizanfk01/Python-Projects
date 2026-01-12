import os

# Path to the folder you want to clean
folder_path = "D:/Python/Os Module Excercise"

# Get all files in the folder
files = os.listdir(folder_path)

# Dictionary to group files by extension
ext_map = {}

# Group files by their extension
for file in files:
    file_path = os.path.join(folder_path, file)

    # Skip if it's a folder
    if os.path.isfile(file_path):
        name, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext not in ext_map:
            ext_map[ext] = []
        ext_map[ext].append(file)

# Rename each file in order per extension
for ext, files_list in ext_map.items():
    for i, filename in enumerate(files_list, start=1):
        old_path = os.path.join(folder_path, filename)
        new_filename = f"{i}. File{ext}"
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} ➜ {new_filename}")
