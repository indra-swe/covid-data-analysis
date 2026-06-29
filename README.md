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
```

## ⚙️ Quantitative Epidemiological Formulations
Raw reporting sequences only provide total historical sums. This architecture processes raw data into standard epidemiological indicators:

* **Daily Outbreak Velocity Vector ($\Delta C_t$):** Extracts the daily change rate to isolate current transmission velocity profiles:
  $$\Delta C_t = C_t - C_{t-1}$$

* **Case Fatality Rate Benchmark ($CFR_t$):** Calculates viral severity and measures localized healthcare system stress as a percentage ratio metric:
  $$\text{CFR}_t = \left( \frac{\text{Deaths}_t}{\text{Confirmed}_t} \right) \times 100$$

* **Smoothed Transmission Signals ($\text{SMA}_7$):** Calculates a 7-day rolling arithmetic mean to smooth out weekly reporting discrepancies and reveal true transmission waves:
  $$\text{Smoothed Cases} = \frac{1}{7} \sum_{i=0}^{6} \Delta C_{t-i}$$

---

## 📊 Strategic Business Observations
1. **The Reporting Drop Anomaly:** Plotting raw daily changes discloses a regular 7-day drop cycle that corresponds to drop-offs in weekend laboratory data processing. This makes rolling window averages necessary to prevent misinterpreting reporting drops as a drop in transmission velocity.
2. **CFR Divergence Drivers:** Cross-analyzing total volumes alongside the Case Fatality Rate reveals significant performance differences between regional healthcare systems. Higher spikes in localized CFR scores provide an analytical indicator that alerts operations managers to structural system bottlenecks or shifts in viral severity.

---

## 🚀 Environment Quickstart & Execution

### 1. Initialize System Dependencies
```bash
git clone [https://github.com/indra-swe/covid-data-analysis.git](https://github.com/indra-swe/covid-data-analysis.git)
cd covid-data-analysis
pip install -r requirements.txt
```
### 2. Trigger Data Retrieval & Core Analytics
```bash
python notebooks/covid_pipeline.py
```
### 3. Launch the Deployed Portal Console
```bash
streamlit run notebooks/app.py
```
