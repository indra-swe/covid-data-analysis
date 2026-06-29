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

