import streamlit as st
import matplotlib.pyplot as plt
def fake_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4])
    return fig

st.markdown("## Debian Community .")
st.caption("By @DebianCommunity :material/forum:")
### news about new release
for x in range(7):
    cnt_news = st.container(border=True)
    with cnt_news:
        st.markdown("**News about new release**")
        st.caption("By @DebianCommunity :material/forum:")
        fake_plot()
        
        
            
    


    
            
    