import streamlit as st
import matplotlib.pyplot as plt
import mplcursors
def fake_plot():
    fig, ax = plt.subplots()
    bars = ax.bar(['A', 'B', 'C', 'D'], [10, 20, 15, 25], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
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

    # Add interactive cursor
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'Value: {sel.target[1]}'))

    return fig

def bubels_plot():
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3, 4], [10, 20, 15, 25], s=[100, 200, 150, 250], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax.set_title('Sample Bubble Chart')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
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

cnt_news = st.container(border=True)
with cnt_news:
    st.markdown("**Bar chart new release**")
    st.caption("By @DebianCommunity :material/forum:")
    st.pyplot(fake_plot())

cnt_bubels = st.container(border=True)
with cnt_bubels:
    st.markdown("**Bubels chart new release**")
    st.caption("By @DebianCommunity :material/forum:")
    st.pyplot(bubels_plot())

        
        
            
    


    
            
    