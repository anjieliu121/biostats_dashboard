from st_pages import add_page_title
import pandas as pd
from utils.css_utils import selection_box, multiselect_css
from utils.data_io import read_df, read_cols, subset_df, download_filtered_data, read_json
from utils.data_visual import plot_header, plot_timeseries, plot_lines, plot_bar, display_filtered_data, display_filter_cols, display_dataset

from utils.page_setup import display_page
from utils.plot_utils import download_fig

page_info = read_json("data0001")
file_name = page_info["file_name"]

add_page_title(page_title=page_info["page_name"], layout="wide")

display_page(page_info)


# import dataset
df = read_df(file_name)
cols = read_cols(df)

# display dataset
display_dataset(df, notes="Each row has a unique combination of Geography, Age, and Week_Ending_Sat.")

# filter dataset by column names
display_filter_cols(df, cols, "Age, flu")

# variables can users can plot
var_indices = [4, 5, 6]
variables = [cols[i] for i in var_indices]

# graph options
graph_options = ["Timeseries Plot", "Multi-Line Plot", "Bar Chart"]
graph_select = plot_header(graph_options)

# geography options (US + States)
geography = sorted(df['Geography'].unique())
geography.remove("United States")
geography.insert(0, "United States")

geography_select = selection_box('Select U.S. or a State/Federal district in the U.S.', geography, index=0)
df = subset_df(df, "Geography", geography_select)

# age options
age = list(df['Age'].unique())
age.insert(0, "All Age Groups")
ages_select = multiselect_css('Select 1 or more age groups', age, age[0])
if "All Age Groups" not in ages_select:
    df = subset_df(df, "Age", *ages_select)

# plot title
title = f"Flu Coverage: {ages_select} in {geography_select}"

if graph_select == "Timeseries Plot":
    # select which variable to plot
    var_select = selection_box('Select the variable on the y-axis', variables, index=0)
    # plot
    fig = plot_timeseries(df, 'Week_Ending_Sat', var_select, title, "Age")
elif graph_select == "Multi-Line Plot":
    # select which variables to plot
    vars_select = multiselect_css("Select 1 or more variables", variables, variables[0])
    if "All Age Groups" in ages_select:
        ages_select = list(df['Age'].unique())
    fig = plot_lines(df, "Week_Ending_Sat", vars_select, title, "Age", ages_select)
elif graph_select == "Bar Chart":
    unique_combinations = df.groupby(['Geography', 'Population', 'Age']).size().reset_index().rename(columns={0: 'Count'})
    age_order = ['6 Months - 4 Years', '5-12 Years', '13-17 Years', '6 Months - 17 Years', '18-49 Years', '50-64 Years', '65+ Years']
    unique_combinations['Age'] = pd.Categorical(unique_combinations['Age'], categories=age_order, ordered=True)
    unique_combinations = unique_combinations.sort_values(by='Age')
    title = title + " and its Population"
    fig = plot_bar(unique_combinations, "Age", "Population", title)

# download figure
download_fig(fig, title)

# download filtered data
display_filtered_data(df)
filtered_conditions = f"{geography_select}_{ages_select}"
download_filtered_data(df, file_name[:-4], filtered_conditions)