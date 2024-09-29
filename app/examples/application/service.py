from app.examples.application.validations import ExampleCreate, ExampleUpdate
from app.examples.domain.model import Example
from app.examples.domain.abstract_repository import ExampleAbstractRepository


class ExampleService:
    def __init__(self, repository: ExampleAbstractRepository):
        self.repository = repository

    async def find_example(self, example_id: int):
        """Get register in the persistence"""

        result = await self.repository.find(example_id)

        return result

    async def find_all_examples(self):
        """Get all registers in the persistence"""

        result = await self.repository.find_all()

        return result

    async def create_example(self, example: ExampleCreate):
        """Save register in the persistence"""

        result = await self.repository.create(example)

        return result

    async def update_example(self, example_id: int, example: ExampleUpdate):
        """Update register in the persistence"""

        result = await self.repository.update(example_id, example)

        return result

    async def delete_example(self, example_id: int):
        """Delete register in the persistence"""

        result = await self.repository.delete(example_id)

        return result
