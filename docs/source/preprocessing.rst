Preprocessing
=============

Raw data must be cleaned and transformed before modeling. Below are the steps followed:

1. **Missing Values**:
   - TotalCharges column had blank strings; these were converted to NaN and filled.

2. **Data Type Conversion**:
   - Converted TotalCharges to numeric values.
   - Encoded categorical variables using Label Encoding and One-Hot Encoding.

3. **Feature Engineering**:
   - Created new features like `tenure group` (short, medium, long).

4. **Scaling**:
   - Scaled numerical features using StandardScaler or MinMaxScaler.

5. **Handling Imbalance**:
   - Used SMOTE to balance the dataset because churn classes were imbalanced (more No than Yes).

```python
from imblearn.over_sampling import SMOTE
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)
