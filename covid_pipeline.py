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
