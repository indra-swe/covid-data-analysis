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
