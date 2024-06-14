import os as o
import shutil

def optional_sub_folder(folder_path, subfolder_name):
    subfolder_path = o.path.join(folder_path, subfolder_name)
    if not o.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def clean_folder(filename):
    for files in o.listdir(filename):
        if o.path.isfile(o.path(join(filename, files))):
            file_extension = files.split(".")[-1].lower()
            if file_extension:
                sub_folder_name = f"{file_extension.upper()} files"
                path = optional_sub_folder(filename, files)
                file_path = o.path.join(filename, files)
                new_location = o.path.join(path, files)
                if not o.path.exists(new_location):
                    shutil.move(file_path, path)
                    print(f"Moved: {files} -> {sub_folder_name}")
                else:
                    print(f"Skipped: {files} already exists in {path}")

if "__name__" == "__main__":
    print("Desktop Cleaner by Mr. Jarme.\n")
    folder_path = input("Please Enter The Folder Path: \n")
    if o.path_isdir(folder_path):
        clean_folder(folder_path)
        print("Operation Complete")
    else:
        print("Process Error!")
