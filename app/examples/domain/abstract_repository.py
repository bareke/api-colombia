from abc import ABC, abstractmethod


class ExampleAbstractRepository(ABC):

    @abstractmethod
    async def find(self):
        pass

    @abstractmethod
    async def find_all(self):
        pass

    @abstractmethod
    async def create(self):
        pass

    @abstractmethod
    async def delete(self):
        pass
