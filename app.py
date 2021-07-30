import streamlit as st

st.title('Stream Lit from Deployment')
st.sidebar.write('Sidebar')


# input taken from dashboard
feature_columns = ['Store', 'DayOfWeek', 'Open', 'Promo',  'SchoolHoliday', 'Day', 'WeekOfYear','Month', 'Year', 'StoreType',
              'Assortment','CompetitionDistance', 'Promo2']

## INPUTS
value1 = st.sidebar.number_input('some value')