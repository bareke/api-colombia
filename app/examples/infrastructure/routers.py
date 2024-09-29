from fastapi import APIRouter

from app.examples.application.validations import ExampleCreate, ExampleUpdate
from app.examples.application.service import ExampleService
from app.examples.infrastructure.repository import ExampleRepository
from app.settings.database import database

router = APIRouter(
    prefix="/examples",
    tags=["examples"],
)

repository = ExampleRepository(database)
example_service = ExampleService(repository)


@router.get("")
async def get_all_examples():
    return await example_service.find_all_examples()


@router.get("/{id}")
async def get_example(id: int):
    return await example_service.find_example(id)


@router.post("")
async def create_example(example: ExampleCreate):
    return await example_service.create_example(example)


@router.put("/{id}")
async def update_example(id: int, example: ExampleUpdate):
    return await example_service.update_example(id, example)


@router.delete("/{id}")
async def delete_example(id: int):
    return await example_service.delete_example(id)
