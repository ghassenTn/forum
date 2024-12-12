import streamlit as st
import matplotlib.pyplot as plt
import streamlit_antd_components as sac
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

def line_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 15, 25], color='#1f77b4')
    ax.set_title('Sample Line Chart')
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
sb = st.sidebar
st.logo("https://avatars.githubusercontent.com/u/124514548?v=4",size='large',link='https://github.com/ghassenTn')
st.markdown("## Debian Community .")
st.caption("By @DebianCommunity :material/forum:")
### news about new release

cnt_news = st.container(border=True)
with cnt_news:
    st.markdown("**Bar chart new release**")
    st.caption("By @DebianCommunity :material/forum:")
    st.pyplot(fake_plot())
    with st.expander("Show code"):
        st.code("""
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
""")

cnt_bubels = st.container(border=True)
with cnt_bubels:
    st.markdown("**Bubels chart new release**")
    st.caption("By @DebianCommunity :material/forum:")
    st.pyplot(bubels_plot())
    with st.expander("Show code"):
        st.code("""
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
""")

cnt_line = st.container(border=True)
with cnt_line:
    st.markdown("**Line chart new release**")
    st.caption("By @DebianCommunity :material/forum:")
    st.pyplot(line_plot())
    with st.expander("Show code"):
        st.code("""
def line_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 15, 25], color='#1f77b4')
    ax.set_title('Sample Line Chart')
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

""")

with sb:
    st.caption("**ghassenTn** :material/workspace_premium:")
    st.caption("Ml developer")
    sac.chip(
    items=[
        sac.ChipItem(label='github', icon='github'),
        sac.ChipItem(label='twitter', icon='twitter'),
    ], label='label', index=[0, 2], align='center', radius='md', multiple=True
)
    sac.rate(label='', value=3.5, align='center',half=True)
    
    


    
            
    