from fastapi import APIRouter
from models.schemas import SymptomInput, RecommendationOutput

from services.recommendation_system import get_recommendation


router = APIRouter()
print('Api is called !')
@router.post("/recommend", response_model=RecommendationOutput)
def recommend(symptom_input: SymptomInput):
    return get_recommendation(symptom_input.symptom)


