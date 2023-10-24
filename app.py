import streamlit as st
import numpy as np
import pandas as pd
import pickle
import xgboost

# title
st.title('CREDIT RISK DEFAULT PREDICTION')

# loading pickle files
ms = pickle.load(open('ms.pkl','rb'))
xg = pickle.load(open('xg_model.pkl','rb'))
X_train = pickle.load(open('X_train.pkl','rb'))
le_default_on_file = pickle.load(open('le_default_on_file.pkl','rb'))
le_loan_grade = pickle.load(open('le_loan_grade.pkl','rb'))
le_loan_intent = pickle.load(open('le_loan_intent.pkl','rb'))
le_ownership = pickle.load(open('le_ownership.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

# taking input from user

st.write('Please enter below customer details')

age = st.number_input('Age',min_value=20, max_value=150, step=1, format="%d")
income = st.number_input('Income',step=1, format="%d")
ownership = st.selectbox('Home Ownership Type', sorted(df['person_home_ownership'].unique()))
ownership = le_ownership.transform([ownership])
emp_length = st.number_input('Employment Length', max_value = 150, step=1)
loan_intent = st.selectbox('Loan Intent', sorted(df['loan_intent'].unique()))
loan_intent = le_loan_intent.transform([loan_intent])
loan_grade = st.selectbox('Loan Intent', sorted(df['loan_grade'].unique()))
loan_grade = le_loan_grade.transform([loan_grade])
loan_amount = st.number_input('Loan_Amount',step=1,value=20000)
loan_int_rate = st.number_input('Loan Interest Rate',step=0.1)
loan_percent_income = income/loan_amount
previous_defaulter = st.selectbox('Previous Defaulter', df['cb_person_default_on_file'].unique())
previous_defaulter = le_default_on_file.transform([previous_defaulter])
credit_history = st.number_input('Credit History Length', min_value=0, max_value= 35, step=1)

# prediction

result = xg.predict([[age,income,ownership[0],emp_length,loan_intent[0],loan_grade[0],loan_amount,
                     loan_int_rate, loan_percent_income,previous_defaulter[0],credit_history]])

# creating a button

button_style = """
        <style>
        div.stButton > button:first-child {
            background-color: green !important;
            color: black !important;
        }
        </style>
    """

# Display the button with the custom style
st.markdown(button_style, unsafe_allow_html=True)

# creating a condition application when the button is pressed:

if st.button("Predict"):

    if result == 1:
        st.write('<span style="font-size: 30px;color: red;">Defaulter</span>', unsafe_allow_html=True)
    else:
        st.write('<span style="font-size: 30px;color: lightgreen;">Non Defaulter</span>', unsafe_allow_html=True)

