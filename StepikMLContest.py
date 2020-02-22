#  Практическое задание
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Считаем данные
event_data = pd.read_csv('data/event_data_train.csv')

# Преобразуем данные для лучшей читабельности.
# 1. Переведем timestamp в нормальную дату.
event_data['date'] = pd.to_datetime(event_data.timestamp, unit='s')

# 2. Добавим колонку - день выполнения степа
event_data['day'] = event_data.date.dt.date

# Посчитаем, сколько пользователей заходило каждый день
print(event_data.groupby('day').user_id.nunique().head())

# Нарисуем график посещения
event_data.groupby('day').user_id.nunique().plot()
plt.show()

# Посмотрим распределение пользователей по количеству набранных баллов
event_data[event_data.action == 'passed'].groupby('user_id', as_index=False).agg({'step_id': 'count'})\
    .rename(columns={'step_id': 'passed_step'}).passed_step.hist()
plt.show()

# Мы потеряли пользователей, которые не решили ни одного степа.
# Попробуем другой метод.
print(event_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0).reset_index().head())

event_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0)\
    .reset_index().discovered.hist()
plt.show()