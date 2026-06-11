import streamlit as st
import pandas as pd
import random
import time

# Configure the page settings
st.set_page_config(page_title="Ocularis AI", page_icon="👁️", layout="wide")

# Dashboard Header
st.title("👁️ Ocularis AI: Sentinel Engine")
st.subheader("Sub-200ms Synthetic KYC Fraud Detection")

# Load the dataset you just generated
@st.cache_data
def load_data():
    try:
        return pd.read_csv("ocularis_synthetic_kyc_data.csv")
    except FileNotFoundError:
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.error("Data not found. Make sure ocularis_synthetic_kyc_data.csv is in the same folder.")
else:
    # 1. Top Level Metrics
    st.markdown("### System Telemetry")
    col1, col2, col3 = st.columns(3)
    
    total_scanned = len(df)
    fraud_detected = df['Fraud_Flag'].sum()
    
    col1.metric("Total KYC Profiles Scanned", f"{total_scanned:,}")
    col2.metric("Synthetic Fraud Caught", f"{fraud_detected}")
    col3.metric("Avg Engine Latency", "184 ms", "-12 ms") # Shows a cool green arrow

    st.divider()

    # 2. Live Scan Simulation
    st.markdown("### Live Endpoint Simulation")
    st.write("Click the button below to simulate a real-time banking API call running entirely locally.")
    
    if st.button("Run Real-Time Verification Scan", type="primary"):
        with st.spinner("Processing payload via localized SLM..."):
            time.sleep(0.18) # Simulates your sub-200ms latency
            
            # Grab one random applicant from your data
            sample = df.sample(1).iloc[0]
            
            # Display applicant details
            st.write("**Incoming Applicant Profile:**")
            st.code(f"Name: {sample['First_Name']} {sample['Last_Name']}\nDOB: {sample['DOB']}\nPAN: {sample['PAN_Number']}\nAadhaar: {sample['Aadhaar_Number']}")
            
            # Display the AI decision
            if sample['Fraud_Flag'] == 1:
                st.error(f"🚨 FRAUD DETECTED: Synthetic Identity Anomaly. Confidence Score: {sample['Risk_Score']}")
            else:
                st.success(f"✅ PASSED: Identity Verified. Risk Score: {sample['Risk_Score']}")

    st.divider()
    
    # 3. Data Logs
    st.markdown("### Recent Network Logs")
    st.dataframe(df.head(15), use_container_width=True)