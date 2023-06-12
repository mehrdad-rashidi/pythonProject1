import mysql.connector


# class MyTableEntity:
class MysqlConnection3:
    def __init__(self, **kwargs):
        self.table = 'my_table'  # Replace with your actual table name
        self.column_properties = self._get_table_columns()
        for column_name, column_type in self.column_properties.items():
            setattr(self, column_name, kwargs.get(column_name))

    def _get_table_columns(self):
        column_properties = {}
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='your_database'
        )
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {self.table}")
        columns = cursor.fetchall()
        for column in columns:
            column_name = column[0]
            column_type = column[1]
            column_properties[column_name] = column_type
        cursor.close()
        connection.close()
        return column_properties

    def save(self):
        column_names = ', '.join(self.column_properties.keys())
        placeholders = ', '.join(['%s'] * len(self.column_properties))
        query = f"INSERT INTO {self.table} ({column_names}) VALUES ({placeholders})"
        values = [getattr(self, column) for column in self.column_properties.keys()]
        # Execute the query and save the entity to the database

    @staticmethod
    def load(id):
        entity = MysqlConnection3()
        # Load the entity from the database using the provided id
        # Populate the entity properties based on the retrieved data
        return entity

    def update(self):
        set_columns = ', '.join([f"{column} = %s" for column in self.column_properties.keys()])
        query = f"UPDATE {self.table} SET {set_columns} WHERE id = %s"
        values = [getattr(self, column) for column in self.column_properties.keys()]
        values.append(self.id)
        # Execute the query to update the entity in the database

    def delete(self):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        values = (self.id,)
        # Execute the query to delete the entity from the database
