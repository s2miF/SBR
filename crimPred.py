#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:56:09 2024

@author: SamiFahad
"""
# Visualization Libraries
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Preprocessing Libraries
import pandas as pd
import numpy as np
import streamlit as st

import pickle as pi
import datetime


#st.markdown('<style>body{direction: rtl;background-color: red; align-items: center;}</style>',
#            unsafe_allow_html=True)

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

knnReg = pi.load(open('C:/Users/Default user.E5AD/Desktop/crime/knnReg_model.pkl', 'rb'))
with open('C:/Users/Default user.E5AD/Desktop/crime/classificationMrand_model.pkl', 'rb') as f:
    ClassMo = pi.load(f)
#prophet = pi.load(open('C:/Users/Default user.E5AD/Desktop/crime/prophet_model.pkl', 'rb'))
#with open('C:/Users/Default user.E5AD/Desktop/crime/prophet_model.pkl', 'rb') as f:
   # prophet = pi.load(f)
with open('C:/Users/Default user.E5AD/Desktop/crime/primary_type_mapping.pkl', 'rb') as f:
    primary_type_mapping = pi.load(f)
df = pd.read_csv("C:/Users/Default user.E5AD/Desktop/crime/dSC.csv",index_col=0)



def predictReg (input_data):
  
    inp = input_data
    inp1 = np.array(inp)
    input_as_np = inp1.reshape(1, -1)
    pre = knnReg.predict(input_as_np)
    pr = pre.astype(int)
    return(f"العدد المتوقع : {pr[0]}")
def predictCls (input_data):
  
    inp = input_data
    inp1 = np.array(inp)
    input_as_np = inp1.reshape(1, -1)
    pre = ClassMo.predict(input_as_np)
    def unfactorize_primary_type(factorized_predictions, primary_type_mapping):
        original_primary_type_predictions = primary_type_mapping[factorized_predictions]
        return original_primary_type_predictions

    original_primary_type_predictions = unfactorize_primary_type(pre, primary_type_mapping)
    return(f"الجريمة المتوقعة : {original_primary_type_predictions[0]}")

def main():
    option = st.selectbox("هل تريد التنبؤ بعدد الجرائم أم نوع الجريمه ",
                          ("عدد الجرائم",
                           "نوع الجريمة"))
    if option == "عدد الجرائم":
        FBIcode = st.number_input("ادخل رقم الحالة الآمنية:",step=1,value=1
                                  ,placeholder="ادخل رقم الحالة الآمنية:")
        crim = st.radio(":ادخل تصنيف أهمية الجريمة",[0,1,2,3,4],horizontal=True,
                        help="ملاحظة (0) يعني أهمية مرتفعة و (4) تعني منخفة")
        area = st.number_input("ادخل رقم الحي:",step=1,value=1)
        dis = st.number_input("أدخل رقم المنطقة:",step=1,value=1)
        timeS = st.date_input("أدخل التاريخ:", datetime.date(2019, 7, 6))
        dignosis = ''
        # creating a button for perdiction
        if st.button('Result'):
            dignosis = predictReg([FBIcode,crim,dis,area,
                                   timeS.year,timeS.month,timeS.day])
            st.success(dignosis)
            
    if option == "نوع الجريمة":
        FBIcode = st.number_input("ادخل رقم الحالة الآمنية:",step=1,value=1
                                  ,placeholder="ادخل رقم الحالة الآمنية:")
        crim = st.radio("ارخل تصنيف أهمية الجريمة:",[0,1,2,3,4],horizontal=True,
                        help="ملاحظة (0) يعني أهميد مرتفعة و (4) تعني منخفة")
        area = st.number_input("ادخل رقم الحي:",step=1,value=1)
        timeS = st.date_input("أدخل التاريخ:", datetime.date(2019, 7, 6))
        dignosis = ''
        # creating a button for perdiction
        if st.button('Result'):
            dignosis = predictCls([FBIcode,crim,area,
                                   timeS.year,timeS.month,timeS.day])
            bb ,org = pd.factorize(df['primary_type'])
            #st.write(dignosis)
            st.success(dignosis) 
            
    
if __name__=='__main__':
    main()