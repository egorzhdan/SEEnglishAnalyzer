import xml.etree.ElementTree as ElementTree
import os
import stack_exchange

path = os.path.expanduser('~') + "/Downloads/dump/"
users = dict()
posts = []


def load_answers():
    print("Loading Posts.xml...", end=" ", flush=True)
    file = path + "Posts.xml"
    try:
        tree = ElementTree.parse(file).getroot()
    except FileNotFoundError:
        print("File", file, "not found")
        return

    print("done.")
    for post in tree.iter():
        post_type = post.get("PostTypeId")
        if post_type is not None and int(post_type) == 2:
            posts.append(stack_exchange.Post(post))


def load_users():
    print("Loading Users.xml...", end=" ", flush=True)
    file = path + "Users.xml"
    try:
        tree = ElementTree.parse(file).getroot()
    except FileNotFoundError:
        print("File", file, "not found")
        return

    print("done.")
    for user in tree.iter():
        user_id = user.get("Id")
        if user_id is not None:
            users[int(user_id)] = stack_exchange.User(user)


def load_badges():
    print("Loading Badges.xml...", end=" ", flush=True)
    file = path + "Badges.xml"
    try:
        tree = ElementTree.parse(file).getroot()
    except FileNotFoundError:
        print("File", file, "not found")
        return []

    print("done.")
    for badge in tree.iter():
        user_id = badge.get("UserId")
        if user_id is not None:
            key = int(user_id)
            if key in users:
                users[key].add_badge(badge)
