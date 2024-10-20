
import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open("pipe.pkl",'rb'))
price_ind = pickle.load(open("laptop.pkl",'rb'))


st.title("Laptop Price Recommender System")
company = st.selectbox('Brand',price_ind['Company'].unique())
type = st.selectbox('type',price_ind['TypeName'].unique())
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop')

touchscreen = st.selectbox('Touchscreen',['NO','Yes'])
ips = st.selectbox('IPS',['No','Yes'])
screen_size = st.number_input('Screen Size')
resolution =  st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU',price_ind['cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',price_ind['Gpu_varity'].unique())

os = st.selectbox('OS',price_ind['os'].unique())
if st.button('Predict Price'):

    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os],dtype=object)

    query = query.reshape(1, 12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))




