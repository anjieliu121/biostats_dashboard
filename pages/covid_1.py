from st_pages import add_page_title
import streamlit as st
from PIL import Image
from utils.constants import covid_file_names, covid_page_names
from visualization.covid_1_vis import dispaly_page, visualization

key = "covid_1"

add_page_title(page_title=covid_page_names[key], layout="wide")

dispaly_page(key, "12/9/2023")

visualization(covid_file_names[key])

img_path = "images/ut_logo.png"
logo = Image.open(img_path)
st.sidebar.image(img_path)