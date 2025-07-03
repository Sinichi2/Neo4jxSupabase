from Supabase import create_client, Client
from dotenv import load_dotenv
import os

# Loading the .env file 
load_dotenv()

url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_API')

#Creating the supabase client 
supabase: Client = create_client(url, key)

response = (
    supabase.table()
)