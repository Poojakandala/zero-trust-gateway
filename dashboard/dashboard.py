import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

st.set_page_config(page_title="FinTech Risk Shield", layout="wide")

# FIX 1: Corrected 'unsafe_allow_html'
def apply_style(is_attack):
    if is_attack:
        st.markdown("""<style> .stApp { background-color: #4b0000; color: white; } </style>""", unsafe_allow_html=True)
    else:
        st.markdown("""<style> .stApp { background-color: #0e1117; color: white; } </style>""", unsafe_allow_html=True)

# FIX 2: Handle missing Database/Table gracefully
db_path = os.path.join('gateway', 'audit.db')
df = pd.DataFrame(columns=['timestamp', 'client_ip', 'risk_score', 'status'])

if os.path.exists(db_path):
    try:
        conn = sqlite3.connect(db_path, check_same_thread=False)
        df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 50", conn)
    except:
        pass # Table might not be created yet

# Determine if under attack
is_under_attack = False
if not df.empty:
    is_under_attack = any(df.head(5)['risk_score'] > 0.8)

apply_style(is_under_attack)

if is_under_attack:
    st.error("⚠️ CRITICAL SECURITY BREACH DETECTED: AUTO-BLOCKING ENABLED")
else:
    st.success("✅ System Status: Secure - Zero Trust Policy Active")

# Dashboard UI
c1, c2, c3 = st.columns(3)
c1.metric("Total Requests", len(df))
c2.metric("Current Risk Level", f"{df['risk_score'].iloc[0]:.2f}" if not df.empty else "0.00")
c3.metric("Status", "LOCKED" if is_under_attack else "ACTIVE")

if not df.empty:
    fig = px.area(df, x='timestamp', y='risk_score', title="Live AI Risk Analysis")
    fig.update_traces(line_color='#ff4b4b' if is_under_attack else '#00ffcc')
    st.plotly_chart(fig, use_container_width=True)
    st.table(df.head(10))
else:
    st.info("📡 Waiting for traffic... Please run simulate_traffic.py")
