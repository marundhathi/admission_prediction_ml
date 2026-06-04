import streamlit as st
from PIL import Image
import joblib

st.title("Admission Prediction and University Recommendation")
st.header('Data Analysis')
st.subheader('Data Description')
st.write('This app predicts admission of students to universities(Yes/No). If admitted, it recommends the university.')
st.image(Image.open('uni.jpg'))

gre=st.number_input("Enter GRE Score (260–340)", value=320, step=1)
toefl=st.number_input("Enter TOEFL Score (90–120)", value=108, step=1)
univ_rating=st.number_input("Enter University Rating (1–5)", value=4, step=1)
sop=st.number_input("Enter SOP Rating (1.0–5.0)", value=4.0, step=0.1, format="%.1f")
lor=st.number_input("Enter LOR Rating (1.0–5.0)", value=4.0, step=0.1, format="%.1f")
cgpa=st.number_input("Enter CGPA (6.0–10.0)", value=8.8, step=0.01, format="%.2f")
research_input=st.radio("No of Research (0 = No, 1 = Yes)", (0, 1))
jee_score=st.number_input("Enter JEE Score (0–360)", value=310, step=1)

admi=joblib.load("model.pkl")
unimodel=joblib.load("model1.pkl")
le=joblib.load("le.pkl")

if st.button('Predict'):
                #encoding and transforming inputs
    try:
        input_features=[[gre, toefl, univ_rating, sop, lor, cgpa, int(research_input)]]
        admit_pred=admi.predict(input_features)

        if admit_pred[0]==1:
            st.write("Admission Prediction: **Admitted ✅**")

            # Step 2: University Prediction (with JEE)
            input_uni=[[gre, toefl, univ_rating, sop, lor, cgpa, int(research_input), jee_score]]
            uni_pred=unimodel.predict(input_uni)
            uni_name=le.inverse_transform(uni_pred)[0]

            st.write(f"Recommended University: **{uni_name}** 🎓")

        else:
            st.write("Admission Prediction: **Not Admitted ❌**")
            st.write("No University recommendation.")

    except Exception as e:
        st.error(f"Error in prediction: {e}")

     