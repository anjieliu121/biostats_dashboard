import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from utils.constants import fig_height, title_fontsize, tick_fontsize


def display_source(url):
    #components.iframe(link)
    st.header("Source: [link](%s)" % url)

def read_df(file_name):
    df = pd.read_csv(f"data/{file_name}")
    return df


def read_cols(df):
    cols = np.array(df.columns)
    return cols


def display_plotly_chart(fig, fig_height=fig_height, title_fontsize=title_fontsize, tick_fontsize=tick_fontsize):
    fig.update_layout(height=fig_height)
    fig.update_xaxes(title_font=dict(size=title_fontsize), tickfont=dict(size=tick_fontsize))
    fig.update_yaxes(title_font=dict(size=title_fontsize), tickfont=dict(size=tick_fontsize))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True, height=fig_height)


def univariate_distribution(file_name):
    df = read_df(file_name)
    cols = read_cols(df)

    st.markdown("""
        	<style>
        	.stSelectbox:first-of-type > div[data-baseweb="select"] > div {
        	      background-color: #bf5700;
            	  padding: 10px;
        	}
        	</style>
        """, unsafe_allow_html=True)

    st.header("Univariate Visualization")
    col_select = st.selectbox("Univariate Distribution", cols, label_visibility="collapsed")

    fig = px.histogram(df, x=col_select)
    display_plotly_chart(fig)


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


def display_dataset(file_name):
    df = read_df(file_name)
    st.header("Quick Glance at the Data")
    st.dataframe(df, use_container_width=True)
