class PlayerAccount:
    def __init__(self, email, username, password, db):
        """Create number, name, balance, db(database) and db.register(database register) in __init__."""
        self.email = email
        self.username = username
        self.password = password
        self.db = db
        db.register(self)

    """
       @property decorator wraps setter methods to create a property, 
       which can be directly accessed as if it was a public attribute
       """
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        self.__db = db

    def __repr__(self):
        """
        The object representation can be changed by implementing the __repr__ method,which is required to a string.
        """
        return f'Account(username="{self.username}", password="{self.password}", Game="{self.db.game}")'