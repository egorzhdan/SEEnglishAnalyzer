import data


class Post(object):
    def __init__(self, node):
        self.identifier = node.get("Id")
        self.score = node.get("Score")
        self.owner_id = node.get("OwnerUserId")
        self.body = node.get("Body")

    def get_owner(self):
        return data.users[self.owner_id]


class User(object):
    def __init__(self, node):
        self.identifier = node.get("Id")
        self.display_name = node.get("DisplayName")
        self.reputation = node.get("Reputation")
        self.class2_count = 0

    def add_badge(self, node):
        badge_class = node.get("Class")
        if badge_class is not None and int(badge_class) == 2:
            self.class2_count += 1
