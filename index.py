#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:58:30 2024

@author: SamiFahad
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle as pi
import plotly.express as px
import streamlit as st
import time
from crimPred import main
import folium
from folium.plugins import MarkerCluster
import streamlit_folium
from streamlit_folium import folium_static ,st_folium
from streamlit_modal import Modal
from PIL import Image
import streamlit.components.v1 as comp


#st.set_page_config(layout = 'wide')
#with open('C:/Users/Default user.E5AD/Desktop/crime/index.html','r') as f:
 #   Hcontent = f.read()
    
#st.markdown(Hcontent,unsafe_allow_html=True)
#cssPath = 'C:/Users/Default user.E5AD/Desktop/crime/styles.css'
#with open(cssPath,'r')as f:
 #   cssCode = f.read()
#st.markdown(f'<style>{cssCode}</style>',unsafe_allow_html=True)
#st.pyplot(fig)
#st.markdown(m._repr_html_(), unsafe_allow_html=True)

#------include the dataset start
df = pd.read_csv("C:/Users/Default user.E5AD/Desktop/crime/dSC.csv",index_col=0)
#------include the dataset end


#-------------- side bar start
with st.sidebar.container():
    image = Image.open("C:/Users/Default user.E5AD/Desktop/crime/images/logo1.png")
    new_image = image.resize((400, 300))
    st.image(new_image,use_column_width=True)
    
#st.sidebar.image("C:/Users/Default user.E5AD/Desktop/crime/images/logo1.png",use_column_width=True)
#st.sidebar.header("هل تريد التنبؤ أم تحليل البيانات")
ch = st.sidebar.selectbox("إختر من القائمة المنسدلة الخدمة المطلوبة", ("الصفحة الرئيسية","تنبؤ" , "رسم بياني")) # choice from two op
#------------- side bar end
#-------select box start!
#------- if user select predictaiton the population 

if ch == "تنبؤ":
    #st.title("عدد السكان في المملكة العربية السعودية")
    
    main()
#------ if the user unselect 
if ch == "الصفحة الرئيسية":
    
        progress_text = "يتم تحميل الصفحة ليتم عرض البيانات التي تريدها :sunglasses:"
        my_bar = st.progress(0, text=progress_text)
        long_text = "مرحباً بك في مشروع معسكر علوم البيانات لللتنبؤ بالجريمة قبل وقوعها :balloon: " 
        with st.container(height=50):
            st.markdown(long_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
            
        #time.sleep(0.1)
            
        my_bar.empty()
        #st.balloons()
        st.markdown(
            """
            <style>
            .stNumberInput{width:306px !important; margin-left: 27% !important;} 
            </style>
            
            """,unsafe_allow_html=True)
        year = st.number_input("Enter The Year U Want Dispaly",step=1,min_value=2001,max_value=2023,format="%d",value=2020)
        col1,col2,col3=st.columns(3)
        
        with col1:
            st.markdown("<h5 style='font-style: italic;font_size: x-large; text-align: -webkit-center; color: antiquewhite;'>Top One Of CrimeType</h5>", unsafe_allow_html=True)
            crimetype = df.query(f'year == {year}')['primary_type'].value_counts().head(2)
            st.markdown(f"<h5 style='font_size: xx-large; font-style: italic;text-align: center; color: chocolate;'>{crimetype.index[0]}</h5>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<h5 style='font-style: italic;font_size: x-large; text-align: -webkit-center; color: antiquewhite;'>Total Of Crime In {year}</h5>", unsafe_allow_html=True)
            crimeCount = df.query(f'year == {year} & primary_type == "{crimetype.index[0]}"')['primary_type'].value_counts().sum()
            st.markdown(f"<h5 style='font-style: italic;font-size: xx-large; text-align: center; color: chocolate;'>{crimeCount}</h5>", unsafe_allow_html=True)

        with col3:
            
            st.markdown("<h5 style='font_size: large; text-align: -webkit-center; color:antiquewhite;'>Where The Crime Occurred </h5>", unsafe_allow_html=True)
            number3 = df.query(f'year == {year} & primary_type == "{crimetype.index[0]}"')['community_area'].value_counts().head(2)
            st.markdown(f"<h5 style='font-style: italic;font-size: xx-large; text-align:center; color:chocolate;'>{number3.index[0]}</h5>", unsafe_allow_html=True)

        #st.markdown("<hr style=margin-top: -22px;/>",unsafe_allow_html=True)
        co1,co2,co3=st.columns(3)
        
        with co1:
            st.markdown("<h5 style='font_size: x-large; text-align: -webkit-center; color: antiquewhite;'>Top Two Of crimeType</h5>", unsafe_allow_html=True)
            number1 = df.query(f'year == {year}')['primary_type'].value_counts().head(2)
            st.markdown(f"<h5 style='font-style: italic;text-align: center; color: chocolate;'>{number1.index[1]}</h5>", unsafe_allow_html=True)

        with co2:
            st.markdown(f"<h5 style='font_size: x-large; text-align: -webkit-center; color: antiquewhite;'>Total Of Crime In{year}</h5>", unsafe_allow_html=True)
            number2 = df.query(f'year == {year}')['primary_type'].value_counts().sum()
            st.markdown(f"<h5 style='font-style: italic;font-size: xx-large; text-align: center; color: chocolate;'>{number2}</h5>", unsafe_allow_html=True)

        with co3:
            
            st.markdown("<h5 style='font_size: large; text-align: -webkit-center; color: antiquewhite;'>Where The Crime Occurred </h5>", unsafe_allow_html=True)
            number3 = df.query(f'year == {year} & primary_type == "{number1.index[1]}"')['community_area'].value_counts().head(2)
            st.markdown(f"<h5 style='font-style: italic;font-size: xx-large; text-align: center; color: chocolate;'>{number3.index[1]}</h5>", unsafe_allow_html=True)

        st.markdown("<hr/>",unsafe_allow_html=True)
        st.info("موضح في الخارطة أدناه المركبات الأمنية وعدد الجرائم في كل منطقة")
        m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=10)

# تجميع البيانات وحساب عدد الـ beat في كل منطقة
        beat_counts = df.groupby('community_area')['beat'].apply(lambda x: len(set(x)))

# تجميع البيانات وحساب عدد الجرائم في كل منطقة
        crime_counts = df.groupby('community_area').size()

# إنشاء مجموعة علامات الأماكن
        marker_cluster = MarkerCluster()

# إضافة علامة لكل منطقة
        for area in df['community_area'].unique():
    # حصول عدد الـ beat وعدد الجرائم لكل منطقة
            beat_count = beat_counts.get(area, 0)
            crime_count = crime_counts.get(area, 0)

    # تحديد لون المنطقة التي تحتوي على أكبر عدد من الجرائم
            color = 'red' if area == crime_counts.idxmax() else 'blue'

    # إنشاء علامة لكل منطقة مع عرض عدد الـ beat وعدد الجرائم فيها
            marker = folium.Marker(location=[df[df['community_area'] == area]['latitude'].mean(),
                                     df[df['community_area'] == area]['longitude'].mean()],
                           popup=f"منطقة المجتمع: {area}<br>عدد الـ beat: {beat_count}<br>عدد الجرائم: {crime_count}",
                           icon=folium.Icon(color=color))
            marker_cluster.add_child(marker)

# إضافة مجموعة علامات الأماكن إلى الخريطة
        m.add_child(marker_cluster)

# عرض الخريطة
        
        popM = "<script>alert('لعرض صفحة تحليل البيانات أو التنبؤ الرجاء الإختيار من القائمة الجانبية')</script>"
        comp.html(popM,width=10,height=10)
        map1,map2 = st.columns(2)
        with map1:
            folium_static(m, width=710, height=550)


# if user select the visual
if ch == "رسم بياني":
    
    choice = st.selectbox("اختر الرسم المراد",("None","line chart","bar chart","scatter chart","heatmap"))
    if choice == "None":
        st.warning("إختر من القائمة المنسدلة الرسم المراد")
    if choice == "line chart":
        st.info("المعروض أدناه الرسم الخطي الذي يبين عدد السكان على مر السنين")
        crime_counts = df.groupby("year")['primary_type'].size()
        ye = df['year'].value_counts().sort_index()
        figure = px.line(ye,text=df['primary_type'].head(23) ,labels={"x": "years", "y": "crimeCounts"},width=997,height=510)
        st.plotly_chart(figure)
    if choice == "bar chart":
        st.info("المعروض أدناه الرسم الخطي الذي يبين عدد السكان على مر السنين")
        crime_counts = df['primary_type'].value_counts()
        figure = px.bar(crime_counts,
                     labels={"x": "Region", "y": "population"}
                     ,width=(1000),height=(500),
                     color_continuous_scale=(px.colors.sequential.Viridis))
        st.plotly_chart(figure)
    if choice == "scatter chart":
        st.info("المعروض أدناه الرسم الخطي الذي يبين عدد السكان على مر السنين")
        ye = df['year'].value_counts().sort_index()
        figure = px.scatter(ye,text=df['primary_type'].head(23),
                     labels={"x": "Region", "y": "population"},color=(df['primary_type'].head(23))
                    ,hover_name=(df['primary_type'].head(23)),width=(1000),height=(500),
                     color_continuous_scale=(px.colors.sequential.Viridis))
        st.plotly_chart(figure)
    if choice == "heatmap":
        crime_counts_by_city = df['community_area'].value_counts().sort_values(ascending=False)

# إعداد بيانات الرسم البياني
        cities = crime_counts_by_city.index
        crime_counts = crime_counts_by_city.values
        colors = crime_counts / max(crime_counts)  # تغيير لون النقاط بناءً على كمية الجريمة

# رسم الرسم البياني
        plt.figure(figsize=(12, 8))
        figure=plt.scatter(df['longitude'], df['latitude'], c=df['community_area'], cmap='viridis', s=5)
        
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Crime Locations by Community Area')
        plt.colorbar(label='Community Area')

# كتابة القيم الموجودة في العمود community_area
        for i, city in enumerate(cities):
            plt.text(df.loc[df['community_area'] == city, 'longitude'].mean(),
                     df.loc[df['community_area'] == city, 'latitude'].mean(),
                     str(city),
                     fontsize=8,
                     color='black',
                     ha='center',
                     va='center')

        st.pyplot(plt)
        
        