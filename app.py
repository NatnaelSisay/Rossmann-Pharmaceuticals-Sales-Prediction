from logging import log
import streamlit as st
import pandas as pd
from myscripts.logger_config import logger

st.set_page_config(page_title="Rossman Pharmaceuticals")

st.title('Rossmann Pharmaceuticals Prediction Dashboard')
st.sidebar.write('Sidebar')

## INPUTS
store_id = st.sidebar.number_input('Store Id', min_value=0, step=1)
test_file = st.sidebar.file_uploader("Upload Files",type=['csv'])
predict_button = st.sidebar.button('Predict')

try:
  test_df = pd.read_csv(test_file)
  st.write(test_df.head())
except:
  logger.error('File Not Correct')
  print("In Correct File type")

if(predict_button):
  st.write(f"Store = {store_id} Prediction Begin ...")