import streamlit as st
import plotly.express as px
from st_pages import add_page_title
from utils.page_setup import display_page, display_contributors
from utils.data_io import read_json, read_cols, read_cdc_api, convert_state_abbr_full, download_filtered_data, subset_df, get_unique_values
from utils.css_utils import selection_box, multiselection_box, markdown_background
from utils.data_visual import display_filtered_data, plot_bar_univariate, plot_header, display_plotly_chart
from utils.plot_utils import download_fig
import plotly.io as pio
pio.templates.default = "plotly"



page_info = read_json("data0002")
page_name = page_info["page_name"]
column_description = page_info["columns"]

add_page_title(page_title=page_name, layout="wide")
display_page(page_info)
query_limit = st.text_input('Query Limit', 1000)
st.warning(f'Since the original dataset contains more than 105 million rows, this page will only query {query_limit} rows for visualization purposes. You can edit the query limit, but be aware of the runtime.', icon="⚠️")



client_args = {"dataset_identifier": "n8mc-b4w4", "limit": query_limit}
# data query
st.header("Data Query")
st.markdown("Select variables of interest. Leave the selection blank to include all values of that variable. The value options are ranked based on their corresponding row counts.")
variables_query = ["case_month", "res_state", "age_group", "sex", "race", "ethnicity"] # variables selected for querying
cols = st.columns(len(variables_query), gap="small")

# TODO !!! There's a small bug that (1) when you check "Select all options", all options are selected;
#      (2) but then when you delete a few options,
#      (3) the "Select all options" is still checked even though it's technically not all options
for c, key in zip(cols, variables_query):
    with c:
        key_options = column_description[key]["values"]
        all_options = st.checkbox(f"Select all options", key=key)
        if all_options:
            selected_options = key_options
            options = multiselection_box(key, key_options, *selected_options)
        else:
            options = multiselection_box(key, key_options)

    if options:
        client_args[key] = options
markdown_background(f'Selected Arguments: {client_args}')
# get data using API
df = read_cdc_api(client_args)
df = convert_state_abbr_full(df, state_col='res_state')
states = list(df['state_fullname'].unique())
states.sort()
# get data using UT Box
#df = read_box()
# display data
display_filtered_data(df)
# display column description
variables = read_cols(df)
# variable selection box, description of the selected variable
option = selection_box('Select to see variable description', variables, index=0)
markdown_background(f'Variable Description: {column_description[option]["description"]}')
# download data
file_name = page_name.replace(" ", "_")
download_filtered_data(df, file_name, client_args)

########################################################################################################################
#                                               metadata plot                                                          #
########################################################################################################################


def update_categorical_axes(fig, unique_values):
    fig.update_layout(
        xaxis=dict(
            type='category',
            categoryarray=unique_values,
            tickmode='array',
            tickvals=unique_values,
            ticktext=unique_values,
        ),
    )
    fig.update_yaxes(type='category')
    return fig

graph_options = ["Unique Count for each Variable (Bar Chart)", "Observation Count across Time by State (Line Plot)"]
graph_select = plot_header(graph_options, header="Metadata Visualization")
if graph_select == graph_options[0]:
    variable_options = [v for v in variables if v not in ["res_county", "state_fips_code", "county_fips_code"]]
    option = selection_box('Select a variable to plot', variable_options, index=0)
    # plot
    plot_bar_univariate(df, option)
elif graph_select == graph_options[1]:
    # filter by states
    options = multiselection_box('Select States', states, states[1], states[4])
    df_sub = subset_df(df, 'state_fullname', *options)
    agg_df = df_sub.groupby(["case_month", "res_state"]).size().reset_index(name="count")
    # plot
    fig = px.line(agg_df, x="case_month", y="count", color="res_state")
    unique_values = get_unique_values(df, "case_month")
    update_categorical_axes(fig, unique_values)
    display_plotly_chart(fig)

########################################################################################################################
#                                               plots set up                                                           #
########################################################################################################################
graph_options = []
# if len(df["case_month"].unique()) > 1:
#
graph_options.append("Response across Time/Population Group by State (Bar Chart)")
graph_select = plot_header(graph_options)
if graph_select == graph_options[0]:
    # filter by state
    state_options = ["ALL states"] + states
    state_option = selection_box('Select one State', state_options, index=0)
    if state_option != "ALL states":
        df_sub = subset_df(df, 'state_fullname', state_option)
    else:
        df_sub = df.copy()
    # select x
    x_options = ["case_month", "age_group", "sex", "race", "ethnicity"]
    x_option = selection_box('Select one Independent Variable (x axis)', x_options, index=0)
    # select y
    y_options = [v for v in variables if v not in ["case_month", "res_state", "state_fullname", "res_county", "state_fips_code", "county_fips_code"]]
    y_options = [y for y in y_options if y != x_option]
    y_option = selection_box('Select one Response Variable (y axis)', y_options, index=0)
    unique_values = get_unique_values(df_sub, y_option)
    if unique_values:
        agg_df = df_sub.groupby([x_option, y_option]).size().reset_index(name="count")
        # plot
        fig = px.bar(agg_df, x=x_option, y="count", color=y_option)  # , barmode="group"
        unique_values = get_unique_values(df_sub, "case_month")
        #update_categorical_axes(fig, unique_values)
        display_plotly_chart(fig)
        # download fig
        title = f"{y_option} VS {x_option} IN {state_option}"
        download_fig(fig, title)
    else:
        st.warning(f"The column is empty for {state_option}. No plot can be generated. Try another state or response variable!", icon="🤨")#🔺🚫


# show people who upload the data
upload_users = page_info['upload_users']
display_contributors(upload_users)


