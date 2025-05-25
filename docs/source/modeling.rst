
---

# 📘 `modeling.rst`

```rst
Modeling
========

We trained multiple models to predict customer churn:

Models Used:
------------

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost Classifier

Model Evaluation:
-----------------

Used the following metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

Best Model:
-----------

**XGBoost Classifier** gave the highest F1-score and ROC-AUC.

Top Features Identified:
------------------------

- Contract
- tenure
- MonthlyCharges
- OnlineSecurity
- TechSupport

```python
from xgboost import XGBClassifier

model = XGBClassifier()
model.fit(X_train, y_train)
