import streamlit as st
from langchain.llms import OpenAI

st.title(':100: Hobby Assistant')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key='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')
  st.info(llm(input_text))

with st.form('my_form'):
  # subject = st.text_input('Enter the hobby you want to work on', '', placeholder='singing, skiing, coding...')
  goal = st.text_input('Hobby goal:', '', placeholder='to order food in Italian, to get better at singing...')
  current = st.text_input('Current experience:', '', placeholder='beginner, I can run for 1 hour...')
  time = st.slider('How many minutes a day can you spend on it?', 15, 180, 45, step=15)
  st.text('Uncheck the days you want to skip')
  col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
  with col1:
    mon ="Monday " if not st.checkbox('Mon', True) else ''
  with col2:
    tue = "Tuesday " if not st.checkbox('Tue', True) else ''
  with col3:
    wed ="Wednesday " if not st.checkbox('Wed', True) else ''
  with col4:
    thur ="Thursday " if not st.checkbox('Thur', True) else ''
  with col5:
    fri = "Friday " if not st.checkbox('Fri', True) else ''
  with col6:
    sat ="Saturday " if not st.checkbox('Sat', True) else ''
  with col7:
    sun ="Sunday " if not st.checkbox('Sun', True) else ''
  skip = " Skip "+mon + tue + wed+thur+fri+sat+sun if mon or tue or wed or thur or fri or sat or sun else ""
  # text = "Write a detailed weekly guide to get better at "+subject +" spending "+ str(time) + " minutes a day." + mon + tue + wed+thur+fri+sat+sun + ". Right now my experience at "+subject+" is: "+current+". My goal is "+goal+ ". And how long will it take me to reach my goal?"
  text = "Write a one week plan "+goal +" spending "+ str(time) + " minutes a day."+ skip +" Right now my experience level is: "+current+ ". How long will it take me to reach my goal?"
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)