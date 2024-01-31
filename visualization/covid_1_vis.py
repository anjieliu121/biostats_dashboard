import streamlit as st
import plotly.express as px
import pandas as pd

from utils.css_utils import selection_box, markdown_background, \
    multiselect_css
from utils.data_visual import plot_header, display_plotly_chart, display_filtered_data

from utils.constants import covid_1_description
from utils.data_io import read_df, read_cols, subset_df, subset_df_date, customize_df_covid1, convert_df_csv, download_filtered_data
from utils.plot_utils import download_fig




#@st.cache_data(ttl=24 * 3600)
def visualization(file_name):
    graph_options = ["Timeseries Plot", "Multi-Line Plot"]
    graph_select = plot_header(graph_options)
    # import dataset
    df = read_df(file_name)
    df = customize_df_covid1(df)
    cols = read_cols(df)

    # x variables
    variables = cols[2:-2]

    # create state selection box
    states = sorted(df['state_fullname'].unique())
    index_Texas = states.index('Texas')
    states_select = selection_box('Select State/Federal district/Inhabited territories in the U.S.', states,
                                  index=index_Texas)
    df_temp = subset_df(df, "state_fullname", states_select)

    # date range
    start = min(df_temp['date'])
    end = max(df_temp['date'])
    start_date = st.date_input('Start date', start, min_value=start, max_value=end)
    end_date = st.date_input('End date', end, min_value=start, max_value=end)
    if start_date < end_date:
        start_date, end_date = pd.Timestamp(start_date), pd.Timestamp(end_date)
        df_temp = subset_df_date(df_temp, "date", start_date, end_date)
        # title
        title = f"{states_select} from {start_date.date()} to {end_date.date()}"
        if graph_select == graph_options[0]:
            plot_scatterplot(df_temp, variables, states_select, title)
        elif graph_select == graph_options[1]:
            plot_lineplot(df_temp, variables, states_select, title)
        # show and download filtered data
        display_filtered_data(df_temp)
        download_filtered_data(df_temp, file_name[:-4], title)
    else:
        st.error('Error: End date must fall after start date.')


def plot_scatterplot(df, variables, states_select, title):
    # variable selection box, description of the selected variable
    y_select = selection_box('Select the variable on the y-axis', variables, index=3)
    y_description = covid_1_description[y_select]
    markdown_background(f'Variable Description: {y_description}')
    # color variable selection box, description
    color_variables = [item for item in variables if item != y_select]
    color_variables = ['None'] + color_variables
    c_select = selection_box('(Optional) Select another variable to compare with the selected y variable',
                             color_variables, index=0)

    if c_select != "None":
        c_description = covid_1_description[c_select]
        markdown_background(f'Variable Description: {c_description}')
        # plot
        fig = px.scatter(df, x='date', y=y_select, color=c_select, color_continuous_scale="reds", title=title)
    else:
        # plot
        fig = px.scatter(df, x='date', y=y_select, title=title)
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


def plot_lineplot(df, variables, states_select, title):
    linewidth = 1
    # a list of selected options
    options = multiselect_css('Select multiple variables to compare', variables, variables[0], variables[3])
    # variable descriptions
    for i in options:
        y_description = covid_1_description[i]
        markdown_background(f'{i}: {y_description}')

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


