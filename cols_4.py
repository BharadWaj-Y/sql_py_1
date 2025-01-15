import pandas as pd

# Define the path to the dataset
csv_file_path = r"D:\dump\basics\SQL+PY_1\datasets\retail-orders.csv"

# Read the dataset using pandas
df = pd.read_csv(csv_file_path, na_values=['Not Available', 'unknown'])

# Convert all column names to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Print the updated column names
print(df.columns.tolist())
