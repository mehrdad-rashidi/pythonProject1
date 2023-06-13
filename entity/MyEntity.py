import orm2.Entity
from orm2.Entity import Entity


# Define an entity class
class MyEntity(Entity):
    def __init__(self):
        super().__init__()

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



