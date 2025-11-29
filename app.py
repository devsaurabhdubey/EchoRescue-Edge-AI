import streamlit as st
import pandas as pd
import time
import random

# Page Config
st.set_page_config(page_title="EchoRescue HQ", page_icon="⛑️", layout="wide")

# Custom CSS for the "Hackathon Look"
st.markdown("""
    <style>
    .stMetric { background-color: #1E1E1E; padding: 15px; border-radius: 5px; border: 1px solid #333; }
    .stAlert { padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("⛑️ ECHO-RESCUE | COMMAND CENTER")
    st.caption("Distributed Acoustic Sensing Network for Disaster Response")
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/1024px-User_icon_2.svg.png", width=50)
    st.write("**Unit:** Alpha-1 (Online)")

st.divider()

# Sidebar Controls (The "Wizard of Oz" triggers)
st.sidebar.header("👮 Demo Controller")
st.sidebar.info("Use these buttons to simulate incoming signals from the Edge device during your video.")
trigger_tap = st.sidebar.button("🚨 TRIGGER: LIFESIGN TAP")
trigger_voice = st.sidebar.button("🚨 TRIGGER: DISTRESS VOICE")
reset = st.sidebar.button("🟢 RESET SYSTEM")

# State Management
if 'status' not in st.session_state:
    st.session_state.status = "SCANNING"

if trigger_tap:
    st.session_state.status = "TAP_DETECTED"
if trigger_voice:
    st.session_state.status = "VOICE_DETECTED"
if reset:
    st.session_state.status = "SCANNING"

# Main Dashboard Interface
c1, c2, c3 = st.columns(3)

# 1. Status Panel
with c1:
    st.subheader("📡 Live Status")
    if st.session_state.status == "SCANNING":
        st.success("✅ SYSTEM NORMAL - Scanning Sector 4...")
        confidence = random.uniform(0.01, 0.05)
        st.metric("Signal Confidence", f"{confidence:.2f}", "-0.01%")
    elif st.session_state.status == "TAP_DETECTED":
        st.error("⚠️ ALERT: RHYTHMIC TAPPING DETECTED")
        st.metric("Signal Confidence", "0.98", "+95%")
        st.audio("https://www.soundjay.com/buttons/beep-01a.mp3") # Beep sound
    elif st.session_state.status == "VOICE_DETECTED":
        st.warning("⚠️ ALERT: HUMAN VOICE DETECTED")
        st.metric("Signal Confidence", "0.94", "+90%")

# 2. Probability Chart
with c2:
    st.subheader("📊 Neural Analysis")
    if st.session_state.status == "SCANNING":
        data = pd.DataFrame({'Class': ['Noise', 'Tap', 'Voice'], 'Prob': [0.95, 0.02, 0.03]})
    elif st.session_state.status == "TAP_DETECTED":
        data = pd.DataFrame({'Class': ['Noise', 'Tap', 'Voice'], 'Prob': [0.01, 0.98, 0.01]})
    else:
        data = pd.DataFrame({'Class': ['Noise', 'Tap', 'Voice'], 'Prob': [0.05, 0.05, 0.90]})
    
    st.bar_chart(data.set_index('Class'))

# 3. Map
with c3:
    st.subheader("📍 Location Lock")
    map_data = pd.DataFrame({'lat': [25.2048], 'lon': [55.2708]}) # Example coords
    st.map(map_data, zoom=12)

# Footer
st.caption("Edge Impulse Model V1.0 | Latency: 120ms | Battery: 84%")
