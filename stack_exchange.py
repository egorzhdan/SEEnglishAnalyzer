class Post(object):
    def __init__(self, node):
        self.identifier = node.get("Id")
        self.score = node.get("Score")
        self.owner_id = node.get("OwnerUserId")
        self.body = node.get("Body")


class User(object):
    def __init__(self, node):
        self.identifier = node.get("Id")
        self.display_name = node.get("DisplayName")
        self.reputation = node.get("Reputation")
        self.class2_count = 0
