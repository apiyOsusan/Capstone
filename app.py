import streamlit as st
import pandas as pd
import joblib
st.markdown(
    """
    <style>
    .colorful-title {
        font-size: 36px !important;
        color: #FFA07A; /* Light Salmon */
        text-shadow: 2px 2px #FFD700; /* Gold shadow */
        font-family: 'Arial Black', sans-serif;
    }
    .prediction-box-positive {
        background-color: #98FB98; /* Pale Green */
        color: #006400; /* Dark Green */
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        font-weight: bold;
    }
    .prediction-box-negative {
        background-color: #F08080; /* Light Coral */
        color: #8B0000; /* Dark Red */
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load model
model = joblib.load("adult_income_voting_model.pkl")
# Load the encoded training data
trained_data = joblib.load('X_train.pkl')

# Column order used during training
with open('columns.txt', 'r') as f:
    train_columns = f.read().splitlines()


st.markdown('<h1 class="colorful-title">✨ Income Predictor Deluxe ✨</h1>', unsafe_allow_html=True)

def user_input():
    age = st.number_input("Age", min_value=0, max_value=100, value=25, key="age")
    education_num = st.number_input("Education Number", min_value=1, max_value=16, value=10, key="education_num")
    hours_per_week = st.number_input("Hours per Week", min_value=1, max_value=100, value=40, key="hours_per_week")
    workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'], key="workclass")
    education = st.selectbox("Education Level", options=['Bachelors', 'Masters', 'PhD'], key="education")
    marital_status = st.selectbox("Marital Status", options=['Married-AF-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed'], key="marital_status")
    occupation = st.selectbox("Occupation", options=['Adm-clerical', 'Armed-Forces' , 'Craft-repair', 'Exec-managerial', 'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct', 'Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv', 'Sales', 'Tech-support', 'Transport-moving'], key="occupation")
    relationship = st.selectbox("Relationship", options=['Not-in-family', 'Other-relative', 'Own-child', 'Unmarried', 'Wife'], key="relationship")
    race = st.selectbox("Race", options=['Asian-Pac-Islander', 'Black', 'White', 'Other'], key="race")
    sex = st.selectbox("Sex", ['Male', 'Female'], key="sex")
    native_country = st.selectbox("Native Country", options=['Cambodia','Canada', 'China', 'Columbia', 'Cuba', 'Dominican-Republic', 'Ecuador', 'El-Salvador', 'England', 'France', 'Germany', 'Greece', 'Guatemala', 'Haiti', 'Holand-Netherlands', 'Honduras', 'Hong', 'Hungary', 'India', 'Iran', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Laos', 'Mexico', 'Nicaragua', 'Outlying-US(Guam-USVI-etc)','Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Scotland', 'South', 'Taiwan', 'Thailand', 'Trinadad&Tobago', 'United-States', 'Vietnam', 'Yugoslavia'], key="native_country")

    data = {
        'age': age,
        'education-num': education_num,
        'hours-per-week': hours_per_week,
        'workclass': workclass,
        'education': education,
        'marital-status': marital_status,
        'occupation': occupation,
        'relationship': relationship,
        'race': race,
        'sex': sex,
        'native-country': native_country
    }
    return pd.DataFrame([data])

st.subheader("Enter User Features:")
input_df = user_input()

if st.button('Predict Income'):
    # Prediction logic (moved inside the if block)
    input_encoded = pd.get_dummies(input_df)
    input_final = input_encoded.reindex(columns=train_columns, fill_value=0)
    prediction = model.predict(input_final)[0]

    st.subheader("Prediction:")
    if prediction == 1:
        st.markdown('<div class="prediction-box-positive">💰 Prediction: > $50K 💰</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="prediction-box-negative">📉 Prediction: <= $50K 📉</div>', unsafe_allow_html=True)