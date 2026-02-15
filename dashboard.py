import streamlit as st
import random
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

st.set_page_config(page_title="TigerWatch AI", layout="wide", initial_sidebar_state="collapsed")

# --- Custom Styling ---
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 28px; color: #00FFCC; }
    [data-testid="stMetricLabel"] { font-size: 16px; font-weight: bold; color: #AAAAAA; }
    .main { background-color: #0E1117; }
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background: #1A1C24;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []
if 'lat' not in st.session_state:
    st.session_state.lat, st.session_state.lon = 26.8467, 80.9462

@st.fragment(run_every=7)
def styled_dashboard():
    # Simulated Data
    st.session_state.lat += random.uniform(-0.0005, 0.0005)
    st.session_state.lon += random.uniform(-0.0005, 0.0005)
    animal = random.choice(["🐅 Tiger", "🐘 Elephant", "🐆 Leopard"])
    risk_level = random.choice(["Low", "Moderate", "Critical"])
    risk_color = {"Low": "🟢", "Moderate": "🟡", "Critical": "🔴"}[risk_level]

    # Header Section
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.title("🌲 TigerWatch AI")
        st.caption(f"Active Monitoring: Lucknow Forest Division | Last Update: {datetime.now().strftime('%H:%M:%S')}")
    with col_t2:
        st.markdown(f"### Status: {risk_color} {risk_level}")

    # Top Row Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Detection", animal)
    m2.metric("Latitude", f"{st.session_state.lat:.4f}")
    m3.metric("Longitude", f"{st.session_state.lon:.4f}")
    m4.metric("Battery", f"{random.randint(70,99)}%", delta="-1%")

    st.write("##") # Spacer

    # Middle Row: Map and Data
    c1, c2 = st.columns([2, 1])
    
    with c1:
        with st.container(border=True):
            st.markdown("#### 📍 Real-Time Location")
            m = folium.Map(location=[st.session_state.lat, st.session_state.lon], 
                           zoom_start=16, tiles="CartoDB dark_matter")
            folium.CircleMarker(
                location=[st.session_state.lat, st.session_state.lon],
                radius=10, color="red", fill=True, fill_opacity=0.7
            ).add_to(m)
            st_folium(m, width="100%", height=350, key="aesthetic_map", returned_objects=[])

    with c2:
        with st.container(border=True):
            st.markdown("#### 📜 Recent Logs")
            # Update History
            new_entry = {"Time": datetime.now().strftime("%H:%M"), "Species": animal, "Risk": risk_level}
            st.session_state.history.insert(0, new_entry)
            st.session_state.history = st.session_state.history[:8]
            
            st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True, hide_index=True)

styled_dashboard()