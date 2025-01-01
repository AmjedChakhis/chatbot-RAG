from neo4j import GraphDatabase, TrustSystemCAs
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
pwd = os.getenv("NEO4J_PASSWORD")

# Use TrustSystemCAs to trust the system's certificate authorities
driver = GraphDatabase.driver(
    uri,
    auth=(user, pwd),
    trusted_certificates=TrustSystemCAs()  # Correct usage
)
print(uri)

try:
    driver.verify_connectivity()
    print(uri)
    print("Connection successful")
except Exception as e:
    print(uri)
    print(f"Connection failed: {e}")
finally:
    print(uri)
    driver.close()
