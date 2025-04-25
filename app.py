import streamlit as st
import gdown
import pickle
import pandas as pd

# Set the page config to improve the look and feel
st.set_page_config(
    page_title="Income Prediction App",
    page_icon=":guardsman:",  # Add an emoji or an icon
    layout="wide",  # Layout style, 'wide' for a full-screen experience
)

# Load the model
with open('/Users/apiy_o/Desktop/Capstone_project.folder/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Custom Styling
st.markdown(""" <style> /* [Your existing CSS here] */ </style> """, unsafe_allow_html=True)

st.title("🎯 Income Prediction App")
st.subheader("Predict income category based on demographic and work-related attributes.")

st.markdown("Enter the details below and click **Predict** to see the income prediction:")

# Input fields
workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 
                                       'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
education_num = st.number_input("Education Number", min_value=0, max_value=16, value=10)
marital_status = st.selectbox("Marital Status", ['Married-civ-spouse', 'Divorced', 'Never-married', 
                                                  'Separated', 'Widowed', 'Married-spouse-absent'])
occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 
                                         'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 
                                         'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 
                                         'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
relationship = st.selectbox("Relationship", ['Wife', 'Own-child', 'Husband', 'Not-in-family', 
                                             'Other-relative', 'Unmarried'])
race = st.selectbox("Race", ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
sex = st.selectbox("Sex", ['Female', 'Male'])
capital_gain = st.number_input("Capital Gain", min_value=0, max_value=99999, value=0)
capital_loss = st.number_input("Capital Loss", min_value=0, max_value=99999, value=0)
native_country = st.selectbox("Native Country", ['United-States', 'Mexico', 'Philippines', 'Germany', 'Canada', 
                                                 'Puerto-Rico', 'India', 'Cuba', 'England', 'Jamaica', 'Others'])
has_capital_gain = st.selectbox("Has Capital Gain?", [0, 1])
has_capital_loss = st.selectbox("Has Capital Loss?", [0, 1])
age_group = st.selectbox("Age Group", ['Young', 'Middle-aged', 'Senior', 'Elderly'])
education_simplified = st.selectbox("Education Simplified", ['HS-grad', 'Some-college', 'Bachelors', 
                                                             'Masters', 'Assoc-acdm', 'Assoc-voc', 'Others'])
hours_category = st.selectbox("Hours Category", ['Part-time', 'Full-time', 'Over-time'])
fnlwgt = st.number_input("Final Weight", min_value=0, max_value=100000, value=0)

# Create a DataFrame from user inputs
input_data = pd.DataFrame({
        'workclass': [workclass],
        'education-num': [education_num],
        'marital-status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'sex': [sex],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'native-country': [native_country],
        'has_capital_gain': [has_capital_gain],
        'has_capital_loss': [has_capital_loss],
        'age_group': [age_group],
        'education_simplified': [education_simplified],
        'hours_category': [hours_category],
        'fnlwgt': [fnlwgt]
    })

# Button to trigger prediction
if st.button("Predict"):
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 1:
        st.success("Predicted Income: >50K")
    else:
        st.error("Predicted Income: <=50K")

# Footer
st.markdown("""
    <footer style="text-align: center; font-size: 14px; color: #606060;">
        Developed by <b>Apiyo Susan Kirimba</b> | Model Deployment via Streamlit
    </footer>
""", unsafe_allow_html=True)