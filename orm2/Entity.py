class Entity:
    """
    The base class for defining entity classes that represent database tables.

    Attributes:
        columns (dict): A dictionary mapping column names to their corresponding data types.
        foreign_keys (dict): A dictionary mapping column names to the tables they reference as foreign keys.
        relationships (dict): A dictionary mapping column names to the tables they have a relationship with.
        primary_key_column (str): The name of the primary key column.

    Methods:
        column: A decorator to define a column of the entity.
        primary_key: A decorator to define the primary key column of the entity.
        foreign_key: A decorator to define a foreign key column of the entity.
        relationship: A decorator to define a relationship between the entity and another table.
        __annotations__: Returns the annotations dictionary representing the entity's columns.

    Example Usage:
        class MyEntity(Entity):
            @Entity.column()
            @Entity.primary_key
            def id(self) -> int:
                pass

            @Entity.column('VARCHAR(50)')
            def name(self) -> str:
                pass

            @Entity.column()
            @Entity.foreign_key(referenced_table='Address')
            def address_id(self) -> int:
                pass

            @Entity.relationship(related_table='Address')
            def address(self) -> str:
                pass
    """

    columns = {}
    foreign_keys = {}
    relationships = {}
    primary_key_column = None

    @classmethod
    def column(cls, data_type=None):
        """
        A decorator to define a column of the entity.

        Args:
            data_type (str): The data type of the column. Default is None.

        Returns:
            func: The decorated function.

        Example Usage:
            @Entity.column('VARCHAR(50)')
            def name(self) -> str:
                pass
        """

        def decorator(func):
            column_name = func.__name__
            cls.columns[column_name] = data_type
            return func

        return decorator

    @classmethod
    def primary_key(cls, primary_key_func=None):
        """
        A decorator to define the primary key column of the entity.

        Args:
            primary_key_func (function): The function representing the primary key column. Default is None.

        Returns:
            function or str: The decorated function if a primary_key_func is provided, else the primary key column name.

        Example Usage:
            @Entity.column()
            @Entity.primary_key
            def id(self) -> int:
                pass
        """
        if primary_key_func:
            cls.primary_key_column = primary_key_func.__name__
            return primary_key_func
        else:
            return cls.primary_key_column

    @classmethod
    def foreign_key(cls, referenced_table):
        """
        A decorator to define a foreign key column of the entity.

        Args:
            referenced_table (str): The name of the table that the column references.

        Returns:
            function: The decorated function.

        Example Usage:
            @Entity.column()
            @Entity.foreign_key(referenced_table='Address')
            def address_id(self) -> int:
                pass
        """

        def decorator(func):
            column_name = func.__name__
            cls.foreign_keys[column_name] = referenced_table
            return func

        return decorator

    @classmethod
    def relationship(cls, related_table):
        """
        A decorator to define a relationship between the entity and another table.

        Args:
            related_table (str): The name of the table that the entity has a relationship with.

        Returns:
            function: The decorated function.

        Example Usage:
            @Entity.relationship(related_table='Address')
            def address(self) -> str:
                pass
        """

        def decorator(func):
            column_name = func.__name__
            cls.relationships[column_name] = related_table
            return func

        return decorator

    @classmethod
    def __annotations__(cls):
        """
        Returns the annotations dictionary representing the entity's columns.

        Returns:
            dict: The annotations' dictionary.

        Example Usage:
            annotations = MyEntity.__annotations__()

                The @Entity.relationship(related_table='Address')
        decorator in the MyEntity class is used to define a relationship
        between the MyEntity table and the Address table.

        When you decorate a method in MyEntity class with @Entity.relationship,
        it signifies that there is a relationship between
        the MyEntity table and the Address table based on the specified column.

        Here's a breakdown of what the @Entity.relationship decorator does:

        1. It decorates a method in the MyEntity class that represents a column related to the Address table.
        2. The related_table argument is provided to the decorator, specifying the name of the table that
        MyEntity has a relationship with (in this case, 'Address').
        3. The decorator stores this relationship information in the relationships dictionary of the Entity base class,
        associating the column name with the related table.

        By using the @Entity.relationship decorator, you can indicate and establish relationships between different
        tables in your entity model. This can be useful for performing joins and accessing
        related data from other tables when querying the database.

        For example, in your MyEntity class, the decorated address method represents a
        relationship between the MyEntity table and the Address table. This relationship implies that there is a
        connection between records in the MyEntity table and records in the Address table,
        and you can utilize this relationship for querying and retrieving related data.

        Keep in mind that the implementation of how the relationship is used in queries or other
        operations would depend on your specific ORM or database library.

        Let me know if you need any further clarification or have any other questions!
        """
        annotations = {}
        for column_name, data_type in cls.columns.items():
            if column_name == cls.primary_key_column:
                annotations[column_name] = f"{data_type} PRIMARY KEY"
            elif column_name in cls.foreign_keys:
                referenced_table = cls.foreign_keys[column_name]
                annotations[column_name] = f"{data_type} REFERENCES {referenced_table}"
            else:
                annotations[column_name] = data_type
        return annotations


