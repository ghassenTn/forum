from random import randint
import streamlit as st
import matplotlib.pyplot as plt
import streamlit_antd_components as sac
from streamlit_echarts import st_echarts
import pandas as pd

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

sac.divider(label='Stacked Horizontal Bar', icon='bar-chart', align='center', color='gray')
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Direct", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "series": [
        {
            "name": "Direct",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [320, 302, 301, 334, 390, 330, 320],
        },
        {
            "name": "Mail Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "Affiliate Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "Video Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [150, 212, 201, 154, 190, 330, 410],
        },
        {
            "name": "Search Engine",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [820, 832, 901, 934, 1290, 1330, 1320],
        },
    ],
}
st_echarts(options=options, height="500px")
    
    
    



def get_virtual_data(year):
    date_list = pd.date_range(
        start=f"{year}-01-01", end=f"{year + 1}-01-01", freq="D"
    )
    return [[d.strftime("%Y-%m-%d"), randint(1, 10000)] for d in date_list]

option = {
    "tooltip": {"position": "top"},
    "visualMap": {
        "min": 0,
        "max": 10000,
        "calculable": True,
        "orient": "horizontal",
        "left": "center",
        "top": "top",
    },
    "calendar": [
        {"range": "2020", "cellSize": ["auto", 20]},
        {"top": 260, "range": "2019", "cellSize": ["auto", 20]},
        {"top": 450, "range": "2018", "cellSize": ["auto", 20], "right": 5},
    ],
    "series": [
        {
            "type": "heatmap",
            "coordinateSystem": "calendar",
            "calendarIndex": 0,
            "data": get_virtual_data(2020),
        },
        {
            "type": "heatmap",
            "coordinateSystem": "calendar",
            "calendarIndex": 1,
            "data": get_virtual_data(2019),
        },
        {
            "type": "heatmap",
            "coordinateSystem": "calendar",
            "calendarIndex": 2,
            "data": get_virtual_data(2018),
        },
    ],
}
st_echarts(option, height="640px", key="echarts1")

    
            
    