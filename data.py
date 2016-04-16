import xml.etree.ElementTree as ElementTree
import os
import stack_exchange

path = os.path.expanduser('~') + "/Downloads/dump/"


def load_answers():
    posts = []
    print("Loading Users.xml...", end=" ", flush=True)
    file = path + "Posts.xml"
    try:
        tree = ElementTree.parse(file).getroot()
    except FileNotFoundError:
        print("File", file, "not found")
        return []

    print("done.")
    for post in tree.iter():
        post_type = post.get("PostTypeId")
        if post_type is not None and int(post_type) == 2:
            posts.append(stack_exchange.Post(post))
    return posts
