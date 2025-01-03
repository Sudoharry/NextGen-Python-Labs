import os

# Get the current directory
current_directory = os.getcwd()


# List all files and directories
entries = os.listdir(current_directory)

print(f"Files and directories in '{current_directory}':")
for entry in entries:
   print(f"- {entry}")
