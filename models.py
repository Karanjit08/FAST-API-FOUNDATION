from pydantic import BaseModel


class MenuItem(BaseModel):
    id: int
    name: str
    price: int
    category: str
    description: str
    available: bool