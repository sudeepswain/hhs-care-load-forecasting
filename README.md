# Predictive Forecasting of Care Load & Placement Demand

## Project Overview
This project analyzes historical HHS Care population data and evaluates forecasting models for 7-day, 14-day, and 30-day horizons.

## Objectives
- Explore historical HHS Care population trends.
- Evaluate forecasting performance at three horizons.
- Compare a Persistence Baseline with a Random Forest model.
- Present findings for analytical review.

## Dataset
The source data contains recorded observations from January 12, 2023, to December 21, 2025. Reporting dates are irregular, so missing dates are not interpolated in the official forecasting analysis.

Only publish or redistribute the source dataset if its sharing terms permit it.

## Models
- Persistence Baseline
- Random Forest

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Lower values indicate better performance.

## Key Findings

| Forecast Horizon | Persistence MAE | Random Forest MAE |
|---|---:|---:|
| 7 days | 46.93 | 123.86 |
| 14 days | 82.92 | 140.36 |
| 30 days | 156.00 | 152.06 |

The Persistence Baseline performed better at 7 and 14 days. Random Forest showed a modest improvement at 30 days on the evaluated test data.

## Tools
Python, Pandas, NumPy, Scikit-learn, Google Colab, GitHub, and Streamlit.

## Limitations
Reporting dates are irregular, evaluation sample sizes vary by horizon, and results reflect the selected historical test periods. The models require further validation before operational use.
