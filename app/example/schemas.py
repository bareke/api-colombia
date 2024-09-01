from pydantic import BaseModel as BaseSchema


class ExampleBase(BaseSchema):
    name: str
    last_name: str
