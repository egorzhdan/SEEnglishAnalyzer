import xml.etree.ElementTree as ElementTree
import os
import stack_exchange

path = os.path.expanduser('~') + "/Downloads/dump/"


def load_answers():
    posts = []
    print("Loading Users.xml...", end=" ", flush=True)
    tree = ElementTree.parse(path + "Posts.xml").getroot()
    print("done.")
    for post in tree.iter():
        post_type = post.get("PostTypeId")
        if post_type is not None and int(post_type) == 2:
            posts.append(stack_exchange.Post(post))
    return posts
