from pydantic import BaseModel
from typing import List
print('schema is loaded')
class SymptomInput(BaseModel):
    symptom: List[str] # this will take multiple input (multiple symptoms)

class RecommendationOutput(BaseModel):
    matched_symptom: List[str] 
    recommend_treatment: str