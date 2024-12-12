import streamlit as st
import matplotlib.pyplot as plt
def fake_plot():
    fig, ax = plt.subplots()
    ax.bar(['A', 'B', 'C', 'D'], [10, 20, 15, 25], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax.set_title('Sample Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#dddddd')
    ax.spines['bottom'].set_color('#dddddd')
    ax.tick_params(axis='x', colors='#555555')
    ax.tick_params(axis='y', colors='#555555')
    ax.yaxis.grid(True, color='#eeeeee')
    ax.xaxis.grid(False)
    fig.tight_layout()
    return fig

st.markdown("## Debian Community .")
st.caption("By @DebianCommunity :material/forum:")
### news about new release
for x in range(7):
    cnt_news = st.container(border=True)
    with cnt_news:
        st.markdown("**News about new release**")
        st.caption("By @DebianCommunity :material/forum:")
        st.pyplot(fake_plot())
        
        
            
    


    
            
    