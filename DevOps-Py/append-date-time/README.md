## Task

Append the current date and time to the same file.

## Explanation:

1) Importing datetime:

  The datetime module is used to get the current date and time.  
  datetime.now() fetches the current timestamp.
  strftime formats the timestamp into a readable string (YYYY-MM-DD HH:MM:SS).

2) Appending Mode:

  open(file_name, "a"): Opens the file in append mode ("a"). This allows you to add new content to the file without overwriting the existing content.

3)  Appending Data:

  file.write(f"\nAppended on: {current_datetime}"): Adds a newline before appending the current date and time.

4) Output:

  Prints a confirmation message indicating that the date and time have been appended.

