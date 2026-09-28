import streamlit as st
import mysql.connector
import pandas as pd
import time

# Database Function

def get_data():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "-------",
        database = "temperature_db"
)
    
    df = pd.read_sql("SELECT * FROM temperature", conn)
    conn.close()
    return df

# Streamlit App

st.set_page_config(page_title = "Tire Temperature Dashboard", layout = "centered")
st.title("Tire Temperature Dashboard")

placeholder = st.empty()

while True:
    df = get_data()
    
    if not df.empty:
        max_temp = df["temp_value"].max()
        min_temp = df["temp_value"].min()
        median_temp = df["temp_value"].median()
        latest_temp = df["temp_value"].iloc[-1]
        
        with placeholder.container():
            col1, col2, col3 = st.columns(3)
            col1.metric("Max Temp", f"{max_temp}℃")
            col2.metric("Min Temp", f"{min_temp}℃")
            col3.metric("Median Temp", f"{median_temp}℃")
           
            st.divider()
            
            st.subheader("Current Status")
            
            latest_temp = df["temp_value"].iloc[-1]
            
            if latest_temp > 35:
                st.error(f"🔴 {latest_temp}")
            elif latest_temp < 22:
                st.warning(f"🔵 {latest_temp}")
            else:
                st.success(f"🟢 {latest_temp}")
                
            st.divider()
            
            if latest_temp > 35:
                st.error(f"🔥 High Temperature Alert: {latest_temp}℃")
            elif latest_temp < 22:
                st.warning(f"❄ Low Temperature Alert: {latest_temp}℃")
            elif 22 <= latest_temp <= 35:
                st.success(f"✅ Normal Temperature: {latest_temp}℃")
            else:
                st.warning("No data available")
                          
            st.divider()
                
            summary_df = pd.DataFrame({
                    "Type": ["Max", "Min", "Median"],
                    "Temperature": [max_temp, min_temp,median_temp]
                    })
                
            st.write(summary_df.set_index("Type"))
            st.bar_chart(summary_df.set_index("Type"))
            
            time.sleep(2)