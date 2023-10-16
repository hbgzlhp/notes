from neo4j import GraphDatabase
import json

uri = "bolt://localhost:7687"  # Neo4j数据库的URI
username = "neo4j"  # Neo4j数据库的用户名
password = "Lihongping1."  # Neo4j数据库的密码

driver = GraphDatabase.driver(uri, auth=(username, password))
session = driver.session()


with open('test.json', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    entity_1 = item['entity_1']
    entity_2 = item['entity_2']
    relationship = item['relationship']

    query = f'MERGE (e1:Entity {{name: "{entity_1}"}}) ' \
            f'MERGE (e2:Entity {{name: "{entity_2}"}}) ' \
            f'MERGE (e1)-[:{relationship}]->(e2)'

    session.run(query)

session.close()
driver.close()

