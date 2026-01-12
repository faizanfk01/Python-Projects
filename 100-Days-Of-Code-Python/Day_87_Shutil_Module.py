import shutil
import os

# shutil.copy("main.py", "main2.py")
# shutil.copytree(".tutorial", "mytutorial")
# shutil.move(".tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial")
# os.remove("file.file")


folder_path = "D:/Python"
os.chdir(folder_path)

folder_name = "Os Module Excercise 1"

for i in range(2, 11):
    new_filename = f"Os Module Excercise {i}"
    if os.path.exists(folder_name):
        shutil.copytree("Os Module Excercise 1", new_filename)
        print(f"Copied to {new_filename}")
    else:
        print("The Folder doesn't Exists, FAILED!")