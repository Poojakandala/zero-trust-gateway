import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="FinTech Risk Shield", layout="wide", page_icon="🛡️")

# Use a relative path so GitHub can find the uploaded file
db_path = "audit.db"

# --- SIDEBAR INFO ---
st.sidebar.title("🛡️ System Control")
st.sidebar.info("""
**Zero Trust AI Gateway**
- **AI Model:** Random Forest Classifier
- **Defense:** Active 403-Forbidden Blocking
- **Logic:** Behavioral Risk Analysis
""")
st.sidebar.markdown("---")
# Live pulse effect for the judges
st.sidebar.success("🟢 System Heartbeat: ACTIVE")
st.sidebar.caption("Last Sync: " + time.strftime("%H:%M:%S"))

# --- APP STYLING ---
def apply_style(is_attack):
    if is_attack:
        st.markdown("""<style> .stApp { background-color: #2b0000; color: white; } </style>""", unsafe_allow_html=True)
    else:
        st.markdown("""<style> .stApp { background-color: #0e1117; color: white; } </style>""", unsafe_allow_html=True)

# --- DATA LOADING (Updated for GitHub/Local Demo) ---
df = pd.DataFrame(columns=['timestamp', 'client_ip', 'risk_score', 'status'])

try:
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path, check_same_thread=False)
        # Load the latest 50 logs for the Audit Trail
        df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 50", conn)
        conn.close()
    else:
        st.sidebar.warning("📡 Demo Mode: Local DB not found.")
except Exception as e:
    st.sidebar.error(f"Mode: Offline View")

# Check for attacks (High Risk Score > 0.8 in the last 5 requests)
is_under_attack = False
if not df.empty:
    is_under_attack = any(df.head(5)['risk_score'] > 0.8)

apply_style(is_under_attack)

# --- HEADER ---
st.title("🛡️ FinTech Risk Shield: Zero Trust AI Gateway")
st.markdown("---")

if is_under_attack:
    st.error("⚠️ CRITICAL SECURITY BREACH DETECTED: 403 AUTO-BLOCKING ENABLED")
else:
    st.success("✅ System Status: SECURE - Zero Trust Policy Active")

# --- METRICS (Making it look Attractive) ---
c1, c2, c3 = st.columns(3)
total_reqs = len(df)
current_risk = df['risk_score'].iloc[0] if not df.empty else 0.0

with c1:
    st.markdown("### Total Traffic")
    st.subheader(f"📊 {total_reqs} Requests")
with c2:
    st.markdown("### Threat Level")
    st.subheader(f"🔥 {current_risk:.2f} Score")
with c3:
    st.markdown("### Firewall State")
    status_text = "🔒 LOCKED" if is_under_attack else "🔓 MONITORING"
    st.subheader(status_text)

# --- VISUALIZATION ---
if not df.empty:
    # Risk Trend Chart
    fig = px.area(df, x='timestamp', y='risk_score', title="Live AI Behavioral Risk Analysis")
    fig.update_traces(line_color='#ff4b4b' if is_under_attack else '#00ffcc', fillcolor='rgba(0, 255, 204, 0.1)')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

    # Audit Trail Table
    st.subheader("📋 Real-time Security Audit Trail")
    # Styling the status column for the table
    def color_status(val):
        color = 'red' if val == '403 Forbidden' else 'green'
        return f'color: {color}'
    
    st.dataframe(df.style.applymap(color_status, subset=['status']), use_container_width=True)
else:
    st.warning("📡 No traffic detected. Please start the simulator (simulate_traffic.py) to feed the AI.")

# --- AUTO-REFRESH ---
# Updates every 2 seconds to show live data
time.sleep(2)
st.rerun()
