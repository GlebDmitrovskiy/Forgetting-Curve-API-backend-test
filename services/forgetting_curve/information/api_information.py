from services.forgetting_curve.information.endpoints import Endpoints
from services.forgetting_curve.information.payload_information import PayloadInformation
import requests


class Information:
    def __init__(self):
        self.endpoints = Endpoints()
        self.payload_information = PayloadInformation()

    def create_information(self, nickname, information: str, explanation: str):
        response = requests.post(url=self.endpoints.post_information(nickname=nickname),
                                 json=self.payload_information.create_information(information=information,
                                                                                  explanation=explanation))

        return response

    def delete_information(self, nickname, information_id: str):
        response = requests.delete(url=self.endpoints.delete_information(nickname=nickname, information_id=information_id))
        return response

    def get_information(self, nickname):
        response = requests.get(url=self.endpoints.get_information(nickname=nickname))
        return response

