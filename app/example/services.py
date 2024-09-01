from app.example.schemas import ExampleBase
from app.settings.database import database


class ExampleService:
    def __init__(self):
        self.repository = database

    async def find_example(self, example_id: int):
        """Get register in the persistence"""

        result = await self.repository.example.find_first(where={"id": example_id})

        return result

    async def find_all_example(self):
        """Get all registers in the persistence"""

        result = await self.repository.example.find_many()

        return result

    async def create_example(self, example: ExampleBase):
        """Save register in the persistence"""

        result = await self.repository.example.create(data=vars(example))

        return result

    async def update_example(self, example_id: int, example: ExampleBase):
        """Update register in the persistence"""

        result = await self.repository.example.update(
            where={"id": example_id},
            data=vars(example),
        )

        return result

    async def delete_example(self, example_id: int):
        """Delete register in the persistence"""

        result = await self.repository.example.delete(where={"id": example_id})

        return result
