from unittest.mock import inplace

import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

print("Dataset's first 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nDataset statistics:")
print(df.describe())

dz_df = pd.read_csv('dz.csv')

# Берем первые две колонки и заменяем неуказанные города на "(прочие)"
temp_df = dz_df[['Name','City']].fillna("(прочие)")

# Копируем последнюю колонку
temp_df['Salary'] = dz_df['Salary']

# Удаляем строки, где не указана зарплата, чтоб не портили статистику
temp_df.dropna(inplace=True)

# Группируем, усредняем и выводим
mean_salary_df = temp_df.groupby('City')['Salary'].mean()
print("\nСредняя зарплата по городам:")
print(mean_salary_df)