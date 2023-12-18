import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import io
from utils.css_utils import display_data_description, display_download_button, selection_box, markdown_background, multiselect_css
from utils.visualization_utils import display_dataset, display_source, read_df, display_plotly_chart, download_fig
from utils.constants import covid_file_names, covid_descriptions, covid_url, state_abbr_full, covid_1_description

def dispaly_page(key, date):
    file_name = covid_file_names[key]
    display_data_description(covid_descriptions[key])
    display_source(covid_url[key])
    display_download_button(file_name, date)
    notes = "Each row has a unique state and date value pair."
    display_dataset(file_name, notes)



def visualization(file_name):
    # header
    st.header("Interactive Multivariate Visualization")
    # warning
    st.warning('Minimize the sidebar to the left by clicking \'X\' for the best plot view.', icon="⚠️")
    # plot options
    graph_options = ["Colored Scatter Plot", "Multi-Line Plot"]
    graph_select = selection_box('Select Plot Option', graph_options, index=0)

    # import dataset
    df = read_df(file_name)
    df['state_fullname'] = [state_abbr_full[s] for s in df['state']]
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df = df.sort_values(by=['state', 'date'])
    variables = df.columns[2:-2]

    # create state selection box
    states = sorted(df['state_fullname'].unique())
    index_Texas = states.index('Texas')
    states_select = selection_box('Select State/Federal district/Inhabited territories in the U.S.', states, index=index_Texas)
    df_temp = df[df['state_fullname'] == states_select]

    # date range
    start = min(df_temp['date'])
    end = max(df_temp['date'])
    start_date = st.date_input('Start date', start, min_value=start, max_value=end)
    end_date = st.date_input('End date', end, min_value=start, max_value=end)
    if start_date < end_date:
        start_date, end_date = pd.Timestamp(start_date), pd.Timestamp(end_date)
        df_temp = df_temp[df_temp['date'].between(start_date, end_date)]
        # title
        title = f"{states_select} from {start_date.date()} to {end_date.date()}"
        if graph_select == graph_options[0]:
            plot_scatterplot(df_temp, variables, states_select, title)
        elif graph_select == graph_options[1]:
            plot_lineplot(df_temp, variables, states_select, title)
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
                             color_variables, index=3)

    if c_select != "None":
        c_description = covid_1_description[c_select]
        markdown_background(f'Variable Description: {c_description}')
        # plot
        fig = px.scatter(df, x='date', y=y_select, color=c_select, color_continuous_scale="reds", title=title)
    else:
        # plot
        fig = px.scatter(df, x='date', y=y_select)
    fig = display_plotly_chart(fig)
    # download fig
    title = f"{title}-{y_select}-{c_select}"
    download_fig(fig, title)


def plot_lineplot(df, variables, states_select, title):
    linewidth = 1
    # a list of selected options
    options = multiselect_css('Select multiple variables to compare', variables)
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
