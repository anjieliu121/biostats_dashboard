import streamlit as st
import numpy as np
import pandas as pd
import json
from sodapy import Socrata
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
def subset_df(df, col, *conditions):
    # state = Texas
    df = df[df[col].isin(conditions)]
    return df


@st.cache_data(ttl=24 * 3600)
def subset_df_date(df, col, start, end):
    df = df[df[col].between(start, end)]
    return df


@st.cache_data(ttl=24 * 3600)
def subset_df_col(df, cols_select):
    return df[cols_select]



@st.cache_data(ttl=24 * 3600)
def customize_df_covid1(df):
    df['state_fullname'] = [state_abbr_full[s] for s in df['state']]
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df = df.sort_values(by=['state', 'date'])
    return df


@st.cache_data(ttl=24 * 3600)
def convert_df_csv(df):
    return df.to_csv(index=False).encode('utf-8')


def download_filtered_data(df, file_name, filtered_conditions):
    csv = convert_df_csv(df)

    st.download_button(
        "Download Filtered Data",
        csv,
        f"{file_name}_{filtered_conditions}.csv",
        "text/csv",
        key='download-csv'
    )


@st.cache_data(ttl=24 * 3600)
def read_json(file_name):
    f = open(f"json/{file_name}.json")
    d = json.load(f)
    f.close()
    return d


@st.cache_data(ttl=24 * 3600)
def read_cdc_api(client_args):
    client = Socrata("data.cdc.gov", None)
    results = client.get(**client_args)
    df = pd.DataFrame.from_records(results)
    return df

"""
json_path = "https://github.com/anjieliu121/biostats_dashboard/blob/5c486334a84c1507977d1298108e1ba767f075ec/json"
response = requests.get(json_path)
if response.status_code == 200:
    files_info = response.json()
    # Iterate over each file in the folder
    json_files = files_info["payload"]["tree"]
    json_files_cnt = json_files["totalCount"]
    for json_file in json_files["items"]:
        # Get the raw content URL for each file
        name = json_file["name"]
        full_path = f"{json_path}/{name}"
        # Make a request to the raw content URL to get the file content
        file_response = requests.get(full_path)
        if file_response.status_code == 200:
            # Parse the JSON content of the file
            file_data = json.loads(file_response.text)
            st.markdown(file_data)
else:
    st.markdown("cannot access data files")
    
"""