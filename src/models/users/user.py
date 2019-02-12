import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
import src.models.users.constants as UserContants
from src.models.alerts.alert import Alert


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an email /password is valid or not
        check email existes and that password associated to that email is correct
        :param email: The user's email str
        :param password: A sha512 hased password
        :return: True if vaild Flase otherwise
        """
        user_data = Database.find_one(UserContants.COLLECTION, {"email": email})
        if user_data is None:
            raise UserErrors.UserNotExistsError("User doesn't exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Password incorrect")

        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers user using email and password
        The password already comes hashed as sha-512
        :param email:  user's email
        :param password:
        :return:
        """
        user_data = Database.find_one(UserContants.COLLECTION, {"email": email})
        if user_data is not None:
            # tell user they are already register
            raise UserErrors.UserAlreadyRegisteredError("The email you used already exist")
        if not Utils.email_is_valid(email):
            # tell user that their e-mail is not constructed properly
            raise UserErrors.InvalidEmailError("The email does not have right format")
        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert(UserContants.COLLECTION, self.json())

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one(UserContants.COLLECTION, {'email': email}))

    def get_alerts(self):
        return Alert.find_by_user_email(self.email)