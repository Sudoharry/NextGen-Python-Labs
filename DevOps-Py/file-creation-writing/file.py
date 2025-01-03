## Crete a file and write the content in it

file_name = "devops_python.txt"
content = "Pyhton is useful for DevOps."


# Check the file exits and if doesn't exits then create a new file name and overwrite the content if it exits

with open (file_name, "w") as file:
     file.write(content)

#Output
print(f"The text message is written to {file_name}")
