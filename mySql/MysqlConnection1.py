import mysql.connector


class MysqlConnection1:
    __connection = None
    __cursor = None
    __host = None
    __user = None
    __password = None
    __database = None

    def __init__(self, host1, user1, password1, database1):
        self.user = user1
        self.password = password1
        self.host = host1
        self.database = database1
        try:
            self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host,
                                                      database=self.database)

            if self.connection.is_connected():
                print('Connected to MySQL database')
                self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print('Reason Error Connect to Database is : ', e.msg, ' Error Code : ', e.errno, 'SqlStat : ', e.sqlstate)
            exit()

    def closeConnection(self, commit=True):
        if commit:
            self.connection.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params=params or ())

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

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

    @connection.setter
    def connection(self, value):
        self.__connection = value

    @cursor.setter
    def cursor(self, value):
        print('Value is :', value)
        self.__cursor = value

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
