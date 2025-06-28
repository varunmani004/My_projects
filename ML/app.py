import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Gold Price Predictor", layout="centered")

st.title("💰 Gold Price Prediction Web App")
st.write("Upload your CSV file with market indicators to predict gold price using different ML models.")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data Preview")
    st.write(df.head())

    st.subheader("Select a Model")
    model_choice = st.selectbox("Choose a model", ["Random Forest", "Lasso", "XGBoost"])

    # Load selected model
    if model_choice == "Random Forest":
        model = joblib.load(r"C:\Users\Varun\anaconda_projects\Python 3\random_forest.pkl")
    elif model_choice == "Lasso":
        model = joblib.load(r"C:\Users\Varun\anaconda_projects\Python 3\lasso_model.pkl")
    elif model_choice == "XGBoost":
        model = joblib.load(r"C:\Users\Varun\anaconda_projects\Python 3\xgboost_model.pkl")

    # Input features
    feature_cols = ['SPX', 'USO', 'SLV', 'EUR/USD']
    try:
        X_input = df[feature_cols]

        # Prediction
        prediction = model.predict(X_input)

        df['Predicted Gold Price'] = prediction
        st.subheader("📈 Predictions")
        st.write(df[['Predicted Gold Price']].head())

        st.line_chart(df[['Predicted Gold Price']])

        # Download predicted CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download predictions as CSV",
            data=csv,
            file_name='predicted_gold_prices.csv',
            mime='text/csv',
        )

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        st.info("Ensure the CSV has the following columns: SPX, USO, SLV, EUR/USD")
