from services.forgetting_curve.users.api_users import Users
from services.forgetting_curve.information.api_information import Information
class BaseTest:
    def setup_method(self):
        self.api_users = Users()
        self.api_information = Information()