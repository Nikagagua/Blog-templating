import requests


class Post:
    def __init__(self):
        blog_url = 'https://api.npoint.io/0bd32f974ed7a1c26000'
        try:
            response = requests.get(url=blog_url)
            self.all_posts = response.json()
        except requests.exceptions.RequestException as err:
            print(f"Error retrieving blog posts: {err}")
            self.all_posts = []