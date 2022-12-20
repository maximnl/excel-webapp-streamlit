import pandas as pd
import plotly.express as px

excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'
df = pd.read_excel(excel_file, 
                   sheet_name = sheet_name,
                   header = 3,                          
                   usecols='B:D')
print(df.shape)
departments = df['Department'].unique().tolist()
print(departments)

departments_selection = ['Sales', 'Marketing', 'Finance']
mask = df['Department'].isin(departments_selection)
print(df[mask].head())

age_selection = (30,40)
mask = df['Age'].between(*age_selection)
df[mask]

df_grouped = df.groupby(by=['Rating']).count()[['Age']]
df_grouped

df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()
df_grouped

bar_chart = px.bar(df_grouped, 
             x='Rating', 
             y='Votes',
             text='Votes',
             color_discrete_sequence =['#F63366']*len(df_grouped),
             template= 'plotly_white')

bar_chart.show()

