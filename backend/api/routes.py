from fastapi import APIRouter
from models.schemas import SymptomInput, RecommendationOutput

from services.recommendation_system import get_recommendation
from services.diagnosis_ml import predict_disease

router = APIRouter()
print('Api is called !')
@router.post("/recommend", response_model=RecommendationOutput)
def recommend(symptom_input: SymptomInput):
    return get_recommendation(symptom_input.symptom)


@router.post("/predict", response_model=RecommendationOutput)
def predict_disease_route(symptom_input: SymptomInput):
    disease = predict_disease(symptom_input.symptoms)
    return {
        "matched_symptoms" : symptom_input.symptoms,
        "predicted_disease": disease
    }