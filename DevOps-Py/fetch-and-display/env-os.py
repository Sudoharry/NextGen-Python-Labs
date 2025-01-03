import os


# Fetch all environment variables

environment_variables = os.environ


print("System Environment Variables")
for key, value in environment_variables.items():
    print(f"{key}: {value}")

