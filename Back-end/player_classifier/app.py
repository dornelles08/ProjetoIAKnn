from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from player_classifier.schemas import Classification

from .functions.player_classifier import classifier

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@app.get('/classifier', status_code=200, response_model=Classification)
def player_classifier(data: str):
    result = classifier(data)
    return result
