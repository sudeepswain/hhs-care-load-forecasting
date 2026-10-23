
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="HHS Care Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Predictive Forecasting of Care Load & Placement Demand")

st.markdown("""
Compare the Persistence Baseline and Random Forest models
for 7-day, 14-day, and 30-day forecasting horizons.
""")

# Load the final model results
file_path = Path("HHS_All_Horizons_Model_Comparison_Final.csv")

if not file_path.exists():
    st.error("The final model comparison CSV is missing from the repository.")
    st.stop()

results = pd.read_csv(file_path)

required_columns = ["Horizon", "Model", "Test_Rows", "MAE", "RMSE"]

if not all(column in results.columns for column in required_columns):
    st.error("The model comparison CSV does not contain the expected columns.")
    st.stop()

# KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Forecast Horizons", results["Horizon"].nunique())

with col2:
    st.metric("Models Evaluated", results["Model"].nunique())

with col3:
    st.metric("Total Model Results", len(results))

st.divider()

# Model comparison table
st.subheader("Model Comparison")
st.dataframe(results, use_container_width=True)

# MAE chart
st.subheader("Mean Absolute Error (MAE)")

mae_chart = results.pivot(
    index="Horizon",
    columns="Model",
    values="MAE"
)

st.bar_chart(mae_chart)

st.caption("Lower MAE indicates better average prediction accuracy.")

# RMSE chart
st.subheader("Root Mean Squared Error (RMSE)")

rmse_chart = results.pivot(
    index="Horizon",
    columns="Model",
    values="RMSE"
)

st.bar_chart(rmse_chart)

st.caption("Lower RMSE indicates better performance, with greater penalty for large errors.")

# Interpretation
st.subheader("Key Findings")

st.markdown("""
- The Persistence Baseline performed better than Random Forest at 7 days.
- The Persistence Baseline also performed better at 14 days.
- Random Forest showed a modest improvement at 30 days on the evaluated test data.

These findings apply to the selected historical test periods and do not guarantee future performance.
""")
