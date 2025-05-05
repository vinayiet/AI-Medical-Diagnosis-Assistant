import joblib

model = joblib.load('../notebooks/diagnosis_model.pkl')

SYMPTOM_COLS = [
    'fever', 'headache', 'nausea', 'vomiting', 'fatigue',
    'joint_pain', 'skin_rash', 'cough', 'weight_loss',
    'yellow_eyes'
]

def encode_symptoms(input_symptoms: list[str]) -> list[int]:
    """
    Encode the list of the symptoms into a binary feature vector.
    """
    return [1 if symptom in input_symptoms else 0 for symptom in SYMPTOM_COLS]

def predict_disease(symptoms: list[str]) -> str:
    """
    Predict disease based on encoded symptoms
    
    """
    features = encode_symptoms(symptoms)
    prediction = model.predict([features])
    return prediction[0]
