import streamlit as st
from st_pages import add_page_title
from utils.page_setup import display_page
from utils.data_io import read_json, read_cdc_api
from utils.data_visual import display_dataset


page_info = read_json("data0002")
add_page_title(page_title=page_info["page_name"], layout="wide")
display_page(page_info)


column_description = page_info["columns"]
client_args = {"dataset_identifier": "n8mc-b4w4", "limit": 10000, "case_month": "2024-01"}

cols = st.columns(19, gap="small")
for col in cols:
    option = col.st.selectbox("How would you like to be contacted?", ("Email", "Home phone", "Mobile phone"), index=None, placeholder="Select contact method...")

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
#cdc_api = read_cdc_api(client_args)

#display_dataset(cdc_api)