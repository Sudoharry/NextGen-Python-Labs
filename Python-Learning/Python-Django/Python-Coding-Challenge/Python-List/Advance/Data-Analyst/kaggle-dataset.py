import os
import pandas as pd
import kagglehub

# Download dataset
path = kagglehub.dataset_download("samybaladram/multidisciplinary-csv-datasets-collection")

print("Path to dataset files:", path)


# List files
files = os.listdir(path)
print("Available files:", files)

# Load one file
import os
import pandas as pd
import kagglehub

# Download dataset
path = kagglehub.dataset_download("samybaladram/multidisciplinary-csv-datasets-collection")

print("Path to dataset files:", path)


# List files
files = os.listdir(path)
print("Available files:", files)

# Load dataset
df = pd.read_csv('homes.csv')

# Show top 5 rows
print(df.head())

# Summary info
print(df.info())

# Basic stats
print(df.describe())

