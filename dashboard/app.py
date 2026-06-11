
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

df = pd.read_csv('../data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
df.drop(columns=['EmployeeCount', 'Over18', 'StandardHours'], inplace=True)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Charts
fig1 = px.box(df, x='JobLevel', y='MonthlyIncome', color='JobLevel',
              title='Monthly Income by Job Level')

fig2 = px.box(df, x='PerformanceRating', y='PercentSalaryHike', color='PerformanceRating',
              title='Salary Hike % by Performance Rating')

role_salary = df.groupby('JobRole')['MonthlyIncome'].mean().reset_index().sort_values('MonthlyIncome')
fig3 = px.bar(role_salary, x='MonthlyIncome', y='JobRole', orientation='h',
              title='Avg Salary by Job Role', color='MonthlyIncome', color_continuous_scale='Viridis')

fig4 = px.box(df, x='JobLevel', y='YearsSinceLastPromotion', color='JobLevel',
              title='Years Since Last Promotion by Job Level')

dept_salary = df.groupby('Department')['MonthlyIncome'].mean().reset_index()
fig5 = px.bar(dept_salary, x='Department', y='MonthlyIncome',
              title='Avg Salary by Department', color='Department')

app.layout = dbc.Container([
    html.H1("HR Salary & Promotion Analysis Dashboard", 
            className="text-center my-4 text-warning"),
    html.P("IBM HR Analytics Dataset | 1,470 Employees", 
           className="text-center text-muted mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig1), md=6),
        dbc.Col(dcc.Graph(figure=fig2), md=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig3), md=8),
        dbc.Col(dcc.Graph(figure=fig5), md=4),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig4), md=12),
    ]),
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True, port=8050)
