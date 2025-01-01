## Explanation:
1) List Creation: The tools list contains the names of various DevOps tools.
2) Loop: A for loop iterates over each element in the list.
3) Print: Each tool is printed in a formatted string.


## Explanation

1) tools:

This is the list containing multiple items (strings in this case).
It's like a collection or a container that holds the DevOps tools (e.g., "Docker", "Ansible", etc.).

2)tool:

This is a temporary variable that represents each individual item in the tools list during each iteration of the loop.
The for loop works by assigning one item from the tools list to tool in each cycle, starting with the first item and going until the last.

3) The for loop:

The for loop is a control flow structure used to iterate over each item in the list tools.
On each iteration:
The variable tool takes the value of the current item in the list.
The body of the loop (code inside the loop) executes with tool being the current item.

- Example of how tool changes in each iteration:

 - First iteration: tool = "Docker"
 - Second iteration: tool = "Ansible"
 - And so on, until all items in the tools list are processed.

4) The f"- {tool}":

- This is a formatted string literal (commonly called an f-string), introduced in Python 3.6.
- f" starts an f-string, allowing you to include variables or expressions inside {}.
- {tool} means: Insert the value of tool into the string after the hyphen (-).

- Example:
If tool = "Docker", then f"- {tool}" evaluates to "- Docker".
F-strings make it easy to create dynamic, readable strings.

- Example Execution Steps:
 - tools = ["Docker", "Ansible", "Terraform", "Kubernetes", "Prometheus", "Jenkins"]
 - First loop: tool = "Docker" → Prints: - Docker
 - Second loop: tool = "Ansible" → Prints: - Ansible
 - Repeats until all items are processed.

