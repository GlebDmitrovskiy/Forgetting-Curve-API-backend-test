from services.forgetting_curve.users.api_users import Users
class BaseTest:
    def setup_method(self):
        self.api_users = Users()
