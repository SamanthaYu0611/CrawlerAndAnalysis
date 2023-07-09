import pymysql
import os

def create_db_and_table(host, user, password, database, table):
    connection = pymysql.connect(host=host,user=user,password=password,)
    cursor = connection.cursor()
    
    create_database_sql = f"CREATE DATABASE IF NOT EXISTS {database}"
    cursor.execute(create_database_sql)

    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {database}.{table} (
        import_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id VARCHAR(255),
        post_id VARCHAR(255),
        username VARCHAR(255),
        time DATETIME,
        post_url VARCHAR(255),
        post_text TEXT,
        like_count INT,
        love_count INT,
        go_count INT,
        wow_count INT,
        haha_count INT,
        sad_count INT,
        angry_count INT,
        share_count INT,
        comment_count INT,
        PRIMARY KEY (user_id, post_id)
    )
    """
    cursor.execute(create_table_sql)
    connection.commit()
    cursor.close()
    connection.close()

host = os.getenv('DB_IP')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

create_db_and_table(host, user, password, database, 'fb_seven')    # (host, user, password, database, table)
create_db_and_table(host, user, password, database, 'fb_family')  # (host, user, password, database, table)
