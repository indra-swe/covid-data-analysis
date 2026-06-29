# 🧬 Epidemiological Intelligence: Automated Time-Series Engineering & Global Outbreak Tracking

## 📌 Strategic Overview
This repository contains an automated epidemiological data pipeline and visualization web console that tracks and models global viral outbreaks using live, streaming public health records. Transforming row-level cumulative datasets into actionable tracking indices, the framework calculates transmission waves, models regional case fatality weights, and builds an interactive workspace for clinical analysts.

### 🎯 Key Analytical Objectives Realized
* **Live Ingestion Architecture:** Configured an automated streaming layout that pulls raw daily global data directly from the Johns Hopkins University (JHU) CSSE repository.
* **Schema Schema Restructuring:** Melted wide time-series tracking schemes containing hundreds of date columns into a standardized database format.
* **Transmission Velocity Quantifications:** Extracted first-order differentials to separate new daily transmission scales from historic cumulative totals.
* **Signal Smoothing Profiles:** Formulated 7-day moving window averages to eliminate weekend drops in public health data reporting.

---

## 🛠 Workspace Mapping & Architecture
```text
├── data/
│   └── global_epidemiological_metrics.csv # Automated post-pipeline metrics dataset
├── notebooks/
│   ├── covid_pipeline.py                  # Core data cleaner & static visual report engine
│   └── app.py                             # Interactive dual-axis Streamlit app console interface
├── outputs/
│   ├── global_volume_rankings.png         # Chart: Pareto tracking of country-level distributions
│   └── global_transmission_velocity.png   # Chart: Dual-axis tracking of cumulative growth waves
└── requirements.txt                       # Explicit system dependency specifications