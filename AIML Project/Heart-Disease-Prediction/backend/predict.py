import pandas as pd

from backend.utils import (
    get_model,
    get_feature_columns
)

model = get_model()
feature_columns = get_feature_columns()


def predict_heart_disease(data_dict):

    df = pd.DataFrame([data_dict])

    df = df[feature_columns]

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    confidence = max(probability)

    return {
        "prediction": int(prediction),
        "confidence": round(float(confidence) * 100, 2)
    }