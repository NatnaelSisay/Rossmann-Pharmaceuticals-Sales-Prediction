from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

from myscripts.logger_config import logger

def get_null_percentage(df):
  total_size = np.prod(df.shape)

  null_count = (df.isnull().sum()).sum()

  null_percentage = round((null_count / total_size) * 100, 2)

  logger.info(f'util.py - calculate null percentage: {null_percentage}')
  return null_percentage


def get_holiday(value):
  logger.info(f'util.py - get holiday for : {value}')

  holidays = {'a': 'Public holiday', 'b': "Easter holiday", 'c':'Christmas', 0:"None"}
  return holidays.get(value, None)


def get_assortment(value):
  logger.info(f'util.py - get assortment for value of {value}')

  assort = {'a': 'Basic', 'b': 'Extra', 'c':'Extended'}
  return assort.get(value, None)


def add_month_year(df):
  '''
    'Date' - column should be actual date, not object
  '''
  logger.info('util.py - Year, Month, Day, WeekOfYear for Dataframe')

  new_df = df.copy()
  new_df['Year'] = df['Date'].dt.year
  new_df['Month'] = df['Date'].dt.month
  new_df['Day'] = df['Date'].dt.day
  new_df['WeekOfYear'] = df['Date'].dt.weekofyear
  return new_df

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2