import pandas as pd

# Define the path to the dataset
csv_file_path = r"D:\dump\basics\SQL+PY_1\datasets\retail-orders.csv"

# Read the dataset using pandas
df = pd.read_csv(csv_file_path)

# Display the first 20 rows of the dataset
print(df.head(20))
