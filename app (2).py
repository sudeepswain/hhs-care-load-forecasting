import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HHS Care Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load final model comparison results
results = pd.read_csv(
    "HHS_All_Horizons_Model_Comparison_Final.csv"
)

# Load historical dataset
data = pd.read_csv(
    "HHS_Unaccompanied_Alien_Children_Program.csv"
)

# Clean column names
data.columns = data.columns.str.strip()

# Prepare historical data
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

target = "Children in HHS Care"
data[target] = pd.to_numeric(data[target], errors="coerce")

data = (
    data.dropna(subset=["Date", target])
        .drop_duplicates(subset=["Date"])
        .sort_values("Date")
)

# Dashboard title
st.title("📊 Predictive Forecasting of Care Load & Placement Demand")

st.markdown("""
Explore historical HHS Care population data and compare forecasting
performance across 7-day, 14-day, and 30-day horizons.
""")

# KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Forecast Horizons", results["Horizon"].nunique())

with col2:
    st.metric("Models Evaluated", results["Model"].nunique())

with col3:
    st.metric("Historical Records", len(data))

st.divider()

# Historical trend
st.subheader("Historical HHS Care Population")

st.line_chart(
    data.set_index("Date")[target],
    y_label="Children in HHS Care"
)

st.caption(
    "The chart displays recorded observations. Missing reporting dates "
    "are not filled or interpolated."
)

# Model comparison table
st.subheader("Forecast Model Comparison")
st.dataframe(results, use_container_width=True)

# MAE comparison
st.subheader("Mean Absolute Error (MAE)")
mae_chart = results.pivot(
    index="Horizon",
    columns="Model",
    values="MAE"
)
st.bar_chart(mae_chart)
st.caption("Lower MAE indicates better average prediction accuracy.")

# RMSE comparison
st.subheader("Root Mean Squared Error (RMSE)")
rmse_chart = results.pivot(
    index="Horizon",
    columns="Model",
    values="RMSE"
)
st.bar_chart(rmse_chart)
st.caption("Lower RMSE is better and penalizes larger prediction errors.")
