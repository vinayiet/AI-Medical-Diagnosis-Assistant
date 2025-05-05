import pandas as pd 
from sentence_transformers import SentenceTransformer, util

print('model is loading...')
model = SentenceTransformer('all-MiniLM-L6-v2')
print('model has loaded !')
data = {
    "symptom": ["fever", "cough", "cold", "headache"],
    "treatment": ["paracetamol", "benadryl", "cetirizine", "aspirin"]
}
df = pd.DataFrame(data)
symptoms_list = df["symptom"].tolist()
treatments_list = df["treatment"].tolist()
symptom_embdedding  = model.encode(symptoms_list, convert_to_tensor= True)

print('get recommendation function is called !')
def get_recommendation(user_input: str):
    input_embedding = model.encode(user_input, convert_to_tensor= True)
    scores = util.pytorch_cos_sim(input_embedding, symptom_embdedding)[0]
    top_idx = scores.argmax().item()
    return {
        "matched_symptom" : symptoms_list[top_idx],
        "recommend_treatment" : treatments_list[top_idx]
    }