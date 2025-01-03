## Program

Python script to create a text file and write "Python is useful for DevOps" into it

## Explanation:

1) File Name and Content:

file_name: The name of the file to be created.
content: The string to be written into the file.

2) Open the File:

open(file_name, "w"): Opens the file in write mode ("w"). If the file doesn’t exist, it creates it. If it exists, it overwrites the content.

3)Write to File:

file.write(content): Writes the string to the file.

4) Context Manager:

Using with open(...) ensures the file is properly closed after the writing operation, even if an error occurs.

5) Output:

Prints a confirmation message indicating the file has been created and written.

### Output:
When you run the script, it creates a file named devops_python.txt with the content:

```
Python is useful for DevOps
```
