# Python for DevOps: Comprehensive Task Guide

This README file contains a comprehensive list of Python tasks organized by levels and categories to help you develop Python skills from a DevOps perspective. The tasks start from basic programming concepts and progress to advanced automation and DevOps-specific applications.

---

## **Basic Level: Python Fundamentals**

1. **Print 'Hello, DevOps!'**
   - Write a Python program to print "Hello, DevOps!" and explore different print function variations.

2. **Variables and Printing**
   - Create variables for your name, role, and company, then print them in a formatted string.

3. **Arithmetic Operations**
   - Write a Python program to find the sum, difference, product, and division of two numbers.

4. **Even or Odd**
   - Create a program that checks whether a number is even or odd.

5. **Factorial Calculation**
   - Write a script to calculate the factorial of a given number.

6. **Iterating Through a List**
   - Create a list of tools (e.g., Docker, Ansible) and iterate over them using a loop.

7. **Dictionary Operations**
   - Use a dictionary to store configuration details (e.g., IP, port, username) and print them.

8. **String Manipulations**
   - Write a program to convert a string to uppercase, lowercase, and title case.

9. **Palindrome Check**
   - Implement a simple program to check if a string is a palindrome.

10. **Loop with `continue`**
    - Use a loop to print numbers from 1 to 10, but skip 5 using the `continue` statement.

---

## **Intermediate Level: File and OS Operations**

11. **File Creation and Writing**
    - Write a script to create a text file and write "Python is useful for DevOps" into it.

12. **Appending Date and Time**
    - Append the current date and time to the same file.

13. **Directory Listing**
    - List all files and directories in the current directory using the `os` module.

14. **File Existence Check**
    - Check if a given file exists and delete it if it does.

15. **Log File Line Count**
    - Write a program to read a log file and count the number of lines.

16. **File Copy**
    - Create a program to copy the contents of one file to another.

17. **Environment Variables**
    - Use the `os` module to fetch and display the system's environment variables.

18. **Disk Usage Calculation**
    - Create a program to calculate the disk usage of a directory.

---

## **Networking and Automation**

19. **Fetch IP Address**
    - Use `socket` to fetch the IP address of a given domain.

20. **Ping a Server**
    - Write a Python script to ping a server and check its status.

21. **Automate SSH**
    - Automate SSH login using `paramiko` and execute a command on a remote server.

22. **Website Availability Monitoring**
    - Create a script to monitor a website's availability (HTTP 200 status).

23. **System Performance Stats**
    - Write a program to fetch system performance stats (CPU, memory, disk usage).

24. **Run Shell Commands**
    - Use `subprocess` to run a shell command (e.g., `ls`) and capture its output.

25. **Automate User Creation**
    - Automate the creation of users on a Linux system using Python.

26. **Fetch Public IP**
    - Fetch public IP information using an external API (e.g., ipify).

---

## **Cloud and DevOps-Specific Tasks**

27. **List S3 Buckets**
    - Use `boto3` to list all S3 buckets in an AWS account.

28. **Create an EC2 Instance**
    - Write a Python script to create an EC2 instance using `boto3`.

29. **Fetch Jenkins Job Details**
    - Write a script to fetch details of a Jenkins job using its REST API.

30. **Automate Docker Containers**
    - Automate Docker container creation and management using `docker-py`.

31. **Fetch GitHub Repo Details**
    - Use Python to fetch GitHub repository details via its API.

32. **Parse Ansible Inventory**
    - Write a script to parse an Ansible inventory file and list the hosts.

33. **Automate Log Collection**
    - Use `paramiko` to automate log collection from multiple servers.

34. **Create Kubernetes Namespace**
    - Write a Python script to create a Kubernetes namespace using the `kubernetes` library.

---

## **Error Handling and Debugging**

35. **Intentional Errors**
    - Create a program with intentional errors and use `try-except` to handle them.

36. **Validate YAML/JSON Files**
    - Write a script to validate a YAML or JSON configuration file.

37. **Add Logging**
    - Add logging to a Python script using the `logging` module.

38. **Custom Exception Handling**
    - Create a Python function that raises a custom exception if disk usage exceeds a threshold.

---

## **Data Parsing and Processing**

39. **Parse Log Files**
    - Parse an Apache/Nginx log file and count the number of 404 errors.

40. **Extract IP Addresses**
    - Use `re` to extract IP addresses from a text file.

41. **CSV to JSON Conversion**
    - Write a program to convert a CSV file of user data to JSON format.

42. **JSON Parsing**
    - Parse a JSON file and extract specific details (e.g., usernames).

---

## **Advanced Tasks**

43. **Trigger Terraform Deployment**
    - Write a Python script to trigger a Terraform deployment using `subprocess`.

44. **Automate Git Tasks**
    - Automate Git tasks like creating branches and committing changes using `gitpython`.

45. **Fetch Prometheus Metrics**
    - Write a script to fetch Prometheus metrics and display system performance data.

46. **Monitor Kubernetes Pods**
    - Create a script to monitor Kubernetes pod statuses and send alerts.

47. **Database Connection**
    - Use Python to connect to a database and fetch/query data.

48. **Backup to S3**
    - Automate backup of critical files to S3 using `boto3`.

49. **Compare Config Files**
    - Write a script to compare two configuration files and highlight differences.

50. **Generate Reports**
    - Use Python to generate a report from log files and email it.

---

## **Tips for Progression**

- Start with basic Python syntax and structure.
- Gradually move to scripts that interact with the file system and external APIs.
- Include error handling and logging early on for better debugging.
- Focus on tools and libraries relevant to your DevOps workflow (e.g., `paramiko`, `boto3`).
- Combine multiple tasks to create meaningful automation scripts.

---

Happy Coding! 🚀
