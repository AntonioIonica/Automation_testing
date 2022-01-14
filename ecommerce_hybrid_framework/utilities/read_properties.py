import configparser

config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')


class ReadConfig:
    #without creating any object
    @staticmethod
    def get_url():
        url = config.get('url and login info', 'URL')
        return url

    @staticmethod
    def get_admin_email():
        admin_email = config.get('url and login info', 'email_info')
        return admin_email

    @staticmethod
    def get_admin_pwd():
        admin_pwd = config.get('url and login info', 'pwd_info')
        return admin_pwd
