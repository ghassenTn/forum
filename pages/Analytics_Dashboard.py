import streamlit as st
import numpy as np
cols = st.columns(2)
st.logo("https://img.icons8.com/?size=100&id=uKPJ5HL65nlH&format=png&color=000000",size='large')


a, b = st.columns(2,vertical_alignment='center')
c, d = st.columns(2,vertical_alignment='center')

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)

