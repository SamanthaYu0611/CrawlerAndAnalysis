import json
import os
import pymysql

def insert(host, user, password, database, table, filename):
    connection = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = connection.cursor()

    insert_sql = f"""
    INSERT INTO {table} (user_id, post_id, username, time, post_url, post_text, like_count, love_count, go_count, wow_count, haha_count, sad_count, angry_count, share_count, comment_count)
    VALUES (%(user_id)s, %(post_id)s, %(username)s, %(time)s, %(post_url)s, %(post_text)s, %(like_count)s, %(love_count)s, %(go_count)s, %(wow_count)s, %(haha_count)s, %(sad_count)s, %(angry_count)s, %(share_count)s, %(comment_count)s)
    ON DUPLICATE KEY UPDATE post_id = post_id
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            cursor.execute(insert_sql, data)
    
    connection.commit()
    cursor.close()
    connection.close()

# 獲取路徑
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
print("脚本路径:", script_path)
print("脚本所在目录:", script_directory)

host = os.getenv('DB_IP')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

# 711
filename = os.path.join(script_directory, "posts_7-11.jsonl")
insert(host, user, password, database, 'fb_seven', filename)  # (host, user, password, database, table, filename)

# Family
filename = os.path.join(script_directory, "posts_FamilyMart.jsonl")
insert(host, user, password, database, 'fb_family', filename)  # (host, user, password, database, table, filename)