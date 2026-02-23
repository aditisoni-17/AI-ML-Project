# 🧠 Viva Voce Cheat Sheet

Prepare these answers to demonstrate ownership and deep technical knowledge (Section 6 of Rubric).

### Q: Why did you choose Random Forest over other models?
**A:** "Random Forest is an ensemble method. Unlike a single decision tree, it reduces overfitting by averaging multiple trees (bagging). It is particularly good for financial data because it captures non-linear trends and automatically calculates feature importance."

### Q: How did you handle the imbalanced nature of credit default data?
**A:** "In credit risk, 'Good' applicants far outnumber 'Bad' ones. I used the `class_weight='balanced'` parameter in Scikit-Learn. This penalizes the model more for misclassifying a default, ensuring high Recall (catching more risk)."

### Q: Can you explain the Data Flow (Architecture)?
**A:** "The data enters through the Streamlit UI, passes through the preprocessing pipeline (where income and dependents are imputed), and is then fed into the serialized `joblib` model. The model outputs both a class and a probability score."

### Q: What is 'ROC-AUC' and why is it important here?
**A:** "ROC-AUC measures how well the model distinguishes between low-risk and high-risk applicants, regardless of the classification threshold. A score of 0.95 shows our model is excellent at ranking risk."

### Q: Which feature was most important?
**A:** "**Credit Utilization** was the top predictor. This represents how much of a person's credit limit they are using. High utilization is a strong signal of financial stress."

---
### 🛠️ Common Tools used:
*   **Pandas:** Data manipulation and cleaning.
*   **Scikit-Learn:** Model training and metrics.
*   **Joblib:** Saving and loading the trained model.
*   **Streamlit:** Building the interactive frontend.
*   **LaTeX:** Creating the professional academic report.
