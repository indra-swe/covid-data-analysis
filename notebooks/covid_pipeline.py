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

# =====================================================================
# PHASE 5: STATIC REPORT GENERATION
# =====================================================================
def generate_reporting_graphics(df):
    """Generates high-resolution production charts visualizing viral trajectories."""
    print("⏳ Rendering global health analytical graphics panels...")
    
    # --- Chart 1: Top 10 Heavily Impacted Countries Portfolio ---
    latest_date = df['Date'].max()
    latest_snapshot = df[df['Date'] == latest_date]
    top_countries = latest_snapshot.sort_values(by='Confirmed', ascending=False).head(10)
    
    plt.figure()
    sns.barplot(x='Confirmed', y='Country/Region', data=top_countries, palette='Reds_r')
    plt.title(f"Global Scale: Top 10 Heavily Impacted Countries by Cumulative Volume ({latest_date.strftime('%Y-%m-%d')})", fontweight='bold')
    plt.xlabel('Cumulative Confirmed Cases (Millions)')
    plt.ylabel('Country / Region')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUTS_DIR, "global_volume_rankings.png"), dpi=300)
    plt.close()

    # --- Chart 2: Global Progression Velocity (Aggregate Wave) ---
    global_time = df.groupby('Date')[['Confirmed', 'Deaths', 'Smoothed_New_Cases']].sum().reset_index()
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    ax1.plot(global_time['Date'], global_time['Confirmed'] / 1e6, color='#0073e6', linewidth=2, label='Cumulative Confirmed')
    ax2.fill_between(global_time['Date'], 0, global_time['Smoothed_New_Cases'], color='#ff9900', alpha=0.3, label='7-Day Smooth New Cases')
    
    ax1.set_xlabel('Timeline Horizon')
    ax1.set_ylabel('Total Cumulative Cases (Millions)', color='#0073e6')
    ax2.set_ylabel('New Smoothed Daily Additions', color='#ff9900')
    plt.title("Global Outbreak Velocity Scale & Wave Distribution Profile", fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUTS_DIR, "global_transmission_velocity.png"), dpi=300)
    plt.close()

    print(f"✅ Pipeline graphics written directly inside: {OUTPUTS_DIR}")

# =====================================================================
# SYSTEM MAIN ENTRY POINT
# =====================================================================
if __name__ == "__main__":
    initialize_workspace()
    processed_health_data = run_epidemiological_pipeline()
    generate_reporting_graphics(processed_health_data)
    print("🎉 Complete epidemiological preprocessing pipeline executed flawlessly!")