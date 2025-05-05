from fastapi import APIRouter
from models.schemas import SymptomInput, RecommendationOutput
from services.recommendation_system import get_recommendation
from services.diagnosis_ml import predict_disease
from models.schemas import DiseasePredictionOutput
router = APIRouter()
print('Api is called !')
@router.post("/recommend", response_model=RecommendationOutput)
def recommend(symptom_input: SymptomInput):
    return get_recommendation(symptom_input.symptom)

@router.post("/predict", response_model=DiseasePredictionOutput)
def predict_disease_route(symptom_input: SymptomInput):
    disease = predict_disease(symptom_input.symptoms)  # returns an integer like 7
    return {
        "matched_symptoms": symptom_input.symptoms,
        "predicted_disease": disease
    }
