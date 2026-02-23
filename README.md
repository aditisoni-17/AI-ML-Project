# 🏦 AI Credit Risk Scoring System

A professional machine learning application designed to predict the probability of credit delinquency within the next two years. This project uses traditional Random Forest classification to provide high-accuracy risk assessments through an interactive web-based dashboard.

## 🚀 Overview
Financial institutions face significant challenges in assessing the creditworthiness of applicants. This system leverages demographic and financial profile data to calculate a real-time risk score, helping lenders make data-driven decisions.

### Key Features
*   **Predictive Scoring:** Real-time default probability estimation.
*   **Risk Classification:** Binary classification (Low Risk vs. High Risk) using balanced forest weights.
*   **Model Insights:** Transparent visualization of feature importance (e.g., Credit Utilization, Age).
*   **Interactive UI:** Clean, responsive dashboard built with Streamlit.

---

## 🛠️ Tech Stack
*   **Language:** Python 3.9+
*   **ML Framework:** Scikit-Learn
*   **Data Processing:** Pandas, NumPy
*   **Web Dashboard:** Streamlit
*   **Visualizations:** Matplotlib
*   **Formatting:** LaTeX (Project Report)

---

## 📦 Project Structure
```text
├── app/
│   └── streamlit_app.py      # Main web application code
├── src/
│   ├── preprocess.py        # Data cleaning and pipeline logic
│   ├── train_model.py       # Model training and evaluation script
│   └── explain_model.py     # Feature importance calculation
├── models/
│   └── risk_model.pkl       # Serialized Random Forest model
├── data/
│   └── Credit Risk...csv    # Benchmark dataset
├── report.tex               # Professional LaTeX source
└── README.md                # Project documentation
```

---

## ⚙️ Setup & Installation
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/aditisoni-17/AI-ML-Project.git
    cd AI-ML-Project
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    # OR install manually
    pip install streamlit pandas scikit-learn matplotlib joblib
    ```
3.  **Run the Application:**
    ```bash
    streamlit run app/streamlit_app.py
    ```

---

## 📊 Performance
The model was trained on a benchmark credit dataset and evaluated on unseen test data:
*   **Accuracy:** ~93.5%
*   **ROC-AUC:** ~0.95
*   **Metric Strategy:** Used balanced class weights to ensure high Recall even with imbalanced default data.

---

## 🖋️ Author
**Aditi**
