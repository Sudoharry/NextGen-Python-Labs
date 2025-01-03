from datetime import datetime

# File name needs to specify where we want store the date and time

file_name = "devops_python.txt"


# Get the current date and time

current_datetime =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Open the file in append mode and write the date and time

with open(file_name, "a") as file:
      file.write(f"\nAppended on: {current_datetime}")

# Output

print(f"The current date and time has been appended to {file_name}")
