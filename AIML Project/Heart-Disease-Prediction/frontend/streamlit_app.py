import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.predict import predict_heart_disease

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ Heart Disease Prediction System")

st.markdown(
"""
Provide patient information below and click
**Predict**.
"""
)

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        1,
        120,
        50
    )

    sex = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [0,1,2,3]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        80,
        250,
        120
    )

    chol = st.number_input(
        "Cholesterol",
        100,
        700,
        200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar >120",
        [0,1]
    )

    restecg = st.selectbox(
        "Rest ECG",
        [0,1,2]
    )

with col2:

    thalach = st.number_input(
        "Max Heart Rate",
        50,
        250,
        150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0,1]
    )

    oldpeak = st.number_input(
        "Old Peak",
        0.0,
        10.0,
        1.0
    )

    slope = st.selectbox(
        "Slope",
        [0,1,2]
    )

    ca = st.selectbox(
        "Major Vessels",
        [0,1,2,3,4]
    )

    thal = st.selectbox(
        "Thal",
        [0,1,2,3]
    )

if st.button("Predict Heart Disease"):

    data = {

        "age": age,
        "sex": 1 if sex=="Male" else 0,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    result = predict_heart_disease(data)

    if result["prediction"] == 1:

        st.error(
            f"""
            Heart Disease Detected

            Confidence:
            {result['confidence']}%
            """
        )

    else:

        st.success(
            f"""
            No Heart Disease Detected

            Confidence:
            {result['confidence']}%
            """
        )