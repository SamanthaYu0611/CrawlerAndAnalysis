import pymysql
import os 

def create_db_and_table(host, user, password, database, table):

    # Connect to the database
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 )
    cursor = connection.cursor()

    # Create database
    create_database_sql = f"CREATE DATABASE IF NOT EXISTS {database}"
    cursor.execute(create_database_sql)

    # Create table
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {database}.{table} (
    import_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    period VARCHAR(50),
    content VARCHAR(255),
    label VARCHAR(255),
    PRIMARY KEY (title, period,content)
    )
    """
    cursor.execute(create_table_sql)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    host = os.getenv('DB_IP')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    create_db_and_table('DB_IP', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'official_family')  # (host, user, password, database, table)