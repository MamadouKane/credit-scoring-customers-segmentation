import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Function to calculate the credit score based on the FICO-like formula
def calculate_credit_score(payment_history, credit_utilization, num_credit_accounts, education_level, employment_status):
    score = (payment_history * 0.35) + (credit_utilization * 0.30) + (num_credit_accounts * 0.15) + (education_level * 0.10) + (employment_status * 0.10)
    return score

# Fonction pour afficher une jauge avec Plotly
def plot_gauge(credit_score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=credit_score,
        title={'text': "Credit Score"},
        gauge={'axis': {'range': [300, 850]},
               'steps': [
                   {'range': [300, 579], 'color': "red"},
                   {'range': [580, 669], 'color': "orange"},
                   {'range': [670, 739], 'color': "yellow"},
                   {'range': [740, 799], 'color': "lightgreen"},
                   {'range': [800, 850], 'color': "green"}],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': credit_score}}))

    st.plotly_chart(fig)

# ************************************** interface *********************************
st.set_page_config(page_title="Credit Score Calculator")

# Streamlit app
st.title("Credit Score Calculator")

# Input fields
payment_history = st.number_input("Payment History", value=1000, min_value=0)
credit_utilization = st.slider("Credit Utilization Ratio (in %)", 0, 100, 30)
num_credit_accounts = st.number_input("Number of Credit Accounts", min_value=0, value=10)
education_level = st.selectbox("Education Level", ['High School', 'Bachelor', 'Master', 'PhD'])
employment_status = st.selectbox("Employment Status", ['Unemployed', 'Employed', 'Self-Employed'])

# Mapping education and employment levels
education_level_mapping = {'High School': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
employment_status_mapping = {'Unemployed': 0, 'Employed': 1, 'Self-Employed': 2}

education_level = education_level_mapping[education_level]
employment_status = employment_status_mapping[employment_status]

# prediction button
if st.button("Calculate"):
    try:
        # Calculate credit score
        credit_score = calculate_credit_score(payment_history, credit_utilization, num_credit_accounts, education_level, employment_status)
        
        # display  score 
        st.write(f"Your credit score : {credit_score:.2f}")

        # display graph
        plot_gauge(credit_score)
    except ValueError:
        st.error("Erreur .")


