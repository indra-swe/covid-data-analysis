import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure page environment layout
st.set_page_config(page_title="Epidemiological Intelligence Portal", page_icon="🧬", layout="wide")

# Custom clinical dark slate visual style overrides
st.markdown("""
    <style>
    .main { background-color: #0F1219; color: #F1F3F5; }
    h1, h3, h4 { color: #FF4A4A; font-family: 'Arial', sans-serif; }
    .stSelectbox label { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 Epidemiological Outbreak Tracking Portal")
st.write("Stream dynamic global public health vectors, calculate transmission velocity waves, and track case fatality benchmarks.")

# =====================================================================
# DATA RETRIEVAL INITIALIZATION
# =====================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), 'data', 'global_epidemiological_metrics.csv')

@st.cache_data
def load_workspace_data():
    if not os.path.exists(DATA_FILE_PATH):
        st.error("❌ Data Storage Asset Missing. Run 'notebooks/covid_pipeline.py' first to initialize data records.")
        st.stop()
    data = pd.read_csv(DATA_FILE_PATH)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

df = load_workspace_data()

# =====================================================================
# SIDEBAR GEOGRAPHIC CONTROL PANELS
# =====================================================================
st.sidebar.header("🕹️ Geographic Filters")
selected_country = st.sidebar.selectbox("Select Target Country / Region:", sorted(df['Country/Region'].unique()), index=sorted(df['Country/Region'].unique()).index('US') if 'US' in df['Country/Region'].unique() else 0)

# Filter dataset to match active geographic selections
country_filtered = df[df['Country/Region'] == selected_country].sort_values(by='Date')

# =====================================================================
# INTERACTIVE DATA MATRIX SUMMARY DASHBOARD
# =====================================================================
latest_record = country_filtered.iloc[-1]
latest_date_str = latest_record['Date'].strftime('%Y-%m-%d')

st.markdown(f"### 📍 Regional Summary Profile: {selected_country} (Snapshot up to {latest_date_str})")

# KPI Summary Matrix Metrics Rows
col1, col2, col3, col4 = st.columns(4)
col1.metric("Cumulative Confirmed Cases", f"{int(latest_record['Confirmed']):,}")
col2.metric("Total Documented Casualties", f"{int(latest_record['Deaths']):,}")
col3.metric("Case Fatality Rate (CFR)", f"{float(latest_record['Case_Fatality_Rate']):.2f}%")
col4.metric("Active Daily Wave (7-Day Avg)", f"{int(latest_record['Smoothed_New_Cases']):,}")

# --- VISUAL GRAPH PANEL A: TRANSMISSION SCALING VELOCITY OVER TIME ---
st.markdown("### 📈 Transmission Wave Velocity vs. Cumulative Growth Scaling")
fig_wave = go.Figure()

# Plot Cumulative Line on Primary Y-Axis
fig_wave.add_trace(go.Scatter(x=country_filtered['Date'], y=country_filtered['Confirmed'], name='Cumulative Confirmed', line=dict(color='#0073e6', width=2.5)))

# Plot Daily Volume Bars on Secondary Y-Axis
fig_wave.add_trace(go.Bar(x=country_filtered['Date'], y=country_filtered['New_Cases'], name='New Daily Registrations', marker_color='#ff9900', opacity=0.4, yaxis='y2'))

# Apply advanced dual axis mapping parameters layout styles
fig_wave.update_layout(
    template="plotly_dark",
    paper_bgcolor='#0F1219',
    plot_bgcolor='#0F1219',
    height=500,
    yaxis=dict(title="Cumulative Cases Volume"),
    yaxis2=dict(title="New Daily Transmission Scale", overlaying='y', side='right'),
    legend=dict(x=0.02, y=0.98)
)
st.plotly_chart(fig_wave, use_container_width=True)

# --- VISUAL GRAPH PANEL B: COMPARATIVE REGIONAL ANALYSIS ---
st.markdown("### 🗺️ Global Proportional Comparison Matrix")
latest_global_snapshot = df[df['Date'] == df['Date'].max()].sort_values(by='Confirmed', ascending=False).head(20)

fig_compare = px.bar(
    latest_global_snapshot, 
    x='Confirmed', 
    y='Country/Region', 
    orientation='h',
    title="Top 20 Global Vectors Ranked by Volumetric Case Thresholds",
    labels={'Confirmed':'Confirmed Scale Volume', 'Country/Region':'Country / Region'},
    color='Case_Fatality_Rate',
    color_continuous_scale='Reds'
)
fig_compare.update_layout(template="plotly_dark", paper_bgcolor='#0F1219', plot_bgcolor='#0F1219')
st.plotly_chart(fig_compare, use_container_width=True)
