from st_pages import add_page_title
from utils.constants import flu_file_names, flu_page_names, flu_descriptions, flu_url
from utils.css_utils import selection_box
from utils.data_io import read_df, read_cols, subset_df
from utils.data_visual import plot_header, display_plotly_chart
from utils.page_setup import display_page

import plotly.express as px


def plot_timeseries(df, var_select, title):
    fig = px.scatter(df, x='Week_Ending_Sat', y=var_select, color="Age", title=title)
    fig.update_layout(
        title={
            'text': title,
            'y': 0.95,
            'x': 0.35,
            'xanchor': 'center',
            'yanchor': 'top'},
    )
    fig = display_plotly_chart(fig)

key = "flu_1"
file_name = flu_file_names[key]

add_page_title(page_title=flu_page_names[key], layout="wide")

display_page(flu_file_names, flu_descriptions, flu_url, key, "1/29/2024", "Each row has a unique combination of Geography, Age, and Week_Ending_Sat.")

# import dataset
df = read_df(file_name)
cols = read_cols(df)

# variables can users can plot
variables = cols[4:]

# graph options
graph_select = plot_header()

# geography options (US + States)
geography = sorted(df['Geography'].unique())
geography.remove("United States")
geography.insert(0, "United States")

geography_select = selection_box('Select U.S. or a State/Federal district in the U.S.', geography, index=0)
df = subset_df(df, "Geography", geography_select)

# age options
# !!! change this to multiselect
age = list(df['Age'].unique())
age.insert(0, "All Age Groups")
age_select = selection_box('Select an age group', age, index=0)
if age_select != "All Age Groups":
    df = subset_df(df, "Age", age_select)

# select which variable to plot
var_select = selection_box('Select the variable on the y-axis', variables, index=0)

# plot title
title = f"Flu Coverage: {age_select} in {geography_select}"

if graph_select == "Timeseries Plot":
    plot_timeseries(df, var_select, title)

