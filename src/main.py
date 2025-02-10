#!/usr/bin/env python3
import os
import datetime

# Determine the repository root directory (assumes main.py is in the src folder)
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Define the path for version.md in the repository root
version_file_path = os.path.join(repo_root, 'version.md')

# Get the current date and time in the desired format
now = datetime.datetime.now()
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Write the formatted date and time to version.md
with open(version_file_path, 'w') as f:
    f.write(formatted_datetime + '\n')

print(f"Current date and time ({formatted_datetime}) written to {version_file_path}")
