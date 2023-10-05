import configparser

config = configparser.RawConfigParser()
config.read(".//confingurations/config.ini")

class ReadConfig():

    """
    This class contains methods used to read from config.ini file
    """

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_user_email():
        email = config.get('common info', 'user_email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
    

