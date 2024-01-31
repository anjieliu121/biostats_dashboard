import streamlit as st
from utils.css_utils import display_download_button
from utils.text_utils import display_data_description, display_source


def display_page(file_names, descriptions, urls, key, update_date):
    file_name = file_names[key]
    display_data_description(descriptions[key])
    display_source(urls[key])
    display_download_button(file_name, update_date)

    img_path = "images/ut_logo.png"
    st.sidebar.image(img_path)