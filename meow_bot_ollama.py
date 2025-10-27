import ollama
import streamlit as st
import time

client = ollama.Client(host = "http://localhost:11434")

st.title('MEOW BOT')

st.divider()

if 'message' not in st.session_state:       # Because streamlit will auto start from begin to end every time, such as add 'while True:' at begining
    st.session_state['message'] = []        # built a list to save historial message


prompt = st.chat_input('Please enter your question: ')

if prompt:      # if prompt is not None

    st.session_state['message'].append({'role':'user','content':prompt})        # save user's message to list
    for message in st.session_state['message']:         # print list  -->  print all history messages in furter loop
        st.chat_message(message['role']).markdown(message['content'])

    with st.spinner('Thinking...'):
        time.sleep(1)
        
        respond = client.chat(          # use ollama get model respond
            model = 'deepseek-r1:8b',
            messages = [{'role':'user','content':prompt}]
        )

        st.session_state['message'].append({'role':'assistant','content':respond['message']['content']})        # save assistant's message to list
        st.chat_message('assistant').markdown(respond['message']['content'])



# Run: streamlit run meow_bot.py