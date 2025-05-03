# 📊 Income Prediction Capstone Project

This project focuses on predicting whether an individual's income exceeds $50K annually using demographic and employment-related attributes from the U.S. Census data. The model aims to support poverty identification and inform policy targeting.

---

## 📁 Dataset

- **Source**: [UCI Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- **Size**: 32,561 records × 15 features
- **Target Variable**: `income` (`<=50K` or `>50K`)

### 🔑 Features:
- `age`, `workclass`, `education`, `education-num`, `marital-status`,  
  `occupation`, `relationship`, `race`, `sex`, `capital-gain`,  
  `capital-loss`, `hours-per-week`, `native-country`, `fnlwgt`

---

## 🧪 Project Objectives

1. Predict whether an individual's income exceeds $50K/year.
2. Identify key factors influencing income level.
3. Support policy-making and financial assistance targeting.

---

## ⚙️ Workflow

1. **Data Cleaning & Preprocessing**
   - Handling missing values
   - Encoding categorical features
   - Feature scaling and transformation

2. **Exploratory Data Analysis (EDA)**
   - Visualizations: income vs age, education, gender, race
   - Correlation heatmaps

3. **Modeling**
   - Models: Logistic Regression, Random Forest, Gradient Boosting
   - Final Model: Voting Classifier
   - Evaluation: Accuracy, Precision, Recall, F1-score, Confusion Matrix

4. **📈 Model Evaluation**
   - Used classification metrics to evaluate model performance:
   - Accuracy
   - Precision
   - Recall
   - F1-score
   - Confusion Matrix
   - ROC-AUC Score

5. **🔧 Decision Threshold Optimization**
- Due to class imbalance, optimizing for accuracy alone was insufficient. Instead, we focused on improving precision and F1-score for class 1 (income > 50K).

- ✅ Final Optimized Threshold: ~0.24
At this threshold, the model achieved:

- Metric	Class 0 (<=50K)	Class 1 (>50K)
- Precision	0.82	0.61
- Recall	0.93	0.36
- F1-score	0.87	0.46

- Significant improvement in precision for class 1 (from 0.41 to 0.61)

- F1-score for class 1 reached its best value after tuning the threshold

6. **✅ Final Model Summary**
- Model: Voting Classifier

- Threshold: 0.2378

- Optimized for F1-score of income >50K

- Performance: Balanced trade-off between false positives and false negatives

- Overall Accuracy: 79%

7. **Model Persistence**
   - Models saved with `joblib` (`*.pkl`)

8. **🚀 Future Work**
- Integrate model into a real-time API using Flask or FastAPI

---

## 🚀 Deployment

⚠️ Model files (`*.pkl`) are over 100MB and are excluded from the GitHub repo.

📌 Download models from [Google Drive Link] https://drive.google.com/file/d/126mLKinyfA_VpdohQWfe6nCb-9O25Pg_/view?usp=drive_link

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- Jupyter Notebook
- Gdown
- Pickle
- Git & GitHub
- Scikit-learn
- Streamlit (For Deployment)


---


## 📬 Contact

**Apiyo Susan Kirimba**  
📧 apiyosusan62@gmail.com  
📞 0701086625 | 0719451654  
🔗 [LinkedIn](https://www.linkedin.com/in/apiyosusan) | [GitHub](https://github.com/apiyOsusan)

---
