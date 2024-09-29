from pydantic import BaseModel as BaseSchema

from app.examples.domain.model import Example


class ExampleCreate(BaseSchema):
    name: str
    last_name: str


class ExampleUpdate(BaseSchema):
    name: str = None
    last_name: str = None
