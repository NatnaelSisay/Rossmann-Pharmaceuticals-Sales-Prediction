import numpy as np
def get_null_percentage(df):
  total_size = np.prod(df.shape)

  null_count = (df.isnull().sum()).sum()

  null_percentage = round((null_count / total_size) * 100, 2)
  
  return null_percentage

def get_holiday(value):
  holidays = {'a': 'public holiday', 'b': "Easter holiday", 'c':'Christmas', 0:"None"}
  return holidays.get(value, None)

def get_assortment(value):
  assort = {'a': 'basic', 'b': 'extra', 'c':'extended'}
  return assort.get(value, None)

def add_month_year(df):
  '''
    df index should be date time
  '''
  new_df = df.copy()
  new_df['Year'] = df.index.year
  new_df['Month'] = df.index.month
  new_df['Day'] = df.index.day
  new_df['WeekOfYear'] = df.index.weekofyear
  return new_df

