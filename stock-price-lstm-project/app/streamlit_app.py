import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price Predictor")

df = pd.read_csv('data/stock_data.csv', index_col='Date', parse_dates=True)

st.subheader("Stock Closing Price")
st.line_chart(df['Close'])
