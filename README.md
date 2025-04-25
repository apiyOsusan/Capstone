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

4. **Model Persistence**
   - Models saved with `joblib` (`*.pkl`)

---

## 📈 Results

- **Best model**: Voting Classifier
- **Evaluation metrics**: High F1-score and recall
- **Most influential features**:
  - `education-num`, `hours-per-week`, `occupation`, `capital-gain`, `age`

---

## 🚀 Deployment

⚠️ Model files (`*.pkl`) are over 100MB and are excluded from the GitHub repo.

📌 Download models from [Google Drive Link] (provide once hosted).

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- Jupyter Notebook
- Joblib
- Git & GitHub

---

## 📎 File Structure


---

## 📬 Contact

**Apiyo Susan Kirimba**  
📧 apiyosusan62@gmail.com  
📞 0701086625 | 0719451654  
🔗 [LinkedIn](https://www.linkedin.com/in/apiyosusan) | [GitHub](https://github.com/apiyOsusan)

---
