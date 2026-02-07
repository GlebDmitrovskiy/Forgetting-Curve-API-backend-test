class PayloadInformation:
    @staticmethod
    def create_information(information: str,explanation: str):
        data = {
            "information": information,
            "explanation": explanation
        }
        return data
