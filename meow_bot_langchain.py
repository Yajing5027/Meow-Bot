from langchain_util import get_response
import streamlit as st
import time

st.title('MEOW BOT')

st.divider()

if 'message' not in st.session_state:       
    st.session_state['message'] = []        


prompt = st.chat_input('Please enter your question: ')

if prompt:

    st.session_state['message'].append({'role':'user','content':prompt}) 
    for message in st.session_state['message']: 
        st.chat_message(message['role']).markdown(message['content'])

    with st.spinner('Thinking...'):
        time.sleep(1)
        
        respond = get_response(prompt,'api_key')

        st.session_state['message'].append({'role':'assistant','content':respond})  
        st.chat_message('assistant').markdown(respond)



# Run: streamlit run meow_bot.py