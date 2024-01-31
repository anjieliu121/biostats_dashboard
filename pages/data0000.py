from st_pages import add_page_title
import streamlit as st
from PIL import Image
from utils.constants import covid_file_names, covid_page_names, covid_descriptions, covid_url
from visualization.covid_1_vis import visualization
from utils.page_setup import display_page
from utils.data_io import read_df, read_cols, read_json

from utils.data_visual import display_dataset, display_filter_cols


key = "covid_1"
file_name = covid_file_names[key]

add_page_title(page_title=covid_page_names[key], layout="wide")

display_page(covid_file_names, covid_descriptions, covid_url, key, "1/29/2024")

# import dataset
df = read_df(file_name)
cols = read_cols(df)

# display data
display_dataset(df, notes="Each row has a unique state and date value pair.")

# filter dataset by column names
display_filter_cols(df, cols, "adult, pediatric")


visualization(covid_file_names[key])

page_info = read_json("data0000")
st.header(f"Dataset Contributer: {page_info['upload_user']}")
st.warning("Thank you for uploading the dataset to Meyers Database! If you have more to share, please click here (I'll update the link (eventually))")
