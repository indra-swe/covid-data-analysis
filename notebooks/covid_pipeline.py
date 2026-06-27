import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================================
# DYNAMIC PATH DETERMINATION (ABSOLUTE FORCING)
# =====================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, 'outputs')

# =====================================================================
# SYSTEM INITIALIZATION & GRAPHICS THEME
# =====================================================================
def initialize_workspace():
    """Creates local directory safe paths and establishes visual plotting properties."""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (14, 7)
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 11
    print(f"🚀 Project workspace anchored absolutely at: {PROJECT_ROOT}")

# =====================================================================
# PHASE 4: EPIDEMIOLOGICAL DATA ENGINEERING PIPELINE
# =====================================================================
def run_epidemiological_pipeline():
    """Streams live global time series data from JHU CSSE repository and engineers metrics."""
    print("⏳ Streaming live global time series metrics from JHU CSSE servers...")
    
    # Official Johns Hopkins University URL streams for global confirmed cases and deaths
    CONFIRMED_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    DEATHS_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    
    try:
        raw_confirmed = pd.read_csv(CONFIRMED_URL)
        raw_deaths = pd.read_csv(DEATHS_URL)
    except Exception as e:
        raise ConnectionError(f"CRITICAL: Failed to stream live data from remote servers. Details: {e}")

    print("🧹 Meltdown & Restructuring Unstructured Wide Schemas...")
    # The raw JHU data uses dates as column headers (Wide Format). We melt them to long format for clean database analysis.
    id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long']
    
    df_conf = raw_confirmed.melt(id_vars=id_vars, var_name='Date', value_name='Confirmed')
    df_dead = raw_deaths.melt(id_vars=id_vars, var_name='Date', value_name='Deaths')
    
    # Merge datasets cleanly on tracking composite indexes
    merged_df = pd.merge(df_conf, df_dead, on=id_vars + ['Date'])
    
    # Drop structural geographic coordinates and group by distinct country levels
    merged_df['Date'] = pd.to_datetime(merged_df['Date'], format='%m/%d/%y')
    country_df = merged_df.groupby(['Country/Region', 'Date'])[['Confirmed', 'Deaths']].sum().reset_index()
    
    # Sort securely to guarantee chronological order for rolling math calculations
    country_df.sort_values(by=['Country/Region', 'Date'], inplace=True)
    
    print("⚙️ Engineering Advanced Epidemiological Transmission Indicators...")
    # 1. Calculate Daily Change Vectors (New Cases & New Deaths) per country group
    country_df['New_Cases'] = country_df.groupby('Country/Region')['Confirmed'].diff().fillna(0)
    country_df['New_Deaths'] = country_df.groupby('Country/Region')['Deaths'].diff().fillna(0)
    
    # Force negative reporting anomalies to zero
    country_df['New_Cases'] = country_df['New_Cases'].clip(lower=0)
    country_df['New_Deaths'] = country_df['New_Deaths'].clip(lower=0)
    
    # 2. Engineer Case Fatality Rate (CFR %)
    country_df['Case_Fatality_Rate'] = (country_df['Deaths'] / country_df['Confirmed'] * 100).fillna(0)
    
    # 3. Compute 7-Day Rolling Windows to eliminate structural weekend reporting drops
    country_df['Smoothed_New_Cases'] = country_df.groupby('Country/Region')['New_Cases'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
    
    # Export clean historical database sheet
    output_csv_path = os.path.join(DATA_DIR, "global_epidemiological_metrics.csv")
    country_df.to_csv(output_csv_path, index=False)
    print(f"✅ Preprocessing pipeline complete. Standardized health database saved to: {output_csv_path}")
    return country_df