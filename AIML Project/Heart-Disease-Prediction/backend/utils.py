import os

import joblib
from sklearn.dummy import DummyClassifier

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "heart_disease_model.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "model",
    "feature_columns.pkl"
)

DEFAULT_FEATURE_COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]


def _create_placeholder_model():
    X = [[0] * len(DEFAULT_FEATURE_COLUMNS) for _ in range(4)]
    y = [0, 1, 0, 1]
    model = DummyClassifier(strategy="prior")
    model.fit(X, y)
    return model


def _load_pickle(path, default):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            return joblib.load(path)
        except Exception:
            return default
    return default


model = _load_pickle(MODEL_PATH, _create_placeholder_model())
feature_columns = _load_pickle(FEATURE_PATH, DEFAULT_FEATURE_COLUMNS)

if not isinstance(feature_columns, list) or not feature_columns:
    feature_columns = DEFAULT_FEATURE_COLUMNS


def get_model():
    return model


def get_feature_columns():
    return feature_columns