import streamlit as st
import numpy as np
import plotly.express as px
from utils.constants import fig_height
from utils.css_utils import markdown_background, selection_box
from utils.data_io import read_df, read_cols, subset_df_col


def plot_header(graph_options):
    # header
    st.header("Interactive Multivariate Visualization")
    # warning
    st.warning('Minimize the sidebar to the left by clicking \'×\' for the best plot view.', icon="⭐")
    # plot options
    graph_select = selection_box('Select Plot Option', graph_options, index=0)
    return graph_select


def display_filter_cols(df, cols, sample_search_text):
    st.header("Filter Dataset by Column Names")
    st.warning("Filtered columns will not affect the column options in the visualization below.", icon="⚠️")
    search_phrases = st.text_input('I want column names that contain phrases like ... (separate each word by a comma)', sample_search_text)
    search_list = search_phrases.split(", ")
    cols_select = [col for col in cols if any(word in col for word in search_list)]
    df = subset_df_col(df, cols_select)
    st.dataframe(df, use_container_width=True, height=265)



@st.cache_data(ttl=24 * 3600)
def display_plotly_chart(fig, fig_height=fig_height):
    fig.update_layout(height=fig_height)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True, height=fig_height)
    return fig


@st.cache_data(ttl=24 * 3600)
def plot_bar_univariate(df, option):
    unique_values = df[option].unique()
    unique_values = [x for x in unique_values if x == x]
    st.markdown(unique_values)
    fig = px.bar(df, x=option)
    fig.update_layout(
        xaxis=dict(
            categoryorder="total ascending",
            categoryarray=unique_values,
            #tickmode='array',
            tickvals=unique_values,
            ticktext=unique_values,
            tickangle=45
        ),
    ),
    # fig.update_xaxes(categoryorder="total descending")
    display_plotly_chart(fig)



@st.cache_data(ttl=24 * 3600)
def plot_timeseries(df, x, var_select, title, color):
    if color:
        fig = px.scatter(df, x=x, y=var_select, color=color, title=title)
    fig.update_layout(
        title={
            'text': title,
            'y': 0.95,
            'x': 0.35,
            'xanchor': 'center',
            'yanchor': 'top'},
    )
    fig = display_plotly_chart(fig)
    return fig


@st.cache_data(ttl=24 * 3600)
def plot_lines(df, x, vars_select, title, color, cvars_select):
    if color:
        # add first selected variable with all selected age groups
        fig = px.line(df, x=x, y=vars_select[0], color=color)
        newnames = {key: f"{vars_select[0]}:{key}" for key in cvars_select}
        fig.for_each_trace(lambda t: t.update(name=newnames[t.name],
                                              legendgroup=newnames[t.name]))

        for i in range(1, len(vars_select)):
            line_trace = px.line(df, x=x, y=vars_select[i], color=color)
            newnames = {key: f"{vars_select[i]}:{key}" for key in cvars_select}
            line_trace.for_each_trace(lambda t: t.update(name=newnames[t.name],
                                                         legendgroup=newnames[t.name]))
            for j in range(len(cvars_select)):
                fig.add_trace(line_trace.data[j])
    fig.update_layout(
        title={
            'text': title,
            'y': 0.95,
            'x': 0.35,
            'xanchor': 'center',
            'yanchor': 'top'},
    )
    fig = display_plotly_chart(fig)
    return fig


@st.cache_data(ttl = 24 * 3600)
def plot_bar(df, x, y, title):
    fig = px.bar(df, y=y, x=x, text=y)
    fig.update_traces(textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_layout(
        title={
            'text': title,
            'y': 0.95,
            'x': 0.35,
            'xanchor': 'center',
            'yanchor': 'top'},
    )
    fig = display_plotly_chart(fig)
    return fig


def display_dataset(df, notes=None):
    st.header("Quick Glance at the Raw Data")
    st.dataframe(df, use_container_width=True, height=265)
    if notes is not None:
        st.caption(f"Note: {notes}")


def display_filtered_data(df):
    st.header("Quick Glance at the Filtered Data")
    st.dataframe(df, use_container_width=True)




def multivariate_distribution(file_name):
    df = read_df(file_name)
    cols = read_cols(df)

    st.header("Multivariate Visualization")
    col_select1 = st.selectbox('Select the first variable (x)', cols, index=3)
    col_select2 = st.selectbox('Select the second variable (y)', cols, index=4)
    col_select3 = st.selectbox('(Optional) Select the third variable', cols, index=None,
                               placeholder="(Optional) select colormap")
    if not col_select3:
        fig = px.scatter(df, x=col_select1, y=col_select2)
    else:
        fig = px.scatter(df, x=col_select1, y=col_select2, color=col_select3, color_continuous_scale="reds")
    display_plotly_chart(fig)



