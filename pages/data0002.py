import streamlit as st
from st_pages import add_page_title
from utils.page_setup import display_page
from utils.data_io import read_json, read_cdc_api, download_filtered_data
from utils.css_utils import selection_box, markdown_background
from utils.data_visual import display_filtered_data


page_info = read_json("data0002")
page_name = page_info["page_name"]
add_page_title(page_title=page_name, layout="wide")
display_page(page_info)
st.warning('Since the original dataset contains more than 105 million rows, this page will only query 10,000 rows for visualization purposes.', icon="⚠️")


column_description = page_info["columns"]
variables = list(column_description.keys())

# variable selection box, description of the selected variable
option = selection_box('Select to see variable description', variables, index=0)
markdown_background(f'Variable Description: {column_description[option]["description"]}')
client_args = {"dataset_identifier": "n8mc-b4w4", "limit": 10000}

st.header("Data Query")
st.markdown("Select variables of interest. Leave the selection blank to include all values of that variable. The value options are ranked based on their corresponding row counts.")
for i in range(5):
    cols = st.columns(5, gap="small")
    for c, key in zip(cols, variables[0+5*i:5+5*i]):
        option = c.selectbox(key, column_description[key]["values"], index=None, placeholder="Leave it blank")
        if option:
            client_args[key] = option
markdown_background(f'Selected Arguments: {client_args}')
# get data
df = read_cdc_api(client_args)
# display data
display_filtered_data(df)
# download data
file_name = page_name.replace(" ", "_")
download_filtered_data(df, file_name, client_args)
