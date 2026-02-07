from resources.base_url import base_url

URL = base_url()


class Endpoints:
    @staticmethod
    def post_information(nickname):
        url = URL + f"/users/{nickname}/information"
        return url

    @staticmethod
    def get_information(nickname):
        url = URL + f"/users/{nickname}/information"
        return url

    @staticmethod
    def delete_information(nickname, information_id):
        url = URL + f"/users/{nickname}/information/{information_id}"
        return url
