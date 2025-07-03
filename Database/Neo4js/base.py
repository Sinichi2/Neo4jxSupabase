from dotenv import load_dotenv 
from neo4j import GraphDatabase
import os 

#Loading the .env file 
load_dotenv()


def get_users(): 
    neo4j_uri = os.getenv('SUPABASE_URL')
    neo4j_user = os.getenv('SUPABASE_API')
    # when there will be a password
    driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user))

    
def insert_users(tx, users): 
    for user in users: 
        tx.run('''
               MERGE (u:User {id: $id})
               SET U.name = $name, u.email = $email
               ''', id=user['id'], name=user.get('name'), email=user.get('email'))
        
    with driver.session() as session: 
        session.write_transaction(insert_users, users)

