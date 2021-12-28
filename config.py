import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DATABASE_URI = f'postgres+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:5432/Employee_Time'
