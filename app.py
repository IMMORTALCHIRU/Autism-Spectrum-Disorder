import numpy as np
import pickle
import streamlit as st
from PIL import Image
loader_model=pickle.load(open(r'C:\Users\chiru\OneDrive\Desktop\Prediction-main\trained_model.sav','rb'))
def asd(input_data):

    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loader_model.predict(input_data_reshaped)
    print(prediction)
    if prediction==0:
        return 'Patient is ASD'
    else:
        return 'Patient is non ASD'


def main():
    #add background image
    def add_bg_from_url():
        st.markdown(
            f"""
         <style>
         .stApp {{
             background-image: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/autism-awareness-dtg-free-shipping-autism-brock-tooth.jpg");
             background-attachment: fixed;
             background-size: cover;
             background-repeat: no-repeat;
             background-position: center center;
             height: 100vh;
         }}
         .stApp::before {{
            content: ""; /* Required for pseudo-elements */
            position: absolute; /* Position the pseudo-element relative to its parent */
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.80); /* Black color with 50% opacity */
}}
         </style>
         """,
         unsafe_allow_html=True
     )

    add_bg_from_url()

    s1="<h1><center><strong><font color='red' style='font-family: Sans-serif;'> Early Detection of </font> <font color='yellow' style='font-family: Sans-serif;'> Autism</font> <font color='lightblue' style='font-family: Sans-serif;'> Spectrum</font> <font color='lightgreen' style='font-family: Sans-serif;'> Disorder</font></strong></center></h1>"

    st.markdown(s1, unsafe_allow_html=True)

    original_image = Image.open(r'C:\Users\chiru\OneDrive\Desktop\Prediction-main\asd2_cleanup.png')
    new_width = 900  # Set the new width (in pixels)
    new_height = 420
    resized_image = original_image.resize((new_width, new_height))
    st.image(resized_image, use_column_width=True)


    # add color to selectboxes
    css = '''
<style>
    .stSelectbox [data-testid='stMarkdownContainer'] {
        color:YELLOW;
        font-size:200px;
    }
</style>
'''

    st.markdown(css, unsafe_allow_html=True)

    a11=st.selectbox("Does your child look at you when you call his/her name?",["","YES","NO"])
    if a11=="YES":
        a1=1
    else:
        a1=0
 
    a22=st.selectbox("Is it easy for you to get eye contact with your child?",["","YES","NO"])
    if a22=="YES":
        a2=1
    else:
        a2=0
    
    a33=st.selectbox("Does your child point to indicate that she/he wants something? (e.g. a toy that is out of reach)",["","YES","NO"])
    if a33=="YES":
        a3=1
    else:
        a3=0

    a44=st.selectbox("Does your child point to share interest with you? (e.g. pointing at an interesting sight) ",["","YES","NO"])
    if a44=="YES":
        a4=1
    else:
        a4=0
    
    a55=st.selectbox("Does your child pretend? (e.g. care for dolls, talk on a toy phone)",["","YES","NO"])
    if a55=="YES":
        a5=1
    else:
        a5=0
    
    a66=st.selectbox("Does your child follow where you’re looking?",["","YES","NO"])
    if a66=="YES":
        a6=1
    else:
        a6=0
  
    a77=st.selectbox("If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them? (e.g. stroking hair, hugging them)",["","YES","NO"])
    if a77=="YES":
        a7=1
    else:
        a7=0
    
    a88=st.selectbox("Would you describe your child’s first words?",["","YES","NO"])
    if a88=="YES":
        a8=1
    else:
        a8=0
    
    a99=st.selectbox("Does your child use simple gestures? (e.g. wave goodbye)",["","YES","NO"])
    if a99=="YES":
        a9=1
    else:
        a9=0
   
    a100=st.selectbox("Does your child stare at nothing with no apparent purpose?",["","YES","NO"])
    if a100=="YES":
        a10=1
    else:
        a10=0
    age=st.slider("Age_Mons",12,36)
    css = '''
<style>
    .stSlider [data-testid='stMarkdownContainer'] {
        color: red;
    }
</style>
'''

    st.markdown(css, unsafe_allow_html=True)
    
    g=st.selectbox("Gender",["","Male","Female"])
    if g=="Male":
        gender=1
    else:
        gender=0
        
    e=st.selectbox("Ethnicity",["","Middle Eastern","White European",'Hispanic','Asian','South Asian','Native Indian','Black','Latino','Mixed','Pacifica','Others'])
    if e=="Middle Eastern":
        et=0
    elif e=="White European":
        et=1
    elif e=='Hispanic':
        et=2
    elif e=='Others':
        et=3
    elif e=='Asian':
        et=4
    elif e=='South Asian':
        et=5
    elif e=='Native Indian':
        et=6
    elif e=='Black':
        et=7
    elif e=='Latino':
        et=8
    elif e=='Mixed':
        et=9
    elif e=='Pacifica':
        et=10
    j=st.selectbox("Jaundice",["","YES","NO"])
    if j=="YES":
        jd=1
    else:
        jd=0
    
    f=st.selectbox("Family_mem_with_ASD",["","YES","NO"])
    if f=="YES":
        fm=1
    else:
        fm=0
    w=st.selectbox("who Completed The Test",["","Family member",'Health Care Professional','Self',"Others"])
    if w=="Family member":
        wh=0
    elif w=='Health Care Professional':
        wh=1
    elif w=='Self':
        wh=2
    elif w=="Others":
        wh=3
    
    
    
    diagnosis=""
    # add color to button 
    st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0000FF;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #FF0000;
    color:##ff99ff;
    }
</style>""", unsafe_allow_html=True)



    
    
    if st.button("ASD Test Result"):
        diagnosis=asd([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,age,gender,et,jd,fm,wh])

    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()

    
    
    
    
