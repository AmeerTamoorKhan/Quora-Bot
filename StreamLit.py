import streamlit as st
from AskMeClass import AskMe

cols = st.beta_columns((1, 2, 1, 1, 1))
cols[0].image('images/icon.png')
cols[1].title('''uora Bot''')

options = ['About', 'Quora Bot']
radio = st.sidebar.radio('Select', options)
st.sidebar.markdown('''<h3>Created By: Ameer Tamoor Khan</h3>
                    <h4>Github : <a href="https://github.com/AmeerTamoorKhan" target="_blank">Click Here </a></h4> 
                    <h4>Email: drop-in@atkhan.info</h4> ''', unsafe_allow_html=True)

def default():
    st.header('Working Demonstration:')
    st.video('Images/output.mp4')
    st.header('How is Works:')
    st.markdown('''
            <p>Quora Bot is just a fun Scraping project to grab a relevant, more suitable answer for the asked
            question.</p>
            <p>Scraping is a process of extracting information from the web. Big Data plays an important role in Machine 
            learning. And it happens that you are in search of particular data, which is not easily available, then scraping 
            comes into play.</p>
            <h3><strong>#scraping</strong>  <strong>#selenium</strong>  <strong>#python</strong>  
            <strong>#machinelearning</strong></h3>
            ''', unsafe_allow_html=True)


if radio == options[1]:
    st.header('Enter Your Question:')

    question = st.text_input('e.g., What is Life?', '')
    col = st.beta_columns((1, 1, 1, 1, 1, 1))
    with col[0]:
        enter = st.button('Search')
    with col[1]:
        reset = st.button('Reset')
    st.header('Answer:')
    ans = st.empty()
    ans.text_area('', height=400)
    if enter:
        bot = AskMe(question)
        bot_answer = bot.answer
        ans.text_area('', bot_answer, height=400)
    elif reset:
        st.empty()
elif radio == options[0]:
    default()

