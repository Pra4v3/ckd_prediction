import streamlit as st
import pickle
import numpy as np
import pandas as pd

# 1. Develop a local working model
#     1. style the interface
#     2. feed input data to model
#     3. display prediction
#     4. add additional links and info

#loading the model 
ckd_model = pickle.load(open('ckd_best_model.pickle', "rb"))

# 1. style the interface

st.set_page_config(layout='wide')
st.title("Chronic Kidney Disease (CKD) Prediction using ML 🩺")

st.markdown('''###### This Web app predicts whether a person has chronic kidney disease or not.  
It uses a trained **Machine learning model ⚙️**  for the predictions''')

st.link_button('What is CKD ?', 'https://www.kidney.org/kidney-topics/chronic-kidney-disease-ckd')


# Total data columns needed = 22
data_columns = ['age', 'bp', 'bu', 'sc', 'sod', 'pot', 'hemo',
             'wbcc', 'rbc_abnormal','rbc_normal', 'htn_no',
              'htn_yes', 'dm_no', 'dm_yes', 'cad_no',
              'cad_yes', 'appet_good', 'appet_poor', 
               'pe_no',	'pe_yes', 'ane_no', 'ane_yes']

# Actual inputs needed = 14 + (systolic bp+Diastolic bp) = 14+MAP 
# So 4 columns with 4 each
# one large central box for prediction result
     

st.divider()

col0, col1, col2, col3, col4 = st.columns(5, gap='large')

with col0:
    st.markdown("")
    st.markdown("")
    age = st.number_input(label= "Age",step=1)
    sbp = st.number_input(label= "Systolic Blood Pressure mm/hg", step=1)
    dbp = st.number_input(label= "Diastolic Blood Pressure mm/hg", step=1)
    map = dbp + (1/3 * (sbp - dbp))
    st.write(f'Mean arterial pressure is {round(map)} mm/hg')

with col1:
    st.markdown("")
    st.markdown("")
    hpt = st.selectbox('Does this person have Hypertension ?', ['yes', 'no'])
    dm = st.selectbox('Does this person have Diabetes ?', ['yes', 'no'])
    ihd = st.selectbox('Does this person had coronary artery disease ?', ['yes', 'no'])
    
with col2:
    st.markdown("**Laboratory 🧪**")
    scr_level = st.number_input(label= "Serum creatinine level mg/dL", step=0.1)
    bu_level = st.number_input(label= "Blood urea level mg/dL", step=0.1)
    na_level = st.number_input(label= "Blood Sodium level mEq/L", step=0.1)
    k_level  = st.number_input(label= "Blood Potassium level mEq/L", step=0.1)
# adding submit button
    st.markdown("")
    st.divider()
    st.markdown("")
    submitted = st.button("Get the results 📋") 

with col3:
    st.markdown("**Findings**")
    wbcc_level = st.number_input(label= "White blood cells amount cells/cumm", step=1)
    hb_level = st.number_input(label= "Hemoglobin level g/dL", step=0.1)
    rbc_type = st.radio('are there abnormal red blood cells in urine ?', ['yes', 'no'])

with col4:
    st.markdown("")
    st.markdown("")
    appetite = st.radio('How is the appetite ?', ['good', 'poor'])
    edema = st.radio('Is there leg edema ?', ['yes', 'no'])
    anemia = st.radio('Is there history of anemia ?', ['yes', 'no'])


st.divider()
#col4, col5, col6, col7 = st.columns(4, gap='small')   

# 2. feed input data to model

if hpt == 'yes':
    htn_yes = 1
    htn_no = 0
else:
    htn_yes = 0
    htn_no = 1

if dm == 'yes':
    dm_yes = 1
    dm_no = 0
else:
    dm_yes = 0
    dm_no = 1

if rbc_type == 'yes':
    rbc_abnormal = 1
    rbc_normal = 0
else:
    rbc_abnormal = 0
    rbc_normal = 1

if ihd == 'yes':
    cad_yes = 1
    cad_no = 0
else:
    cad_yes = 0
    cad_no = 1

if appetite == 'good':
    appet_good = 1
    appet_poor = 0
else:
    appet_good = 1
    appet_poor = 0

if edema == 'yes':
    pe_yes = 1
    pe_no = 0
else:
    pe_yes = 0
    pe_no = 1

if anemia == 'yes':
    ane_yes = 1
    ane_no = 0
else:
    ane_yes = 1
    ane_no = 0

# convert strings to variables

input_variables = [age, map, bu_level, scr_level, na_level, k_level, hb_level,
             wbcc_level, rbc_abnormal, rbc_normal, htn_no,
              htn_yes, dm_no, dm_yes, cad_no,
              cad_yes, appet_good, appet_poor, 
               pe_no,	pe_yes, ane_no, ane_yes]

input_array = np.array(input_variables).reshape(1, -1) 

ckd_prediction = ckd_model.predict(input_array)


# 3. display prediction

# Giving ckd prediction

if submitted:
    with col2:
        if ckd_prediction:           
            st.error('This person has high risk of CKD ⚠️. Please seek further medical support')
        else:
            st.success("This person is unlikely to have CKD")


# 4. add additional links and info

tab0, tab1, tab2 = st.tabs(['About the app','Disclaimer', 'About the author'])

 # making about the app
with tab0:
    st.markdown(''' **This web app uses Trained Random Forrest Classifier Machine learning model
                            to predict the possibility of a person having ckd or not**  
                            It was trained with publicly available 
                            [data from actual patients](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)  
                            ''')
    st.markdown('If you are interested source code for the app and training data can be found [here](add link to github)')

# making disclaimer
with tab1:
    st.markdown('Please note that the predictions made by this application are for informational purposes only and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always seek the guidance of your physician or other qualified health provider with any questions you may have regarding a medical condition.')



# making about the author
with tab2:
    st.markdown(''' **I am Praveen Adeesha,  
               As a medical doctor, I am deeply passionate about utilizing the field of artificial intelligence 
               to improve healthcare systems.**''')  
    st.markdown (""" Throughout my career across various hospitals in Sri Lanka, I have encountered many patients who had undiagnosed chronic kidney disease for extended periods.  
                Their late presentation of CKD-related symptoms often results in them being left undiagnosed until the later stages of the disease.  
                I aim to create this app to assist healthcare workers and the general public in identifying individuals at risk of developing chronic kidney disease.
                            """)
    st.markdown('You can contact me through nbn100lk@gmail.com')
            
