import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page setup
st.set_page_config(page_title="💰 Gold Price Predictor", layout="centered")
st.title("💰 Gold Price Prediction Web App")
st.write("Upload your CSV file or enter values manually to predict the gold price using ML models.")

# Model selection
st.subheader("⚙️ Select a Model")
model_choice = st.selectbox(
    "Choose a model", ["Random Forest", "Lasso", "XGBoost"])

# Load model
try:
    if model_choice == "Random Forest":
        model = joblib.load(
            r"ML/random_forest.pkl")
    elif model_choice == "Lasso":
        model = joblib.load(
            r"C:\pross\git Repo\My_projects\ML\lasso_model.pkl")
    elif model_choice == "XGBoost":
        model = joblib.load(
            r"C:\pross\git Repo\My_projects\ML\xgboost_model.pkl")
except FileNotFoundError:
    st.error("⚠️ Model file not found! Please make sure the model `.pkl` files are in the same directory.")
    st.stop()

# Upload section
st.subheader("📤 Upload a CSV File (Optional)")
uploaded_file = st.file_uploader(
    "Upload CSV with columns: SPX, USO, SLV, EUR/USD", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("✅ Uploaded Data Preview:")
else:
    st.info("No CSV uploaded. Using default sample data.")
    try:
        df = pd.read_csv(
            r"C:\pross\git Repo\My_projects\ML\gold_price_data.csv")
    except:
        st.error("⚠️ sample_gold_data.csv not found.")
        st.stop()

# Show data preview
st.write(df.head())

# Predict from file data
try:
    feature_cols = ['SPX', 'USO', 'SLV', 'EUR/USD']
    X_input = df[feature_cols]
    predictions = model.predict(X_input)
    df['Predicted Gold Price'] = predictions

    st.subheader("📈 Predictions from File")
    st.write(df[['Predicted Gold Price']].head())
    st.line_chart(df[['Predicted Gold Price']])

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Predictions as CSV", data=csv,
                       file_name='predicted_gold_prices.csv', mime='text/csv')

except Exception as e:
    st.error(f"⚠️ Prediction error from file: {e}")
    st.info("Make sure your CSV has the required columns: SPX, USO, SLV, EUR/USD")

# Manual input
st.markdown("---")
st.subheader("🔢 Or Enter Values Manually")

spx = st.number_input("SPX (S&P 500 Index)", value=1400.0)
uso = st.number_input("USO (Oil Price)", value=12.0)
slv = st.number_input("SLV (Silver Price)", value=16.0)
eurusd = st.number_input("EUR/USD Exchange Rate", value=1.2)

if st.button("🎯 Predict Manually"):
    input_data = pd.DataFrame([[spx, uso, slv, eurusd]], columns=feature_cols)
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Predicted Gold Price: {prediction:.2f}")
    except Exception as e:
        st.error(f"⚠️ Manual prediction error: {e}")

# Sample CSV download
try:
    with open(r"C:\pross\git Repo\My_projects\ML\gold_price_data.csv", "rb") as file:
        st.download_button("📥 Download Sample CSV", file,
                           file_name="sample_gold_data.csv", mime="text/csv")
except:
    pass
