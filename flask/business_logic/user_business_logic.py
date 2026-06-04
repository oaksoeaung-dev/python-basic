from data_access.user_data_access import UserDataAccess
from models.user import User

class UserBusinessLogic:
    def __init__(self):
        self.da = UserDataAccess()

    def register_user(self,username,password,role="user"):
        user = User(username,password,role)
        success,message = user.validate()
        if not success:
            return success,message
        try:
            self.da.create_user(user)
            return True,"Registration successful!"
        except Exception:
            return False,"Username already exists."

    def authenticate_user(self,username,password):
        user = self.da.get_user_by_username(username)
        if user is None:
            return False,"User not found."
        if not user.check_password(password):
            return False,"Incorrect password."
        return True,user

    def get_user_by_username(self,username):
        return self.da.get_user_by_username(username)
