from fastapi import FastAPI
from pydantic import BaseModel
from model import recommend

app = FastAPI()

@app.get("/recommend")
def predict(select_your_movie:str):
    recommendation = recommend(select_your_movie)
    # Create a dictionary with "recommendations" as the key and the list as the value
    return (recommendation)

