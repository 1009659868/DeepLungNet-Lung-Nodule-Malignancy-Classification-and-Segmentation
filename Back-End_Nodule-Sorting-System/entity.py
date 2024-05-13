

class User:
    u_id=None,
    u_name=None,
    u_password=None,
    u_nickname=None,
    u_email=None

    def __init__(self, u_id, u_name, u_password, u_nickname, u_email):
        self._u_id = u_id
        self._u_name = u_name
        self._u_password = u_password
        self._u_nickname = u_nickname
        self._u_email = u_email

    @property
    def u_id(self):
        return self._u_id

    @u_id.setter
    def u_id(self, value):
        self._u_id = value

    @property
    def u_name(self):
        return self._u_name

    @u_name.setter
    def u_name(self, value):
        self._u_name = value

    @property
    def u_password(self):
        return self._u_password

    @u_password.setter
    def u_password(self, value):
        self._u_password = value

    @property
    def u_nickname(self):
        return self._u_nickname

    @u_nickname.setter
    def u_nickname(self, value):
        self._u_nickname = value

    @property
    def u_email(self):
        return self._u_email

    @u_email.setter
    def u_email(self, value):
        self._u_email = value

    def __str__(self):
        return f"User ID: {self._u_id}, Name: {self._u_name}, Nickname: {self._u_nickname}, Email: {self._u_email}"