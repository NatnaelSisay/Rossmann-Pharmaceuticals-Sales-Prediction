import streamlit as st

st.title('Stream Lit from Deployment')
st.sidebar.write('Sidebar')

## INPUTS
value1 = st.sidebar.number_input('some value')