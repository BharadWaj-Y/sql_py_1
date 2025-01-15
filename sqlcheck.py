from sqlalchemy import create_engine
from urllib.parse import quote_plus

# URL encode the password to handle special characters like '@'
password = quote_plus('@bc45678')

# Create the engine using the updated password
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/mysql_py')

# Check the connection
try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
