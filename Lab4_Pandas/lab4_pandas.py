# Lab 4 - Pandas
import pandas as pd
import numpy as np
# 1. Create DataFrame
data = {
'Name': ['Alice','Bob','Charlie','Diana','Edward'],
'Age': [22, 25, 23, 28, 21],
'City': ['Mumbai','Delhi','Bangalore','Chennai','Hyderabad'],
'Score': [85, 92, 78, 95, 70],
'Grade': ['B','A','C','A+','C']
}
df = pd.DataFrame(data)
print(df)
# 2. Basic Info
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print(df.dtypes)
# 3. Selection & Filtering
print(df['Name'].values)
print(df[df['Score'] > 80])
# 4. Add & Drop Columns
df['Passed'] = df['Score'] >= 75
df['Score_x2']= df['Score'] * 2
df.drop(columns=['Score_x2'], inplace=True)
# 5. Handle Missing Data
df2 = pd.DataFrame({'A':[1,2,None,4,5],'B':[None,2,3,None,5],'C':[1,2,3,4,5]})
print("Null counts:\n", df2.isnull().sum())
df2['A'] = df2['A'].fillna(df2['A'].mean())
df2['B'] = df2['B'].fillna(df2['B'].mean())
print(df2)
# 6. GroupBy
df3 = pd.DataFrame({
'Department': ['HR','IT','HR','IT','Finance','Finance','IT'],
'Salary': [50000,80000,55000,90000,65000,70000,75000]
})
print(df3.groupby('Department')['Salary'].agg(['mean','max','min']))
# 7. Sort
print(df.sort_values('Score', ascending=False)[['Name','Score','Grade']])
# 8. Statistical Summary
print(df[['Age','Score']].describe())
# 9. Apply Function
df['Category'] = df['Score'].apply(
lambda x: 'High' if x>=85 else ('Medium' if x>=75 else 'Low'))
print(df[['Name','Score','Category']])
