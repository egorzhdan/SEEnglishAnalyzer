import xml.etree.ElementTree as ElementTree
import os
import stack_exchange

path = os.path.expanduser('~') + "/Downloads/dump/"
users = dict()
posts = dict()


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
            new_post = stack_exchange.Post(post)
            posts[new_post.identifier] = new_post


def load_questions():
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
        if post_type is not None and int(post_type) == 1:
            new_post = stack_exchange.Post(post)
            posts[new_post.identifier] = new_post


def load_links():
    print("Loading PostLinks.xml...", end=" ", flush=True)
    file = path + "PostLinks.xml"
    try:
        tree = ElementTree.parse(file).getroot()
    except FileNotFoundError:
        print("File", file, "not found")
        return

    print("done.")
    for entry in tree.iter():
        link_type = entry.get("LinkTypeId")
        if link_type is not None and int(link_type) == 3:
            rel_post_id = entry.get("RelatedPostId")
            post_id = entry.get("PostId")
            if rel_post_id is not None and rel_post_id in posts and post_id in posts:
                posts[rel_post_id].dupes.append(post_id)


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
