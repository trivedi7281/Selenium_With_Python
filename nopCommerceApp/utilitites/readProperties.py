import configparser

config = configparser.RawConfigParser()
config.read('/Users/mack/PycharmProjects/nopCommerceApp/Configurations/config.ini')


class readConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        email = config.get('common_info', 'username')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get('common_info', 'password')
        return password
