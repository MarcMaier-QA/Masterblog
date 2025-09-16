import json


def load_posts():
    with open("posts.json", "r") as file:
        return json.load(file)


def save_posts(posts):
    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)