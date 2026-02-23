# 🏦 Intelligent Credit Risk Scoring & Agentic Lending Decision Support System

An end-to-end AI-powered fintech platform designed to predict borrower credit risk. This system introduces a two-phase architecture: a quantitative Machine Learning pipeline for rapid prediction of default probabilities, and a qualitative Agentic AI Assistant for formulating professional, explainable lending recommendations.

## 🚀 Overview
Traditional underwriting processes are often rigid and lack transparency. This platform leverages a Random Forest classifier combined with robust preprocessing to accurately classify high-risk and low-risk candidates while prioritizing critical metrics such as Recall and ROC-AUC.

### Key Features
*   **Two-Phase Architecture:** Quantitative ML pipeline + Qualitative Agentic Assistant.
*   **Explainable AI (XAI):** Translates mathematical feature importance into transparent insights.
*   **Robust Preprocessing:** Automated median imputation and feature scaling.
*   **Interactive UI:** Clean, responsive dashboard built with Streamlit.

---

## 🛠️ Tech Stack
*   **ML Core:** Scikit-Learn (Random Forest)
*   **Data Processing:** Pandas, NumPy
*   **Web Dashboard:** Streamlit
*   **Visualizations:** Matplotlib
*   **Report Formatting:** LaTeX (IEEE Conference Style)

---

## 📦 Project Structure
```text
├── app/
│   └── streamlit_app.py      # Main web application code
├── src/
│   ├── preprocess.py        # Data cleaning and pipeline logic
│   └── train_model.py       # Model training and evaluation
├── models/
│   └── risk_model.pkl       # Serialized Random Forest model
├── notebooks/
│   └── eda.ipynb            # Exploratory Data Analysis
├── data/
│   └── Credit Risk...csv    # Benchmark dataset
├── report.tex               # IEEE Style LaTeX source
├── requirements.txt         # Dependency variants
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
