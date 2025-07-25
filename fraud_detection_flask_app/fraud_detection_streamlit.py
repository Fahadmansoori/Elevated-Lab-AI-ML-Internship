import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("xgboost_model.pkl")

st.set_page_config(page_title="Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection")

st.markdown("Enter or modify the transaction details below:")

# Generate example values (you can change or randomize these)
example_features = [-1.3598, -0.0728, 2.5363, 1.3782, -0.3383, 0.4624, 0.2396,
                    0.0987, 0.3638, 0.0908, -0.5516, -0.6178, -0.9913, -0.3112,
                    1.4681, -0.4704, 0.2079, 0.0258, 0.4030, 0.2514, 0.3784,
                    0.3429, 0.1233, 0.1209, -0.2080, 0.0287, 0.0950, 0.2443]

inputs = []
cols = st.columns(2)

for i in range(28):
    with cols[i % 2]:
        val = st.number_input(f"V{i+1}", value=float(example_features[i]), step=0.0001, format="%.6f")
        inputs.append(val)

amount = st.number_input("Normalized Amount", value=float(example_features[-1]), step=0.0001, format="%.6f")
inputs.append(amount)

if st.button("Predict"):
    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    proba = model.predict_proba(input_array)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraudulent Transaction Detected! (Probability: {proba:.2f})")
    else:
        st.success(f"✅ Transaction is Legitimate. (Probability: {proba:.2f})")
