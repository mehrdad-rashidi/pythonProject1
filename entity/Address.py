from orm2.Entity import Entity


class Address(Entity):
    @Entity.column('INT')
    @Entity.primary_key
    def id(self) -> int:
        pass

    @Entity.column('VARCHAR(100)')
    def street(self) -> str:
        pass

    @Entity.column('VARCHAR(50)')
    def city(self) -> str:
        pass

    @Entity.column('VARCHAR(20)')
    def zip_code(self) -> str:
        pass
