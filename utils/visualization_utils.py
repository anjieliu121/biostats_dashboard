import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from utils.constants import fig_height, title_fontsize, tick_fontsize
from utils.css_utils import markdown_background
import io

def display_source(url):
    # components.iframe(link)
    st.markdown("Source: [link](%s)" % url)


def read_df(file_name):
    df = pd.read_csv(f"data/{file_name}")
    return df


def read_cols(df):
    cols = np.array(df.columns)
    return cols


def display_plotly_chart(fig, fig_height=fig_height, title_fontsize=title_fontsize, tick_fontsize=tick_fontsize):
    fig.update_layout(height=fig_height)
    #fig.update_xaxes(title_font=dict(size=title_fontsize), tickfont=dict(size=tick_fontsize))
    #fig.update_yaxes(title_font=dict(size=title_fontsize), tickfont=dict(size=tick_fontsize))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True, height=fig_height)
    return fig


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


def display_dataset(file_name, notes=None):
    df = read_df(file_name)
    st.header("Quick Glance at the Raw Data")
    st.dataframe(df, use_container_width=True)
    if notes is not None:
        markdown_background(f"Note: {notes}")


def download_fig(fig, title):
    buffer = io.StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    html_bytes = buffer.getvalue().encode()

    st.download_button(
        label='Download HTML',
        data=html_bytes,
        file_name=f'{title}.html',
        mime='text/html'
    )
    col1, col2 = st.columns([1, 1])

    # Use the first column for text input
    with col1:
        plt_width = st.text_input(
            "Enter Desired Plot Width in Pixels",
            value="900",
            placeholder="900",
            # label_visibility='collapsed'
        )
    # Use the second column for the submit button
    with col2:
        plt_height = st.text_input(
            "Enter Desired Plot Height in Pixels",
            value="500",
            placeholder="500",
            # label_visibility='collapsed'
        )
    # update fig height
    width = int(plt_width)
    height = int(plt_height)
    fig.update_layout(height=height, width=width)
    # buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        # PDF
        buffer = io.BytesIO()
        fig.write_image(file=buffer, format="pdf")
        st.download_button(
            label="Download PDF",
            data=buffer,
            file_name=f"{title}.pdf",
            mime="application/pdf",
        )
    with col2:
        # PNG
        buffer = io.BytesIO()
        fig.write_image(file=buffer, format="png")
        st.download_button(
            label="Download PNG",
            data=buffer,
            file_name=f"{title}.png",
            mime="application/png",
        )