import pandas as pd
import numpy as np

student_perfomance = pd.read_csv('data/StudentsPerformance.csv')

print(student_perfomance.describe())

print(student_perfomance.dtypes)

print(student_perfomance.shape)
