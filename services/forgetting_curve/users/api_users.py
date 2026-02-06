from services.forgetting_curve.users.payload_forgetting_curve import PayloadForgettingCurveUsers
from services.forgetting_curve.users.endpoints_forgetting_curve import EndPoints
from config.headers import Headers
import requests


class Users:
    def __init__(self):
        self.endpoints = EndPoints()
        self.payload = PayloadForgettingCurveUsers()
        self.headers = Headers()

    def create_users(self, nickname: str, first_name: str, last_name: str, age: int, job: str):
        response = requests.post(url=self.endpoints.post_users(),
                                 headers=self.headers.post_headers(),
                                 json=self.payload.create_users(nickname=nickname, first_name=first_name,
                                                                last_name=last_name, age=age, job=job))

        return response

    def get_users(self):
        response = requests.get(url=self.endpoints.get_users())
        return response

    def get_users_by_nickname(self, nickname: str):
        response = requests.get(url=self.endpoints.get_user_by_nickname(nickname=nickname))
        return response

    def delete_users_by_nickname(self, nickname: str):
        response = requests.delete(url=self.endpoints.delete_users_by_nickname(nickname=nickname),
                                   headers=self.headers.delete_users_by_nickname())
        return response

    def update_users_by_nickname(self, nickname: str, **data):
        response = requests.put(url=self.endpoints.put_user_by_nickname(nickname=nickname),
                                headers=self.headers.update_users_by_nickname(),
                                json=self.payload.update_user_by_nickname(**data))
        return response
