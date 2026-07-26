# Heart Disease Prediction

This project contains a starter structure for a heart disease prediction app.

## Structure
- backend/: prediction logic
- frontend/: Streamlit interface
- model/: trained model artifacts
- app.py: Flask entry point

# Heart Disease Prediction

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run frontend/streamlit_app.py
```

Run test:

```bash
python test_model.py
```

Project Structure:

```
Heart-Disease-Prediction
│
├── backend
├── frontend
├── model
├── static
├── templates
├── app.py
├── requirements.txt
└── README.md
```