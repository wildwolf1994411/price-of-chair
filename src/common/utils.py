from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile("^[\w-]+@([\w-]+\.)+[\w-]+$") # check match pattern
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: the sha512 password from the login/register form
        :return: A sha512 -> pbkdf2_sha512 encryped password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        check the password the user matches that of database
        :param password: sha512 password
        :param hashed_password: pbkdf2_sha512 password
        :return:
        """
        return pbkdf2_sha512.verify(password, hashed_password)