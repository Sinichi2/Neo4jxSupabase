
#Initialize everything 
__all__ = [
    ''
]

from supabase import create_client
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

# Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

# Neo4j
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_pass = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

# Fetch data from Supabase
response = supabase.table("users").select("*").execute()
users = response.data

# Insert into Neo4j
def insert_users(tx, users):
    for user in users:
        tx.run("""  
            MERGE (u:User {id: $id})
            SET u.name = $name, u.email = $email
        """, id=user['id'], name=user.get('name'), email=user.get('email'))

with driver.session() as session:
    session.write_transaction(insert_users, users)
