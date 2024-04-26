# estimate = y, x = date, geographi
# filter = indicator category label
import streamlit as st
import plotly.express as px
from st_pages import add_page_title
import plotly.io as pio
pio.templates.default = "plotly"

from utils.page_setup import add_sidebar_image, display_contributors
from utils.css_utils import display_download_button, selection_box, markdown_background, multiselection_box
from utils.text_utils import display_data_description, display_source
from utils.data_visual import display_dataset, display_filter_cols, plot_header, display_plotly_chart, display_filtered_data, plot_bar_univariate, plot_timeseries_line
from utils.data_io import read_json, read_df, read_cols, subset_df, subset_df_date, convert_state_abbr_full, convert_date, sort_df, convert_df_csv, download_filtered_data
from utils.plot_utils import download_fig

########################################################################################################################
#                                               set up                                                                 #
########################################################################################################################
page_info = read_json("data0003")
file_name = page_info["file_name"]
columns = page_info["columns"]
numeric = page_info["numeric_columns"]
add_page_title(page_title=page_info["page_name"], layout="wide")
add_sidebar_image()

# show data description and its source
display_data_description(page_info["description"])
display_source(page_info["source"])

# show download data button
display_download_button(file_name, page_info["local_file_update_date"])

# import dataset
df = read_df(file_name)
cols = list(columns.keys())

# display data
display_dataset(df, notes="Each row has a unique value pair of (Geographic Name, Demographic Level, Demographic Name, indicator_category_label, Month_Week).")

# filter dataset by column names
display_filter_cols(df, cols, "name, indicator")
########################################################################################################################
#                                               plots set up                                                           #
########################################################################################################################
graph_options = ["Estimates Over Time", "Colored Bar Chart by Categories"]
graph_select = plot_header(graph_options)

# transform data
df = convert_date(df, date_col='Week_ending', date_format="%m/%d/%Y %I:%M:%S %p")
# main filter by indicator_category_label
indicator_option = selection_box('Select Indicator Category Label', df['indicator_category_label'].unique(), index=0)
df_sub = subset_df(df, 'indicator_category_label', indicator_option)
########################################################################################################################
#                                               bar chart                                                              #
########################################################################################################################
if graph_select == graph_options[0]:
    # main filter by state
    state_option = selection_box('Select Geographic Name', df['Geographic Name'].unique(), index=0)
    df_sub = subset_df(df_sub, 'Geographic Name', state_option)
    # sort df_sub by week_ending
    df_sub = sort_df(df_sub, ['Week_ending'])
    plot_timeseries_line(df_sub, x='Week_ending', y="Estimate", title="Estimates Over Time")
    display_filtered_data(df_sub, False)
if graph_select == graph_options[1]:
    # select a filter
    filters = ['NONE (Entire Dataset)', 'Geographic Level', 'Geographic Name', 'Demographic Level', 'Demographic Name', 'indicator_label', 'Week_ending', 'suppression_flag']
    filter_option = selection_box('Select Filter', filters, index=0)
    if filter_option != filters[0]:
        # select filter categories
        c = columns[filter_option]['values']
        c_options = multiselection_box('Select Categories of Interest', c, c[0])
        df_sub = subset_df(df_sub, filter_option, *c_options)

    # select a variable
    cols_except_filter = ['Estimate']
    option = selection_box('Select Variable', cols_except_filter, index=0)

    if filter_option != filters[0]:
        if df_sub.empty:
            st.warning("Please select something to plot.")
        else:
            if option in numeric:
                fig = px.histogram(df_sub, x=option, color=filter_option)
                display_plotly_chart(fig)
            else:
                agg_df = df_sub.groupby([option, filter_option]).size().reset_index(name="count")
                fig = px.bar(agg_df, x=option, y="count", color=filter_option)  # , barmode=
                display_plotly_chart(fig)
                display_filtered_data(agg_df, header=False)
    else:
        # plot
        if option in numeric:
            fig = px.histogram(df, option)
            display_plotly_chart(fig)
        else:
            plot_bar_univariate(df, option)

# show people who upload the data
upload_users = page_info['upload_users']
display_contributors(upload_users)

