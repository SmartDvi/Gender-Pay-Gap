import dash
from dash import html, Input, Output, dcc, callback, Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from dash import dash_table
import plotly.graph_objects as go
import plotly.express as px
from dash_iconify import DashIconify

app = Dash(__name__, external_stylesheets=dmc.styles.ALL)

# Read and prepare datasets
df = pd.read_csv('C:\\Users\\Moritus Peters\\Downloads\\gap_pay\\fullDenormalised.csv')
df1 = pd.read_csv('C:\\Users\\Moritus Peters\\Downloads\\gap_pay\\gpg.csv')
df.rename(columns={'companyName': 'Company Name'}, inplace=True)
df1.rename(columns={'companyName': 'Company Name'}, inplace=True)
merged_df = pd.merge(df, df1, how='outer', on='Company Name')

#url = 'https://raw.githubusercontent.com/SmartDvi/Gender-Pay-Gap/main/merged_file.csv'
#merged_df = pd.read_csv(url)

merged_df.fillna(merged_df.mode().iloc[0], inplace=True)
merged_df.dropna(axis=1, thresh=int(0.5 * len(merged_df)), inplace=True)

# Calculate total bonuses paid to male and female employees
merged_df['total_bonus_male'] = merged_df['perBonusMale'] * merged_df['meanBonus']
merged_df['total_bonus_female'] = merged_df['perBonusFemale'] * merged_df['meanBonus']

# Calculate the difference in total bonuses
merged_df['bonus_gap'] = merged_df['total_bonus_male'] - merged_df['total_bonus_female']

# Total payroll cost based on mean hourly rates
merged_df['total_payroll_male'] = merged_df['meanHourly'] * merged_df['perBonusMale']
merged_df['total_payroll_female'] = merged_df['meanHourly'] * merged_df['perBonusFemale']

# Financial impact if the gender pay gap is closed
merged_df['pay_gap_impact'] = merged_df['total_payroll_male'] - merged_df['total_payroll_female']

# Potential savings if gender pay gap is closed (optional)
merged_df['potential_savings'] = merged_df['pay_gap_impact'] * 0.5  # Assuming 50% reduction

# Select relevant columns for the Dash DataTable
table_columns = ['Company Name', 'Company Industries', 'Report Year', 'meanHourly', 'total_payroll_male', 'total_payroll_female', 'pay_gap_impact', 'potential_savings']

# Filter the DataFrame for the table
table_data = merged_df[table_columns].dropna().round(2)



# Layout of the app
app.layout = dmc.MantineProvider(
    forceColorScheme="light",
    theme={"colorScheme": "light"},  # Setting a light theme (can be changed to dark)
    children=[
        # Main container for the dashboard
        dmc.Container(
            children=[
                # Dashboard header
                dmc.Paper(
                    children=[
                        html.H1(
                            "Gender Pay Gap Dashboard",
                            style={
                                "textAlign": "Center",
                                "marginBottom": "10px",
                                "fontSize": "2.5rem",
                                "fontWeight": "bold",
                                "color": "#34495e",  # Dark grayish-blue color
                            }
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    p="md",
                    radius="md",
                   style={"backgroundColor": "#ffffff",
                            "marginBottom": "10px",
                            "width": {"base": "100%", "md": "80%", "lg": "60%"}
                            }  # White b # White background for header
                ),
                
                # Dropdown for selecting the industry
                dmc.Select(
                    id="Company_Industries",
                    label="Select Industry",
                    data=[{"label": cat, "value": cat} for cat in merged_df["Company Industries"].dropna().unique()],
                    value=merged_df["Company Industries"].dropna().iloc[0],
                    clearable=False,
                    style={"marginBottom": "20px"}
                ),
                
                # Dropdown for selected Company(ies) under the Industry
                dmc.Select(
                    id='Company_name',
                    label='Select Company',
                    data=[],
                    value=None,
                    clearable=False,
                    style={'marginBottom': '20px'}
                ),
                
                # Grid layout for the key metrics
                dmc.Grid(
                    gutter="xl",
                    children=[
                        # Total Companies card
                        dmc.GridCol(
                            dmc.Card(
                                id="total-companies-card",
                                children=[
                                    dmc.Text("Total Companies"),
                                    dmc.Text("N/A", mt="sm", variant="gradient", size="xl")
                                ],
                                withBorder=True,
                                shadow="md",
                                radius="md",
                                style={"textAlign": "center", "height": "100%"}
                            ), span=2
                        ),
                        # Employees Female card
                        dmc.GridCol(
                            dmc.Card(
                                id="employees-female-card",
                                children=[
                                    dmc.Text("Employees Female"),
                                    dmc.Text("N/A", mt="sm", variant="gradient", size="xl"),
                                ],
                                withBorder=True,
                                shadow="md",
                                radius="md",
                                style={"textAlign": "center", "height": "100%"}
                            ), span=2
                        ),
                        # Employees Male card
                        dmc.GridCol(
                            dmc.Card(
                                id="employees-male-card",
                                children=[
                                    dmc.Text("Employees Male"),
                                    dmc.Text("N/A", mt="sm", variant="gradient", size="xl"),
                                ],
                                withBorder=True,
                                shadow="md",
                                radius="md",
                                style={"textAlign": "center", "height": "100%"}
                            ), span=2
                        ),
                        # Percentage Bonus Paid Female metrics card
                        dmc.GridCol(
                            dmc.Card(
                                id="Percentage_Bonus_Paid_Female",
                                children=[
                                    dmc.Text("mean %Bonus Paid Female"),
                                    dmc.Text("N/A", mt="sm", variant="gradient", size="xl"),
                                ],
                                withBorder=True,
                                shadow="md",
                                radius="md",
                                style={"textAlign": "center", "height": "100%"}
                            ), span=2
                        ),
                        # Percentage Bonus Paid Male metrics card
                        dmc.GridCol(
                            dmc.Card(
                                id="Percentage_Bonus_Paid_Male",
                                children=[
                                    dmc.Text("mean %Bonus Paid Male"),
                                    dmc.Text("N/A", mt="sm", variant="gradient", size="xl"),
                                ],
                                withBorder=True,
                                shadow="md",
                                radius="md",
                                style={"textAlign": "center", "height": "100%"}
                            ), span=2
                        ),
                        # mean Hourly metrics card
                        dmc.GridCol(
                            dmc.Card(
                                id="meanHourly",
                                children=[
                                    dmc.Text("mean Hourly"),
                                    dmc.Text("N/A", mt="sm", variant="gradient", size="xl"),
                                ],
                                withBorder=True,
                                shadow="md",
                                radius="md",
                                style={"textAlign": "center", "height": "100%"}
                            ), span=2
                        ),
                    ]
                ),
                dmc.Tabs(
                    children=[
                        dmc.TabsList(
                            children=[
                                dmc.TabsTab("Dataset/Details", value="1"),
                                dmc.TabsTab("Gender Representation", value="2"),
                                dmc.TabsTab("Female/Male Bonus Distribution", value="3"),
                                dmc.TabsTab("Mean and Median Hourly Pay", value="4"),
                            ]
                        ),
                    ],
                    id="tabs-example",
                    value="1",
                    variant='pills'
                ),

                # Placeholder for the content of each tab
                html.Div(id="tabs-content", style={"paddingTop": 40}),
            ],
            size="lg",
            p="md",
            style={"backgroundColor": "#f0f2f5", "borderRadius": "8px"}  # Light gray background and rounded corners for container
        )
    ]
)

@callback(
    Output('Company_name', 'data'),
    Input('Company_Industries', 'value')
)
def set_companies_options(selected_industry):
    industry_data = merged_df[merged_df["Company Industries"] == selected_industry]
    return [{'label': company, 'value': company} for company in sorted(industry_data['Company Name'].unique())]

# Function to calculate metrics
def calculate_metrics(category, company):
    if not isinstance(category, list):
        category = [category]
    if not isinstance(company, list):
        company = [company]

    category_data = merged_df[(merged_df["Company Industries"].isin(category)) & (merged_df["Company Name"].isin(company))]

    if category_data.empty:
        return {
            "total_company": "N/A",
            "EmployeesFemale": "N/A",
            "EmployeesMale": "N/A",
            "Percentage_Bonus_Paid_Female": "N/A",
            "Percentage_Bonus_Paid_Male": "N/A",
            "meanHourly": "N/A"
        }
    return {
        "total_company": f"{category_data['Company Name'].nunique():,}",
        "EmployeesFemale": f"{category_data['perBonusFemale'].sum():,}",
        "EmployeesMale": f"{category_data['perBonusMale'].sum():,}",
        "Percentage_Bonus_Paid_Female": f"{category_data['perBonusFemale'].mean():.2f}%",
        "Percentage_Bonus_Paid_Male": f"{category_data['perBonusMale'].mean():.2f}%",
        "meanHourly": f"{category_data['meanHourly'].mean():,.2f}h"
    }

@callback(
    [
        Output("total-companies-card", "children"),
        Output("employees-female-card", "children"),
        Output("employees-male-card", "children"),
        Output("Percentage_Bonus_Paid_Female", "children"),
        Output("Percentage_Bonus_Paid_Male", "children"),
        Output("meanHourly", "children"),
    ],
    [Input("Company_Industries", "value"), Input("Company_name", "value")]
)
def update_cards(industry, company):
    metrics = calculate_metrics(industry, company)

    return (
        [
            dmc.Text("Total Companies"),
            dmc.Text(metrics["total_company"], mt="sm", variant="gradient", size="xl")
        ],
        [
            dmc.Text("Employees Female"),
            dmc.Text(metrics["EmployeesFemale"], mt="sm", variant="gradient", size="xl")
        ],
        [
            dmc.Text("Employees Male"),
            dmc.Text(metrics["EmployeesMale"], mt="sm", variant="gradient", size="xl")
        ],
        [
            dmc.Text("mean %Bonus Paid Female"),
            dmc.Text(metrics["Percentage_Bonus_Paid_Female"], mt="sm", variant="gradient", size="xl")
        ],
        [
            dmc.Text("mean %Bonus Paid Male"),
            dmc.Text(metrics["Percentage_Bonus_Paid_Male"], mt="sm", variant="gradient", size="xl")
        ],
        [
            dmc.Text("mean Hourly"),
            dmc.Text(metrics["meanHourly"], mt="sm", variant="gradient", size="xl")
        ]
    )

# developing a callback to update the response of the various tabs
@callback(
    Output("tabs-content", "children"),
    [Input("tabs-example", "value"),
     Input("Company_Industries", "value"),
     Input("Company_name", "value")]
)
def render_tab_content(tab, industry, company):
    category_data = merged_df[
        (merged_df["Company Industries"] == industry) & (merged_df["Company Name"]==company)
    ]

    if tab == "1":
        return   dash_table.DataTable(
            data=table_data.to_dict("records"),
            columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in table_data.columns],
            #editable=True,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            #row_deletable=True,
            #selected_columns=[],  # Updated to avoid potential issues with selected columns
            #selected_rows=[],      # Updated to avoid potential issues with selected rows
            page_action="native",
            page_current=0,
            page_size=10
        )
       
    elif tab == "2":
        chart1 = px.violin(
            category_data, 
            y=['Percentage Employees Female', 'Percentage Employees Male'], 
            box=True, 
            points='all',
            title='Distribution of Gender Representation in Companies',
            labels={
                'value': 'Percentage of Employees',
                'variable': 'Gender'
            }
        )
        # Add detailed layout and annotations
        chart1.update_layout(
            xaxis_title='Gender',
            yaxis_title='Percentage of Employees(%)',
            title_x=0.5,
            title_y=0.95,
            annotations=[
                dict(
                    x=1.05, y=0.5, xref='paper', yref='paper',
                    text="Wider sections indicate more companies have similar percentages.",
                    showarrow=True, arrowhead=2, ax=-60, ay=0,
                    font=dict(size=12)
                ),
                dict(
                    x=0.5, y=0.95, xref='paper', yref='paper',
                    text="Median lines within the violins represent the middle value of the data.",
                    showarrow=False, font=dict(size=12)
                ),
                dict(
                    x=1.05, y=0.3, xref='paper', yref='paper',
                    text="Outliers indicate companies with unusual gender distributions.",
                    showarrow=True, arrowhead=2, ax=-60, ay=-40,
                    font=dict(size=12)
                )
            ],
            #template='plotly_white'
        )

        # Adding color and insights directly within the plot
        chart1.update_traces(meanline_visible=True, points='all', jitter=0.05, scalemode='width')
        return  dcc.Graph(figure=chart1)

    elif tab == "3":
        chart2 = go.Figure()
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Percentage Bonus Paid', 'Percentage BIK Paid'],
            y=[category_data['Percentage Bonus Paid Female'].dropna().mean(),category_data['Percentage BIK Paid Female'].dropna().mean()],
            name='Female',
            marker_color='blue'
        ))
        fig.add_trace(go.Bar(
            x=['Percentage Bonus Paid', 'Percentage BIK Paid'],
            y=[category_data['Percentage Bonus Paid Male'].dropna().mean(), category_data['Percentage BIK Paid Male'].dropna().mean()],
            name='Male',
            marker_color='lightblue'
        ))

        fig.update_layout(
            title='Percentage of Bonuses and Benefits Received by Gender',
            xaxis_title='Benefits Type',
            yaxis_title='Percentage of Employees (%)',
            barmode='group'
        )
        return dcc.Graph(figure=fig)

    elif tab == "4":
        # Use filtered_data directly instead of undefined table_data
        data = {
            'Metrics': ['Mean Hourly Gap', 'Median Hourly Gap'],
            'Female': [
                category_data['Mean Hourly Gap'].dropna().mean(),
                category_data['Median Hourly Gap'].dropna().mean()
            ],
            'Male': [
                category_data['Mean Hourly Gap'].dropna().mean(),
               category_data['Median Hourly Gap'].dropna().mean()
            ]
        }

        fig = go.Figure()
        fig.add_trace(go.Bar(x=data['Metrics'], y=data['Female'], name='Female', marker_color='blue'))
        fig.add_trace(go.Bar(x=data['Metrics'], y=data['Male'], name='Male', marker_color='lightblue'))

        fig.update_layout(
            title='Comparison of Mean and Median Hourly Pay Gaps Between Genders',
            xaxis_title='Pay Gap Metrics',
            yaxis_title='Pay Gap (%)',
            barmode='group'
        )
        return dcc.Graph(figure=fig)




if __name__ == "__main__":
    app.run(debug=True)