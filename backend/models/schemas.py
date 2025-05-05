from pydantic import BaseModel
from typing import List, Union
print('schema is loaded')
class SymptomInput(BaseModel):
    symptoms: List[str] # this will take multiple input (multiple symptoms)

class RecommendationOutput(BaseModel):
    matched_symptom: List[str] 
    recommend_treatment: str

class DiseasePredictionOutput(BaseModel):
    matched_symptoms: List[str]
    predicted_disease: Union[int, str]