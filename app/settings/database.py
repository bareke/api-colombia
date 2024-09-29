from prisma import Prisma

database = Prisma()


async def connect_db() -> None:
    await database.connect()


async def disconnect_db() -> None:
    await database.disconnect()
