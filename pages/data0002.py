import streamlit as st
from st_pages import add_page_title
from utils.page_setup import display_page
from utils.data_io import read_json, read_cdc_api
from utils.css_utils import selection_box, markdown_background
from utils.data_visual import display_dataset


page_info = read_json("data0002")
add_page_title(page_title=page_info["page_name"], layout="wide")
display_page(page_info)


column_description = page_info["columns"]
variables = list(column_description.keys())

# variable selection box, description of the selected variable
option = selection_box('Select to see variable description', variables, index=0)
markdown_background(f'Variable Description: {column_description[option]}')
client_args = {"dataset_identifier": "n8mc-b4w4", "limit": 10000, "case_month": "2024-01"}

st.header("Data Query")
for i in range(5):
    cols = st.columns(5, gap="small")
    for c, key in zip(cols, variables[0+5*i:5+5*i]):
        option = c.selectbox(key, ("Email", "Home phone", "Mobile phone"), index=None, placeholder="Leave it blank")
#cdc_api = read_cdc_api(client_args)

#display_dataset(cdc_api)