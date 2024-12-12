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
st.logo("https://avatars.githubusercontent.com/u/124514548?v=4",size='large')
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
#     st.caption("**ghassenTn** :material/workspace_premium:")
#     sac.divider(label='Social Media', icon='wechat', align='center', color='gray')
#     sac.buttons([
#     sac.ButtonsItem(icon='github',label='Github'),
#     sac.ButtonsItem(label='wechat', icon='wechat'),
#     sac.ButtonsItem(label='',icon='apple')
# ], label='', align='center')
#     sac.rate(label='', value=3.5, align='center',half=True)
#     sac.alert(label='ghassenTn ', description=' Welcome  ', banner=True, icon=False, closable=True,size='md',variant='quote')
    sac.menu([
    sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
    sac.MenuItem('products', icon='box-fill', children=[
        sac.MenuItem('apple', icon='apple'),
        sac.MenuItem('other', icon='git', description='other items', children=[
            sac.MenuItem('google', icon='google', description='item description'),
            sac.MenuItem('gitlab', icon='gitlab'),
            sac.MenuItem('wechat', icon='wechat'),
        ]),
    ]),
    sac.MenuItem('disabled', disabled=True),
    sac.MenuItem(type='divider'),
    sac.MenuItem('link', type='group', children=[
        sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
        sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
    ]),
], open_all=True)
    
    
    


    
            
    