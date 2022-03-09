# here we create utilies file to read common data from ini file and use in our test case
import configparser
config = configparser.RawConfigParser
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getuserEmail():
        username = config.get('common info', 'userEmail')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password





