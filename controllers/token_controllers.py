import configparser


class TokenService:
    @staticmethod
    def store_token(token):
        config = configparser.ConfigParser()
        config['AUTH'] = {'token': token}

        with open('../config.ini', 'w') as configfile:
            config.write(configfile)

    @staticmethod
    def read_token():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['AUTH']['token']
