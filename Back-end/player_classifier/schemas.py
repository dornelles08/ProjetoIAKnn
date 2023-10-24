from pydantic import BaseModel


class Classification(BaseModel):
    position: str
    overall: int
