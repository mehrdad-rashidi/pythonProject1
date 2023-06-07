import mysql.connector


class MysqlConnection:

    def __init__(self, host, user, password, database):
        self.__connection = None
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def mysqlConnection(self, host, user, password, database):
        try:
            __connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
            if __connection.is_connected():
                print('Connected to MySQL database')
                return self.__connection
        except mysql.connector.Error as e:
            print('Reason Error Connect to Database is : ', e)
            exit()

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def database(self):
        return self.__database

    @property
    def connection(self):
        return self.connection

    @host.setter
    def host(self, value):
        self.__host = value

    @user.setter
    def user(self, value):
        self.__user = value

    @password.setter
    def password(self, value):
        self.__password = value

    @database.setter
    def database(self, value):
        self.__database = value

    @connection.setter
    def connection(self, value):
        self.connection = value
