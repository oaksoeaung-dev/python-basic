from werkzeug.security import generate_password_hash,check_password_hash

class User:
    def __init__(self,username="",password="",role="user"):
        self.Id = 0
        self.username = username
        self.password_hash = ""
        self.role = role
        if password:
            self.set_password(password)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def validate(self):
        if self.username == "":
            return False,"Username cannot be empty."
        return True,None

    def map(self,cursor_row):
        self.Id = cursor_row["id"]
        self.username = cursor_row["username"]
        self.password_hash = cursor_row["password_hash"]
        self.role = cursor_row["role"]
