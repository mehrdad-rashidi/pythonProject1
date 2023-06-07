import mysql.connector


class MysqlConnection1:
    __connection = None
    __cursor = None

    def __init__(self, host, user, password, database):
        try:
            self.__connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
            if self.__connection.is_connected():
                print('Connected to MySQL database')
                self.__cursor = self.__connection.cursor()
        except mysql.connector.Error as e:
            print('Reason Error Connect to Database is : ', e)
            exit()

    def closeConnection(self, commit=True):
        if commit:
            self.__connection.commit()
        self.__connection.close()

    def execute(self, sql, params=None):
        self.__cursor.execute(sql, params=params or ())

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

    @connection.setter
    def connection(self, value):
        self.__connection = value

    @cursor.setter
    def cursor(self, value):
        self.__cursor = value