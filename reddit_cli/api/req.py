import click
import requests

while(True):
    r = requests.get('https://api.reddit.com/hot')
    if (r.status_code == 200):
        break;
        
"""
return: posts[i]['data']['title']
"""
def top_posts():
    r_json = r.json()
    posts = r_json['data']['children']
    return posts
