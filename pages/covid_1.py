from st_pages import add_page_title
import streamlit as st
from PIL import Image
from utils.constants import covid_file_names, covid_page_names, covid_descriptions, covid_url
from visualization.covid_1_vis import visualization
from utils.page_setup import display_page


key = "covid_1"

add_page_title(page_title=covid_page_names[key], layout="wide")

display_page(covid_file_names, covid_descriptions, covid_url, key, "1/29/2024", "Each row has a unique state and date value pair.")

visualization(covid_file_names[key])

