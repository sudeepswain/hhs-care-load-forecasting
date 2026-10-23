# Predictive Forecasting of Care Load & Placement Demand

## Project Objective
Analyze historical HHS Care population data and evaluate forecasting models for 7-day, 14-day, and 30-day horizons.

## Data and Methodology
The dataset contains 720 recorded observations from January 12, 2023, to December 21, 2025. There are 355 missing calendar dates in the reporting period. The official forecasting models preserve the recorded observations without interpolating missing dates. Historical lag and rolling statistical features are used, with chronological training and test splits.

## Key Findings
- 7-day: Persistence Baseline MAE = 46.93; Random Forest MAE = 123.86.
- 14-day: Persistence Baseline MAE = 82.92; Random Forest MAE = 140.36.
- 30-day: Persistence Baseline MAE = 156.00; Random Forest MAE = 152.06.

The Persistence Baseline performed better at 7 and 14 days. Random Forest showed a small improvement at 30 days.

## Limitations
Reporting dates are irregular, test sample sizes vary by horizon, and results reflect the selected historical test periods. Further validation is required before operational use.

## Conclusion
The Persistence Baseline is the strongest evaluated model at 7 and 14 days. Random Forest provides only a modest improvement at 30 days.

## Tools
Python, Pandas, NumPy, Scikit-learn, Google Colab, GitHub, and Streamlit.
