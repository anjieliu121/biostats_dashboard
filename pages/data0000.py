from st_pages import add_page_title
import streamlit as st
from utils.page_setup import add_sidebar_image, display_contributors
from utils.css_utils import display_download_button
from utils.text_utils import display_data_description, display_source
# for plots
import plotly.express as px
import pandas as pd
from utils.css_utils import selection_box, markdown_background, multiselection_box
from utils.data_visual import plot_header, display_plotly_chart, display_filtered_data

from utils.data_io import read_json, read_df, read_cols, subset_df, subset_df_date, convert_state_abbr_full, convert_date, sort_df, convert_df_csv, download_filtered_data
from utils.plot_utils import download_fig

from utils.data_visual import display_dataset, display_filter_cols

########################################################################################################################
#                                               set up                                                                 #
########################################################################################################################
page_info = read_json("data0000")
file_name = page_info["file_name"]
columns = page_info["columns"]
add_page_title(page_title=page_info["page_name"], layout="wide")
add_sidebar_image()

# show data description and its source
display_data_description(page_info["description"])
display_source(page_info["source"])

# show download data button
display_download_button(file_name, page_info["local_file_update_date"])

# import dataset
df = read_df(file_name)
cols = list(columns.keys())

# display data
display_dataset(df, notes="Each row has a unique state and date value pair.")

# filter dataset by column names
display_filter_cols(df, cols, "adult, pediatric")

########################################################################################################################
#                                               plots set up                                                           #
########################################################################################################################
graph_options = ["Timeseries Plot", "Multi-Line Plot"]
graph_select = plot_header(graph_options)

# transform data
df = convert_state_abbr_full(df, state_col='state')
df = convert_date(df, date_col='date', date_format='%Y/%m/%d')
df = sort_df(df, cols=['state', 'date'])

# obtain x variables
cols = read_cols(df)
variables = cols[2:-2]

# create state selection box
states = sorted(df['state_fullname'].unique())
index_Texas = states.index('Texas')
states_select = selection_box('Select State/Federal district/Inhabited territories in the U.S.', states, index=index_Texas)
df_temp = subset_df(df, "state_fullname", states_select)

# date range
start = min(df_temp['date'])
end = max(df_temp['date'])
start_date = st.date_input('Start date', start, min_value=start, max_value=end)
end_date = st.date_input('End date', end, min_value=start, max_value=end)

########################################################################################################################
#                                   timeseries scatterplot: response vs. date; colored by another response             #
########################################################################################################################


def plot_timeseries_scatter(df, variables, states_select, title):
    # create a y variable selection box + its description
    y_select = selection_box('Select the variable on the y-axis', variables, index=3)
    y_description = columns[y_select]
    markdown_background(f'Variable Description: {y_description}')
    # create a color variable selection box + its description
    color_variables = [item for item in variables if item != y_select]
    color_variables = ['None'] + color_variables
    c_select = selection_box('(Optional) Select another variable to compare with the selected y variable', color_variables, index=0)
    if c_select != "None":
        c_description = columns[c_select]
        markdown_background(f'Variable Description: {c_description}')
        # plot
        fig = px.scatter(df, x='date', y=y_select, color=c_select, color_continuous_scale="reds", title=title)
    else:
        # plot
        fig = px.scatter(df, x='date', y=y_select, title=title)
    # update plot layout
    fig.update_layout(
        title={
            'text': title,
            'y': 0.95,
            'x': 0.35,
            'xanchor': 'center',
            'yanchor': 'top'},
    )
    fig = display_plotly_chart(fig)
    # download fig
    title = f"{title}-{y_select}-{c_select}"
    download_fig(fig, title)


########################################################################################################################
#                                   timeseries lineplot: multiple responses vs. date                                   #
########################################################################################################################


def plot_timeseries_line(df, variables, states_select, title):
    linewidth = 1
    # create a multiple variable selection box
    options = multiselection_box('Select multiple variables to compare', variables, variables[0], variables[3])
    # variable descriptions
    for i in options:
        y_description = columns[i]
        markdown_background(f'{i}: {y_description}')
    # customize the color of lines
    n_colors = len(options)
    if n_colors > 0:
        if n_colors == 1:
            colors = ["indianred"]
        elif n_colors == 2:
            colors = ["indianred", "steelblue"]
        elif n_colors == 3:
            colors = px.colors.sample_colorscale("emrld", [n / (n_colors - 1) for n in range(n_colors)])
        else:
            colors = px.colors.sample_colorscale("viridis", [n / (n_colors - 1) for n in range(n_colors)])
        # plot
        fig = px.line(df, x='date', y=options[0], hover_data={'date': False})
        fig.update_traces(line_color=colors[0], mode="markers+lines", marker=dict(size=1), name=options[0],
                          showlegend=True, line=dict(width=linewidth))  # hovertemplate=None,
        fig.update_layout(
            title={
                'text': title,
                'y': 0.95,
                'x': 0.35,
                'xanchor': 'center',
                'yanchor': 'top'},
            # legend_title=dict(text="Selected Variables"),
            legend_tracegroupgap=10
        )

        for i, color in zip(range(1, len(options)), colors[1:]):
            line_trace = px.line(df, x='date', y=options[i], hover_data={'date': False})
            line_trace.update_traces(line_color=color, mode="markers+lines", marker=dict(size=1), name=options[i],
                                     showlegend=True, line=dict(width=linewidth))
            fig.add_trace(line_trace.data[0])

        fig.update_layout(yaxis_title=None, hovermode="x unified")
        fig = display_plotly_chart(fig)
        # download fig
        title = f"{title}-{'-'.join(options)}"
        download_fig(fig, title)


if start_date < end_date:
    start_date, end_date = pd.Timestamp(start_date), pd.Timestamp(end_date)
    df_temp = subset_df_date(df_temp, "date", start_date, end_date)
    # title
    title = f"{states_select} from {start_date.date()} to {end_date.date()}"
    if graph_select == graph_options[0]:
        plot_timeseries_scatter(df_temp, variables, states_select, title)
    elif graph_select == graph_options[1]:
        plot_timeseries_line(df_temp, variables, states_select, title)
    # show and download filtered data
    display_filtered_data(df_temp)
    download_filtered_data(df_temp, file_name[:-4], title)
else:
    st.error('Error: End date must fall after start date.')

# show people who upload the data
upload_users = page_info['upload_users']
display_contributors(upload_users)
