import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine

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




# Create SQLAlchemy engine

# URL encode the password to handle special characters like '@'
password = quote_plus('@bc45678')

# Create the engine using the updated password
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/mysql_py')

# Load your dataframe to MySQL (replace option)
df.to_sql('retail_orders', con=engine, if_exists='replace', index=False)

print("Data has been loaded successfully with 'replace' option.")