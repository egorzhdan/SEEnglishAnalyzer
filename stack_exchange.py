class Post(object):
    def __init__(self, node):
        self.identifier = node.get("Id")
        self.score = node.get("Score")
        self.owner_id = node.get("OwnerUserId")
        self.body = node.get("Body")

