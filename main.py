import streamlit as st
import matplotlib.pyplot as plt
import streamlit_antd_components as sac
from streamlit_echarts import st_echarts


sb = st.sidebar
st.logo("https://avatars.githubusercontent.com/u/124514548?v=4",size='large')
st.markdown("## Debian Community .")
st.caption("By @DebianCommunity :material/forum:")
### news about new release

with sb:
    st.caption("**ghassenTn** :material/workspace_premium:")
    sac.divider(label='Social Media', icon='wechat', align='center', color='gray')
    sac.buttons([
    sac.ButtonsItem(icon='github',label='Github'),
    sac.ButtonsItem(label='wechat', icon='wechat'),
    sac.ButtonsItem(label='',icon='apple')
], label='', align='center')
    sac.rate(label='', value=3.5, align='center',half=True)
    liquidfill_option = {
    "series": [{"type": "liquidFill", "data": [0.8, 0.5, 0.4, 0.3]}]
    }
    st_echarts(liquidfill_option)



option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
            ["Milk Tea", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
            ["Matcha Latte", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
            ["Cheese Cocoa", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
            ["Walnut Brownie", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
        ]
    },
    "xAxis": {"type": "category"},
    "yAxis": {"gridIndex": 0},
    "grid": {"top": "55%"},
    "series": [
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "pie",
            "id": "pie",
            "radius": "30%",
            "center": ["50%", "25%"],
            "emphasis": {"focus": "data"},
            "label": {"formatter": "{b}: {@2012} ({d}%)"},
            "encode": {"itemName": "product", "value": "2012", "tooltip": "2012"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")
    
    
    





    
            
    