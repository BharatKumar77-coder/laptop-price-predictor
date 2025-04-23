import numpy as np
import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('Laptop_price_pred.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Predict Laptop Price")

# brand
Company = st.selectbox('Brand',df['Company'].unique())

TypeName = st.selectbox('Type',df['TypeName'].unique())


Ram = st.selectbox('Ram In GB',[2,4,6,8,12,16,24,32])

Weight = st.number_input('Weight of laptop')

Touchscreen = st.selectbox('TouchScreen',['NO','YES'])

IPS  = st.selectbox('IPS',['NO','YES'])

screen_size = st.number_input('Screen Size')

screen_resolution = st.selectbox('Screen Resolution',['1280×800','1366×768','1600×900','1920×1080','2256×1504','2736×1824','2560×1440','3200×1800','3840×2160'])

Cpu_brand = st.selectbox('CPU',df['Cpu_brand'].unique())

HDD	 = st.selectbox('HDD in GB',[0,128,256,512,1024,1024,2048])
SSD = st.selectbox('SSD in GB',[0,8,128,256,512,1024])

Graphic = st.selectbox('GPU',df['Graphic'].unique())

OpSys = st.selectbox('OS',df['OpSys'].unique())

if st.button('Predict Price'):
    if Touchscreen=='YES':
        Touchscreen = 1
    else:
        Touchscreen=0

    if IPS=='YES':
        IPS=1
    else:
        IPS=0

    x_res = int(screen_resolution.split("×")[0])
    y_res = int(screen_resolution.split("×")[1])
    ppi = (((x_res**2) + (y_res))**.5)/screen_size
    query = pd.DataFrame([[Company,TypeName,Ram,OpSys,Weight,Touchscreen,IPS,ppi,Cpu_brand,SSD,HDD,Graphic]],columns=['Company','TypeName','Ram','OpSys','Weight','Touchscreen','IPS','ppi','Cpu_brand','SSD','HDD','Graphic'])

    st.title(str(u'\u20B9') + str(int(np.exp(pipe.predict(query)[0]))))
