from st_pages import add_page_title
import streamlit as st
from visualization.covid_1_vis import visualization
from utils.page_setup import display_page
from utils.data_io import read_df, read_cols, read_json

from utils.data_visual import display_dataset, display_filter_cols


page_info = read_json("data0000")
file_name = page_info["file_name"]

add_page_title(page_title=page_info["page_name"], layout="wide")

display_page(page_info)

# import dataset
df = read_df(file_name)
cols = read_cols(df)

# display data
display_dataset(df, notes="Each row has a unique state and date value pair.")

# filter dataset by column names
display_filter_cols(df, cols, "adult, pediatric")


visualization(file_name)


upload_user = page_info['upload_user']
if len(upload_user) > 1:
    st.header(f"Dataset Contributors")
    st.warning(f"{', '.join(upload_user)}")
else:
    st.header(f"Dataset Contributor")
    st.warning(f"{upload_user[0]}")
st.markdown("Thank you for uploading the dataset to Meyers Database!")
