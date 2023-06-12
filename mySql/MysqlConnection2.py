import mysql.connector


class MysqlConnection2:
    def __init__(self, host, user, password, database, table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, values=None):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def select_query(self, columns, where_columns=None, where_values=None):
        select_columns = ', '.join(columns)
        query = f"SELECT {select_columns} FROM {self.table}"
        if where_columns and where_values:
            where_conditions = ' AND '.join([f"{col} = %s" for col in where_columns])
            query += f" WHERE {where_conditions}"
            self.execute_query(query, where_values)
        else:
            return self.select_query(query)

    def insert_row(self, values):
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {self.table} VALUES ({placeholders})"
        self.execute_query(query, values)

    def update_row(self, column, new_value, condition):
        query = f"UPDATE {self.table} SET {column} = %s WHERE {condition}"
        self.execute_query(query, (new_value,))

    def delete_row(self, condition):
        query = f"DELETE FROM {self.table} WHERE {condition}"
        self.execute_query(query)

    def execute_custom_query(self, query, values=None):
        self.execute_query(query, values)
