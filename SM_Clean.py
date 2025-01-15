
import pandas as pd

# Define the path to the dataset
csv_file_path = r"D:\dump\basics\SQL+PY_1\datasets\retail-orders.csv"

# Read the dataset using pandas
df = pd.read_csv(csv_file_path,na_values=['Not Available','unknown'])

print(df['Ship Mode'].unique())