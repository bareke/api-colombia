from fastapi import APIRouter

from app.example.schemas import ExampleBase
from app.example.services import ExampleService

router = APIRouter(
    prefix="/examples",
    tags=["examples"],
)

example_service = ExampleService()


@router.get("")
async def get_all_examples():
    return await example_service.find_all_example()


@router.get("/{id}")
async def get_example(id: int):
    return await example_service.find_example(id)


@router.post("")
async def create_example(example: ExampleBase):
    return await example_service.create_example(example)


@router.put("/{id}")
async def update_example(id: int, example: ExampleBase):
    return await example_service.update_example(id, example)


@router.delete("/{id}")
async def delete_example(id: int):
    return await example_service.delete_example(id)
