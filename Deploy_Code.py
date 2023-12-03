import numpy as np
import pickle
import streamlit as st
model = pickle.load(open(r"C:\Users\aksha\Desktop\AI variant\Project 1\model.pkl",'rb'))

st.set_page_config(
    page_title="Sales Forecasting App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open(r"C:\Users\aksha\Downloads\R.jpeg")

st.image(image, use_column_width=True)

def welcome():
    return 'Welcome All'

def Predict_sales(last_week, last_of_last_week):
    input = np.array([[[last_week],[last_of_last_week]]]).astype(np.float64)

    prediction = model.predict(input)
    return int(prediction)

def main():
    #st.title("Sales Forecasting")
    html_temp = """
    <div style = 'background-color:cyan; padding:10px'>
    <h2 style = 'color:white;text_align:center;'>Sales Forecasting </h2>
    </div> """ 

    st.markdown(html_temp,unsafe_allow_html=True)
    last_week = st.text_input('Last_Week_Sales','Type Here')
    last_of_last_week = st.text_input('Before_Last_Week_Sales','Type Here')

    if st.button("Predict"):
        output = Predict_sales(last_week, last_of_last_week)
        st.success('The output is {}'.format(output))

    if st.button("About"):
        st.text("Contact Us")


if __name__ == '__main__':
    main()