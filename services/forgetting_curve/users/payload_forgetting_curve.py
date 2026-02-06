class PayloadForgettingCurveUsers:
    @staticmethod
    def create_users(nickname: str, first_name: str, last_name: str, age: int, job: str):
        data = {
            "nickname": nickname,
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "job": job
        }
        return data

    @staticmethod
    def update_user_by_nickname(age: int, job: str):
        data = {
            "age": age,
            "job": job
        }
        return data
