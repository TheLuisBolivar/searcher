# app.py
import streamlit as st

st.title("🔍 Industry Intelligence Report Generator")

user_query = st.text_area("Describe the market or company to investigate:", 
                          placeholder="e.g., Generate a strategy intelligence report for the electric vehicle market and its key players")

if st.button("Generate Report"):
    st.session_state["query"] = user_query