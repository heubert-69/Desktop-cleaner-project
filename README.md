🧹 Desktop Cleaner
---
A simple Python script that organizes files in a given folder by sorting them into subfolders based on their file extensions (e.g., PDF files, PNG files, etc.). Useful for cleaning up cluttered directories like the Desktop.

📦 Requirements
Python 3

Uses standard libraries: os, shutil

🚀 How to Use
Run the script:

```bash
python desktop_cleaner.py
```
Enter the full path of the folder you want to clean (e.g., your Desktop).

The script will:

Create subfolders like JPG files, PDF files, etc.

Move each file into its respective subfolder

Skip duplicates that already exist in destination folders

📁 Example
Before:

```arduino
Desktop/
├── image.jpg
├── resume.pdf
├── notes.txt
```
After running the script:

```arduino
Desktop/
├── JPG files/
│   └── image.jpg
├── PDF files/
│   └── resume.pdf
├── TXT files/
│   └── notes.txt
```

