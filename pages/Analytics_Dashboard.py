import streamlit as st
cols = st.columns(2)

with cols[0]:
    st.metric("Indicator",19,delta='%',delta_color='normal')