import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sklearn

df = pd.read_csv("C:\\Users\\HP\\Desktop\\Assignment\\laptops2.csv")
st.title('Laptop Prices Predictor')

model = joblib.load('model1.pkl')

st.markdown( "## All the fields are mandatory.")
st.subheader('Laptop Details:')

company = st.selectbox("Company", options=df["Company"].unique())

def company_laptop(company):
    if company == 'Dell':
        return 6
    elif company == 'Asus':
        return 4
    elif company == 'lenovo':
        return 18
    elif company == 'Acer':
        return 2
    elif company == 'HP':
        return 7
    elif company == 'Apple':
        return 3
    elif company == 'MSI':
        return 12
    elif company == 'Avita':
        return 5
    elif company == 'MICROSOFT':
        return 11
    elif('Nokia' in i):
        return 14
    elif company == 'ALIENWARE':
        return 1
    elif company == 'LG':
        return 9
    elif company == 'Nexstgo':
        return 13
    elif company == 'Vaio':
        return 16
    elif company == 'Lenovo':
        return 10
    elif company == 'iBall':
        return 17
    elif company == 'Smartron':
        return 15
    elif company == 'AGB':
        return 0
    elif company == 'LAVA':
        return 8

company_of_laptop = company_laptop(company)


processor_name = st.selectbox("Name of the Processor",options=df["Processor_Name"].unique())


def pro_name(processor_name):
    if processor_name == "Intel":
        return 1
    elif processor_name == "AMD":
        return 0
    elif processor_name == "Microsoft":
        return 2
    elif processor_name == "Not Metioned":
        return 3


name_of_the_processor = pro_name(processor_name)


processor_type = st.selectbox("Type of the Processor(CPU)",options=df["processor_type"].unique())


def pro_type(processor_type):
    if processor_type  == "i5":
        return 10
    elif processor_type == "Ryzen 5":
        return 6
    elif processor_type  == "i7":
        return 11
    elif processor_type  == "i3":
        return 9
    elif processor_type  == "Ryzen 7":
        return 7
    elif processor_type  == "Ryzen 3":
        return 5
    elif processor_type  == "SQ1":
        return 8
    elif processor_type  == "APU":
        return 0
    elif processor_type  == "Pentium":
        return 4
    elif processor_type  == "m3":
        return 13
    elif processor_type  == "i9":
        return 12
    elif processor_type  == "Athlon":
        return 1
    elif processor_type  == "Celeron":
        return 2
    elif processor_type  == "Not Metioned":
        return 3



type_of_the_processor = pro_type(processor_type)

generation = st.number_input('Generation', min_value=0)

ram_in_gb = st.number_input('RAM in GB', step=2, min_value=2)

operating_system_type = st.selectbox("Operating System",options=df["Operating_System"].unique())


def os_type(operating_system_type):
    if operating_system_type  == "Windows 10":
        return 3
    elif operating_system_type == "Mac":
        return 2
    elif operating_system_type  == "DOS":
        return 0
    elif operating_system_type  == "Linux/Ubuntu":
        return 1
    elif operating_system_type  == "Windows 8":
        return 4


type_of_os = os_type(operating_system_type)

diskdrive_type = st.selectbox("Disk Drive",options=df["Disk_drive"].unique())


def disk_type(diskdrive_type):
    if diskdrive_type  == "SSD":
        return 3
    elif diskdrive_type == "HDD":
        return 1
    elif diskdrive_type  == "Both":
        return 0
    elif diskdrive_type  == "Not Metioned":
        return 2


type_of_diskdrive = disk_type(diskdrive_type)

rating=st.select_slider('Slide to select', options=[4.4, 4.2, 4.7, 4.5, 4.1, 4., 4.3, 5. , 3.9, 4.8, 4.9, 4.6, 3.8,3.4, 3.3, 3.7, 3.5, 3. , 3.6, 2.7, 1.6, 2. ,3.2, 2.5, 2.8])

graphic_card = st.radio("Graphic Card (0-No,1-Yes)", options=[0, 1])
touchscreen  = st.radio("Touchscreen (0-No,1-Yes)", options=[0, 1])

features=[company_of_laptop,name_of_the_processor,type_of_the_processor,generation,ram_in_gb,type_of_os,type_of_diskdrive,graphic_card,touchscreen,rating]
final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(final_features)
    st.balloons()
    #st.success(f'Your predicted price of the laptop is {round(prediction[0],3)}')
    st.success(f'Your predicted price of the laptop is {prediction[0]}')
