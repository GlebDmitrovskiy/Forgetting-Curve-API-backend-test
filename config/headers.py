class Headers:
    def __init__(self):
        self.basic = {"Content-type":"application/json"}

    def post_headers(self):
        return self.basic

    def delete_users_by_nickname(self):
        return self.basic

    def update_users_by_nickname(self):
        return self.basic
