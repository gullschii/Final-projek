import pickle
import streamlit as st
import pandas as pd
import numpy as np
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(DAYS_EMPLOYED, CODE_GENDER, NAME_FAMILY_STATUS, FLAG_OWN_CAR, AMT_INCOME_TOTAL, AMT_CREDIT):   
 
    # Pre-processing user input    
    if DAYS_EMPLOYED >= 3600:
        DAYS_EMPLOYED = 1
    else:
        DAYS_EMPLOYED = 0
    
    if CODE_GENDER == "M":
        CODE_GENDER = 1
    elif CODE_GENDER == "F": 
        CODE_GENDER = 1
    else:
        CODE_GENDER = 0
        
    if NAME_FAMILY_STATUS == "Married":
        NAME_FAMILY_STATUS = 1
    elif NAME_FAMILY_STATUS == "Civil marriage": 
        NAME_FAMILY_STATUS = 1
    elif NAME_FAMILY_STATUS == "Separated": 
        NAME_FAMILY_STATUS = 1
    elif NAME_FAMILY_STATUS == "Single / not married": 
        NAME_FAMILY_STATUS = 1
    elif NAME_FAMILY_STATUS == "Widow": 
        NAME_FAMILY_STATUS = 1
    else:
        NAME_FAMILY_STATUS = 0
 
    if FLAG_OWN_CAR == "N":
        FLAG_OWN_CAR = 1
    elif FLAG_OWN_CAR == "Y": 
        FLAG_OWN_CAR = 1
    else:
        FLAG_OWN_CAR = 0
        
    if AMT_INCOME_TOTAL >= AMT_CREDIT:
        AMT_INCOME_TOTAL = 1
    else:
        AMT_INCOME_TOTAL = 0

    AMT_CREDIT = AMT_CREDIT
        
    # Making predictions 
    prediction = classifier.predict( 
        [[DAYS_EMPLOYED,CODE_GENDER, NAME_FAMILY_STATUS, FLAG_OWN_CAR, AMT_INCOME_TOTAL, AMT_CREDIT]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Credit Scoring</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    DAYS_EMPLOYED = st.number_input("Berapa Hari Menjadi Pegawai")
    CODE_GENDER = st.selectbox('CODE_GENDER',("M","F"))
    NAME_FAMILY_STATUS = st.selectbox('NAME_FAMILY_STATUS',("Civil marriage","Married","Separated","Single / not married","Unknown","Widow")) 
    FLAG_OWN_CAR = st.selectbox('FLAG_OWN_CAR',("N","Y")) 
    AMT_INCOME_TOTAL = st.number_input("Pemasukan Total Dalam Sebulan")
    AMT_CREDIT = st.number_input("Total Credit")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(DAYS_EMPLOYED,CODE_GENDER, NAME_FAMILY_STATUS, FLAG_OWN_CAR, AMT_INCOME_TOTAL, AMT_CREDIT) 
        st.success('Pinjaman anda {}'.format(result))
        print(AMT_CREDIT)
     
if __name__=='__main__': 
    main()