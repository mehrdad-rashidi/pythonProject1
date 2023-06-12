class ObjectRelationalMapper:
    def __init__(self, database):
        self.database = database

    def save(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        values = tuple(data.values())
        self.database.execute_query(query, values)

    def find_all(self, table):
        query = f"SELECT * FROM {table}"
        result = self.database.execute_query(query)
        return result

    def find_by_conditions(self, table, conditions):
        query = f"SELECT * FROM {table} WHERE {conditions}"
        result = self.database.execute_query(query)
        return result

    def update(self, table, data, conditions):
        set_columns = ', '.join([f"{column} = %s" for column in data.keys()])
        query = f"UPDATE {table} SET {set_columns} WHERE {conditions}"
        values = tuple(data.values())
        self.database.execute_query(query, values)

    def delete(self, table, conditions):
        query = f"DELETE FROM {table} WHERE {conditions}"
        self.database.execute_query(query)
