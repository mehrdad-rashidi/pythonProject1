class SelectQuery:
    __tableName = None
    __schema = None

    def __init__(self) -> None:
        super().__init__()

    def selectQueryBuilder(self, schema, tableName, columnParam, whereParams):
        self.schema = schema
        self.tableName = tableName
        whereClause = ''
        columns = ''
        # column = ''
        # selectQuery = ''
        if whereParams:
            for key, value in whereParams.items():
                whereClause = whereClause + ', ' + key + ' = ', value
        if columnParam:
            for column in columnParam:
                if columns is '':
                    columns = columns + ', ' + column
                else:
                    columns = columns + ', ' + column

        selectQuery = 'select ' + columns + ' from ' + self.schema + self.tableName + ' where ' + whereClause
        return selectQuery

    @property
    def tableName(self):
        return self.__tableName

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        self.__schema = value

    @tableName.setter
    def tableName(self, value):
        self.__tableName = value
