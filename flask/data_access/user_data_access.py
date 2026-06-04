import sqlite3
from models.user import User

class UserDataAccess:
    def __init__(self):
        self.__DATABASE = "appdb.db"
        self.__create_table()

    def __create_connection(self):
        conn = sqlite3.connect(self.__DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

    def __create_table(self):
        with self.__create_connection() as con:
            con.execute("""
                create table if not exists user(
                    id integer primary key autoincrement,
                    username text not null unique,
                    password_hash text not null,
                    role text not null default 'user'
                )
            """)
            con.commit()

    def create_user(self,user:User):
        with self.__create_connection() as con:
            con.execute("""
                insert into user
                (username,password_hash,role)
                values
                (?,?,?)
            """,(user.username,user.password_hash,user.role))
            con.commit()

    def get_user_by_username(self,username) -> User:
        with self.__create_connection() as con:
            cursor = con.execute("select * from user where username = ?",(username,))
            result = cursor.fetchone()
            if result is None:
                return None
            user = User()
            user.map(result)
            return user
