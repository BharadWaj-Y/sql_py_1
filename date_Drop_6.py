import pandas as pd

# Define the path to the dataset
csv_file_path = r"D:\dump\basics\SQL+PY_1\datasets\retail-orders.csv"

# Read the dataset using pandas
df = pd.read_csv(csv_file_path, na_values=['Not Available', 'unknown'])

# Convert column names to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Convert 'order_date' column from object to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Create new columns based on existing columns
df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
df['sale_price'] = df['list_price'] - df['discount']
df['profit'] = df['sale_price'] - df['cost_price']

# Drop the unwanted columns
df.drop(columns=['list_price', 'discount_percent', 'cost_price'], inplace=True)

# Print the first few rows to verify the changes
print(df[['order_date', 'discount', 'sale_price', 'profit']].head())
