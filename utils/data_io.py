import streamlit as st
import numpy as np
import pandas as pd

from utils.constants import state_abbr_full


@st.cache_data(ttl=24 * 3600)
def read_df(file_name):
    df = pd.read_csv(f"data/{file_name}")
    return df


@st.cache_data(ttl=24 * 3600)
def read_cols(df):
    cols = np.array(df.columns)
    return cols


@st.cache_data(ttl=24 * 3600)
def subset_df(df, col, condition):
    # state = Texas
    df = df[df[col] == condition]
    return df


@st.cache_data(ttl=24 * 3600)
def subset_df_date(df, col, start, end):
    df = df[df[col].between(start, end)]
    return df


@st.cache_data(ttl=24 * 3600)
def customize_df_covid1(df):
    df['state_fullname'] = [state_abbr_full[s] for s in df['state']]
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df = df.sort_values(by=['state', 'date'])
    return df


