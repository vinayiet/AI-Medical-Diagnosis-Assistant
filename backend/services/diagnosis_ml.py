import os
import joblib
from typing import List

# Get the absolute path to the model file based on this script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'diagnosis_model.pkl')
LABEL_ENCODER = os.path.join(BASE_DIR, 'label_encoder.pkl')
# Load the model using full path
model = joblib.load(MODEL_PATH)
encoder = joblib.load(LABEL_ENCODER)
print('Prediction model is loaded!')

SYMPTOM_COLS = [
    'fever', 'headache', 'nausea', 'vomiting', 'fatigue',
    'joint_pain', 'skin_rash', 'cough', 'weight_loss',
    'yellow_eyes'
]

def encode_symptoms(input_symptoms: List[str]) -> List[int]:
    return [1 if symptom in input_symptoms else 0 for symptom in SYMPTOM_COLS]

def predict_disease(symptoms: List[str]) -> str:
    features = encode_symptoms(symptoms)
    prediction = model.predict([features])
    disease_name = encoder.classes_[prediction[0]]
    return disease_name
