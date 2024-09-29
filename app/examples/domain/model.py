from datetime import datetime


class Example:
    def __init__(self, id: int, name: str, last_name : str, created_at: datetime, updated_at: datetime) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.created_at = created_at
        self.updated_at = updated_at
