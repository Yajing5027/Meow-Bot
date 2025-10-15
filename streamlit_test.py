import streamlit as st

# auto 'hile True:'


# title
st.title('test')

# show
st.write('Hello world')

# divider
st.divider()



# chat input case
name = st.chat_input('Please enter your name: ')

if name:        # name is not None
    st.write(f'Hi, {name}')



# wait notice case
import time

with st.spinner('Thinking...'):        # add a loding animation and notice word ['with' use to auto control the progress]
    time.sleep(5)       # disappear after 5 seconds
    st.write('Think complete')



# message case (symbol support 'user' 'assissant' 'ai' 'human')
st.chat_message('user').markdown('Who are you?')
st.chat_message('assistant').markdown('I am your rabot.')
st.chat_message('ai').markdown('Yep.')
st.chat_message('human').markdown('Fine.')


# streamlit provide a dictionary for set historial message
st.session_state[key] = value

# Run: streamlit run streamlit_test.py