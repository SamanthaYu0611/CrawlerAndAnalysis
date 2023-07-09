from facebook_scraper import get_posts
from time import sleep
from random import randint
import json
import os

def get_fb_posts(fanpage, page_default, cookies, filename):
    i = 1
    for post in get_posts(fanpage, pages=page_default, cookies=cookies, options={"reactors": True}):
        try:
            post_data = {
                'user_id': str(post['user_id']),
                'username': str(post['username']),
                'time': post['time'].strftime("%Y-%m-%d %H:%M:%S"),
                'post_url': post['post_url'],
                'post_id': str(post['post_id']),
                'post_text': post['post_text'].strip().replace("\n", ""),
                'like_count': post.get('reactions', {}).get('讚', 0),
                'love_count': post.get('reactions', {}).get('大心', 0),
                'go_count': post.get('reactions', {}).get('加油', 0),
                'wow_count': post.get('reactions', {}).get('哇', 0),
                'haha_count': post.get('reactions', {}).get('哈', 0),
                'sad_count': post.get('reactions', {}).get('嗚', 0),
                'angry_count': post.get('reactions', {}).get('怒', 0),
                'share_count': post.get('comments', 0),
                'comment_count': post.get('shares', 0),
            }
            print("\n\t>>>>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
            with open(filename, "a", encoding='utf-8') as file:
                file.write(json.dumps(post_data, ensure_ascii=False) + "\n")
        except Exception as e:
            print("\n\t>>>>> DONE{}.....An error occurred\n\t>>>>> {}\n\n".format(i, str(e)))
        i += 1
        sleep(randint(10, 60))

# 獲取路徑
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
print("脚本路径:", script_path)
print("脚本所在目录:", script_directory)

# 711
fanpage = "711open"
page_default = 50
cookies = os.path.join(script_directory, "www.facebook.com_cookies.txt")
filename = os.path.join(script_directory, "posts_7-11.jsonl")
get_fb_posts(fanpage, page_default, cookies, filename)
print(f"Saved: {filename}")

# # FamilyMart
# fanpage = "FamilyMart"
# page_default = 50
# cookies = os.path.join(script_directory, "www.facebook.com_cookies.txt")
# filename = os.path.join(script_directory, "posts_FamilyMart.jsonl")
# get_fb_posts(fanpage, page_default, cookies, filename)
# print(f"Saved: {filename}")
