import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="FinTech Risk Shield", layout="wide")

# Custom CSS for the "Panic" Mode
def apply_style(is_attack):
    if is_attack:
        st.markdown(
            """<style> .stApp { background-color: #4b0000; color: white; } </style>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """<style> .stApp { background-color: #0e1117; color: white; } </style>""",
            unsafe_allow_html=True
        )

# Data Fetching
conn = sqlite3.connect('gateway/audit.db', check_same_thread=False)
c = conn.cursor()

# Auto-create table if not exists
c.execute("""
CREATE TABLE IF NOT EXISTS logs (
    timestamp TEXT,
    client_ip TEXT,
    risk_score REAL,
    status TEXT
)
""")
conn.commit()

df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 50", conn)

# Detect if under attack
is_under_attack = False
if not df.empty:
    is_under_attack = any(df.head(5)['risk_score'] > 0.8)

apply_style(is_under_attack)

if is_under_attack:
    st.error("⚠️ CRITICAL SECURITY BREACH DETECTED: AUTO-BLOCKING ENABLED")
else:
    st.success("✅ System Status: Secure - Zero Trust Policy Active")

# Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Total Requests", len(df))
c2.metric("Current Risk Level", f"{df['risk_score'].iloc[0]:.2f}" if not df.empty else "0")
c3.metric("Status", "LOCKED" if is_under_attack else "ACTIVE")

# Risk Chart
if not df.empty:
    fig = px.area(df, x='timestamp', y='risk_score', title="Live AI Risk Analysis")
    fig.update_traces(line_color='#ff4b4b' if is_under_attack else '#00ffcc')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No traffic yet. Waiting for API requests...")

# Log Table
st.subheader("Real-time Audit Trail")
st.dataframe(df, use_container_width=True)
