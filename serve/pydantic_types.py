from pydantic import BaseModel
from typing import Dict
from fastapi import FastAPI

class InputIris(BaseModel):
    petal_lenght: float
    petal_width: float

class OutputIris(BaseModel):
    results:Dict[str, float]

