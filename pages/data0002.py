import streamlit as st
from st_pages import add_page_title
from utils.page_setup import display_page
from utils.data_io import read_json, read_cols, read_cdc_api, download_filtered_data
from utils.css_utils import selection_box, multiselection_box, markdown_background
from utils.data_visual import display_filtered_data, plot_bar_univariate

query_limit = 1000

page_info = read_json("data0002")
page_name = page_info["page_name"]
add_page_title(page_title=page_name, layout="wide")
display_page(page_info)
st.warning(f'Since the original dataset contains more than 105 million rows, this page will only query {query_limit} rows for visualization purposes.', icon="⚠️")


column_description = page_info["columns"]
variables = list(column_description.keys())

# variable selection box, description of the selected variable
option = selection_box('Select to see variable description', variables, index=0)
markdown_background(f'Variable Description: {column_description[option]["description"]}')
client_args = {"dataset_identifier": "n8mc-b4w4", "limit": query_limit}
# data query
st.header("Data Query")
st.markdown("Select variables of interest. Leave the selection blank to include all values of that variable. The value options are ranked based on their corresponding row counts.")
variables_query = ["case_month", "res_state", "age_group", "sex", "race", "ethnicity"] # variables selected for querying
cols = st.columns(len(variables_query), gap="small")
for c, key in zip(cols, variables_query):
    #option = c.selectbox(key, column_description[key]["values"], index=None, placeholder="Leave it blank")
    with c:
        key_options = column_description[key]["values"]
        options = multiselection_box(key, key_options)
    if options:
        client_args[key] = options
markdown_background(f'Selected Arguments: {client_args}')
# get data using API
df = read_cdc_api(client_args)
# get data using UT Box
#df = read_box()
# display data
display_filtered_data(df)
# download data
file_name = page_name.replace(" ", "_")
download_filtered_data(df, file_name, client_args)

# univariate visualization
st.header("Plot Univariate Distribution")
variables = read_cols(df)
variable_options = [v for v in variables if v not in ["res_county", "state_fips_code", "county_fips_code"]]
#variable_options = ["age_group"]
option = selection_box('Select a variable to plot', variable_options, index=0)
plot_bar_univariate(df, option)

