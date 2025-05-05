from pydantic import BaseModel

print('schema is loaded')
class SymptomInput(BaseModel):
    symptom: str

class RecommendationOutput(BaseModel):
    matched_symptom: str
    recommend_treatment: str