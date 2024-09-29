from prisma import Prisma
from app.examples.application.validations import ExampleCreate, ExampleUpdate
from app.examples.domain.abstract_repository import ExampleAbstractRepository


class ExampleRepository(ExampleAbstractRepository):
    def __init__(self, persistence: Prisma):
        self.persistence = persistence

    async def find(self, example_id: int) -> dict:
        """Get register in the persistence"""

        result = await self.persistence.example.find_first(
            where={"id": example_id}
        )

        return result

    async def find_all(self) -> list[dict]:
        """Get all registers in the persistence"""

        result = await self.persistence.example.find_many()

        return result

    async def create(self, example: ExampleCreate) -> dict:
        """Save register in the persistence"""

        result = await self.persistence.example.create(
            data=vars(example)
        )

        return result

    async def update(self, example_id: int, example: ExampleUpdate) -> dict:
        """Update register in the persistence"""

        result = await self.persistence.example.update(
            where={"id": example_id},
            data=vars(example),
        )

        return result

    async def delete(self, example_id: int) -> bool:
        """Delete register in the persistence"""

        result = await self.persistence.example.delete(
            where={"id": example_id}
        )

        return result
