import streamlit as st
cols = st.columns(2)
st.logo("https://img.icons8.com/?size=100&id=uKPJ5HL65nlH&format=png&color=000000",size='large')
with cols[0]:
    st.metric("Indicator",19,delta='%',delta_color='normal')