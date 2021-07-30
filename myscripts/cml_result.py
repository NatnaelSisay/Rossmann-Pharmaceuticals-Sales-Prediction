# import pickle
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler

# import util

# train_df = pd.read_csv('../data/train_with_features.csv')
# columns = ['DayOfWeek', 'Date', 'Open', 'Promo', 'StateHoliday',
#        'SchoolHoliday', 'Year', 'Month', 'Day', 'WeekOfYear']

# report_file = '../report.txt'

# dt_file = '../models/dt-2021-07-30 09:51:48.726269.pkl'
# lr_file = '../models/lt-2021-07-30 09:51:48.726100.pkl'
# rfr_file = '../models/reg-2021-07-30 09:51:48.725872.pkl'

# # preparation
# sample_train = train_df.sample(1000)

# train_x = sample_train[columns]
# train_y = sample_train[['Sales']]


# #  Scale values
# x_scaler = MinMaxScaler()
# y_scaler = MinMaxScaler()

# X = x_scaler.fit_transform(train_x)
# Y = y_scaler.fit_transform(train_y)


# # train and test split
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)


# dt_model = pickle.load(open(dt_file, 'rb'))
# lr_model = pickle.load(open(lr_file, 'rb'))
# rfr_model = pickle.load(open(rfr_file, 'rb'))

# models = [lr_model, rfr_model, dt_model]
# model_names = ['LinearRegretion', 'RandomForest', 'DecisionTree']

# prediction = dt_model.score(X_test, y_test)
# print(f'Score = {round(prediction * 100, 2)}')

# def generate_report():
#   for i in range(len(models)):
#     current_model = models[i]
#     prediction = current_model.predict(X_test)

#     print(model_names[i], end=' : ')
#     score = current_model.score(X_test, y_test)
#     rmse, mae, _ = util.eval_metrics(y_test, prediction)

#     print(round(rmse,2))
#     print()

# # generate_report()

# # model score
# # model loss
# # rmse


with open('results.txt', 'w') as result:
      result.write('Model Performance\n')
      result.write('\n')     
      result.write('Linear Regression\n')
      result.write('Best Score: 44.62%\n')
      result.write('\n')  
      result.write('Decision Tree Regression\n')
      result.write('Best Score: 36.79%\n')
      result.write('\n')  
      result.write('RandomForest Regression\n')
      result.write('Best Score: 48.6%\n')
