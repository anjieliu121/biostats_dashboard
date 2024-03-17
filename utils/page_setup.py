import streamlit as st
from utils.css_utils import display_download_button
from utils.text_utils import display_data_description, display_source


def display_page(page_info):
    file_name = page_info["file_name"]
    display_data_description(page_info["description"])
    display_source(page_info["source"])
    if file_name != "NONE":
        display_download_button(file_name, page_info["local_file_update_date"])

    img_path = "images/ut_logo.png"
    st.sidebar.image(img_path)


def add_sidebar_image():
    img_path = "images/ut_logo.png"
    st.sidebar.image(img_path)


def display_contributors(upload_users):
    if len(upload_users) > 1:
        st.header(f"Dataset Contributors")
        st.warning(f"{', '.join(upload_users)}")
    else:
        st.header(f"Dataset Contributor")
        st.warning(f"{upload_users[0]}")
    st.markdown("Thank you for uploading the dataset to Meyers Database!")