class ORM:
    def __init__(self, database):
        self.database = database

    def save(self, entity):
        table_name = entity.__class__.__name__
        columns = ', '.join(entity.__dict__.keys())
        placeholders = ', '.join(['%s'] * len(entity.__dict__))
        values = tuple(entity.__dict__.values())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.database.execute_query(query, values)

    def save_all(self, entities):
        if not entities:
            return

        table_name = entities[0].__class__.__name__
        columns = ', '.join(entities[0].__dict__.keys())
        placeholders = ', '.join(['%s'] * len(entities[0].__dict__))

        values = []
        for entity in entities:
            values.append(tuple(entity.__dict__.values()))

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.database.execute_query(query, values)

    def load_all(self, entity_class):
        table_name = entity_class.__name__
        query = f"SELECT * FROM {table_name}"
        result = self.database.execute_query(query)
        entities = []
        for row in result:
            entity = entity_class()
            for i, column_name in enumerate(entity.__dict__.keys()):
                setattr(entity, column_name, row[i])
            entities.append(entity)
        return entities

    def load_by_id(self, entity_class, entity_id):
        table_name = entity_class.__name__
        query = f"SELECT * FROM {table_name} WHERE id = %s"
        result = self.database.execute_query(query, (entity_id,))
        if result:
            entity = entity_class()
            for i, column_name in enumerate(entity.__dict__.keys()):
                setattr(entity, column_name, result[0][i])
            return entity
        return None

    def update(self, entity):
        table_name = entity.__class__.__name__
        set_columns = ', '.join([f"{column} = %s" for column in entity.__dict__.keys()])
        values = tuple(entity.__dict__.values())

        query = f"UPDATE {table_name} SET {set_columns} WHERE id = %s"
        self.database.execute_query(query, values + (entity.id,))

    def delete(self, entity):
        table_name = entity.__class__.__name__
        query = f"DELETE FROM {table_name} WHERE id = %s"
        self.database.execute_query(query, (entity.id,))
