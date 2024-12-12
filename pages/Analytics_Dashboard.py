import streamlit as st
import numpy as np
cols = st.columns(2)
st.logo("https://img.icons8.com/?size=100&id=uKPJ5HL65nlH&format=png&color=000000",size='large')


col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)