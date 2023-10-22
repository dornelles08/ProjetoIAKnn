from pydantic import BaseModel


class Classifier(BaseModel):
    position: str
    overall: int
