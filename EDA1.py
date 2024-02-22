#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:10:01 2024

@author: SamiFahad
"""

import streamlit as st
import pandas as pd
import altair as alt
#import plotly.express as px
import folium

st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

def main():
    # Title of the dashboard
    st.title('My Dashboard')

    # Load your data
    data = pd.read_csv('C:/Users/Default user.E5AD/Desktop/crime/dSC.csv',index_col=0)
    data = data.reset_index()
    #data.latitude=data.latitude.astype(int)
    #data.longitude=data.longitude.astype(int)
    #st.write(data.info())
    # Chart 1: Line Chart
    st.subheader('Line Chart')
    st.line_chart(data.year)

    # Chart 2: Bar Chart
    #st.subheader('Bar Chart')
    #st.bar_chart(x=data.index[:10],y=data.arrest)

    # Chart 3: Scatter Plot
    #st.subheader('Scatter Plot')
    #st.write(data)

    # Chart 4: Pie Chart
    #st.subheader('Pie Chart')
    #st.write(data)

    # Map
    st.subheader('Map')
    # Create a map using Folium library
    folium_map = folium.Map(location=[41.883500, -87.590531], zoom_start=12)
    # Add markers, layers, etc., to the map as needed
    st.write(folium_map)

if __name__ == "__main__":
    main()