import streamlit as st
import numpy as np
import pandas as pd
import json
from sodapy import Socrata
from utils.constants import state_abbr_full
from utils.css_utils import download_button_css


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
def convert_state_abbr_full(df, state_col='state'):
    # add a new state_fullname column
    df['state_fullname'] = [state_abbr_full[s] for s in df[state_col]]
    return df


@st.cache_data(ttl=24 * 3600)
def convert_date(df, date_col='date', date_format='%Y/%m/%d'):
    # replace the old date column with a new data column
    df[date_col] = pd.to_datetime(df[date_col], format=date_format)
    return df


@st.cache_data(ttl=24 * 3600)
def sort_df(df, cols):
    # cols: a list of column names
    df = df.sort_values(by=cols)
    return df



@st.cache_data(ttl=24 * 3600)
def convert_df_csv(df):
    return df.to_csv(index=False).encode('utf-8')


def download_filtered_data(df, file_name, filtered_conditions):
    st.markdown(download_button_css, unsafe_allow_html=True)
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
    dataset_id = client_args["dataset_identifier"]
    limit = client_args["limit"]
    args = list(client_args.keys())[2:]
    where_clause = ""
    for i in range(len(args)):
        arg = args[i]
        values = list(client_args[arg])
        s = ", ".join(f"'{v}'" for v in values)
        if i != len(args)-1:
            where_clause += f"{arg} IN ({s}) AND "
        else:
            where_clause += f"{arg} IN ({s})"
    results = client.get(dataset_id, where=where_clause, limit=limit)
    df = pd.DataFrame.from_records(results)
    # handle NA values
    na_values = ["NA", "Missing", "Unknown"]
    df = df.replace(na_values, np.nan)
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