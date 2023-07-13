import json
import pymysql
import os 

def insert(host, user, password, database, table, data):

    # Connect to the database
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database
                                 )

    cursor = connection.cursor()

    # Insert into the database
    insert_sql = f"""
    INSERT INTO {table} (title, period, content, remark)
    VALUES (%(title)s, %(period)s, %(content)s, %(remark)s)
    ON DUPLICATE KEY UPDATE title = title
    """
    for n in data:
        cursor.execute(insert_sql, n)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    filename = "output_7-11.json"
    with open(filename, 'r', encoding='utf-8') as file:
        posts = json.load(file)

    host = os.getenv('DB_IP')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    insert('DB_IP', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'official_family', posts)       # (host, user, password, database, table, data)

