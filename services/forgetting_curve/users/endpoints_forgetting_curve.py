from resources.base_url import base_url

URL = base_url()


class EndPoints:
    @staticmethod
    def post_users():
        url = URL + "/users"
        return url

    @staticmethod
    def get_users():
        url = URL + "/users"
        return url

    @staticmethod
    def get_user_by_nickname(nickname):
        url = URL + f"/users/{nickname}"
        return url

    @staticmethod
    def delete_users_by_nickname(nickname):
        url = URL + f"/users/{nickname}"
        return url

    @staticmethod
    def put_user_by_nickname(nickname):
        url = URL + f"/users/{nickname}"
        return url