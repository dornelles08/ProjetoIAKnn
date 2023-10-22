from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from player_classifier.schemas import Classifier

from .functions.player_classifier import classifier

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/classifier', status_code=200, response_model=Classifier)
def player_classifier(data: str):
    result = classifier(data)
    return result
