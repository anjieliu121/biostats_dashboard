import streamlit as st
from PIL import Image
import json
import os
from streamlit_extras.app_logo import add_logo
from st_pages import Page, Section, add_page_title, show_pages
from utils.constants import page_title, web_description, \
    covid_page_names, flu_page_names, rsv_page_names


json_path = "~/json"
if os.path.exists(json_path) and os.path.isdir(json_path):
    st.markdown("ok")
else:
    st.markdown("not ok")

pages = [Page("app.py", page_title)]

# covid section

pages_covid = [Section(name="COVID-19", icon=":microbe:"),
               Page("pages/covid_1.py", covid_page_names["covid_1"], icon=":jigsaw:"),]

# flu section

pages_flu = [Section(name="Flu", icon=":microbe:"),
             Page("pages/flu_1.py", flu_page_names["flu_1"], icon=":jigsaw:"),]

# rsv section

pages_rsv = [Section(name="RSV", icon=":microbe:"),
             Page("pages/rsv_1.py", rsv_page_names["rsv_1"], icon=":jigsaw:"),]

# unclassified section

#Page("pages/rsv_2.py", rsv_page_names["rsv_2"], icon=":jigsaw:"),
# You can also pass in_section=False to a page to make it un-indented
#Page("example_app/example_five.py", "Example Five", "🧰", in_section=False),


# combine
pages = pages + pages_covid + pages_flu + pages_rsv
show_pages(pages)

add_page_title(layout="wide")

f"## {web_description}"

# add UT logo to the sidebar
img_path = "images/ut_logo.png"
st.sidebar.image(img_path)
