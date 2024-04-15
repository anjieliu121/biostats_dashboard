import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
import streamlit.components.v1 as components
from PIL import Image
import webbrowser
from utils.data_io import read_json
from utils.page_setup import add_sidebar_image


# load database information
database_info = read_json("database_info")
dataset_cnt = database_info["dataset_count"]
sections = database_info["sections"]

# initiate a list of pages
pages = [Page("app.py", database_info["page_title"])]

# add each page to the list of pages
for section in sections:
    pages.append(Section(name=section, icon=":microbe:"))
    for page in sections[section]:
        page_info = read_json(page)
        page_type = page_info["type"]
        if page_type == "real":
            icon = ":telescope:"  # ":earth_americas:"
        elif page_type == "simulated":
            icon = ":hammer_and_wrench:"
        else:
            icon = ":jigsaw:"
        pages.append(Page(f"pages/{page}.py", page_info["page_name"], icon=icon))

# display all pages
show_pages(pages)
add_page_title(layout="wide")

# add UT logo to the sidebar
add_sidebar_image()

########################################################################################################################
#                                               Introductory Page                                                      #
########################################################################################################################
col1, col2 = st.columns([0.15, 0.85])
with col1:
    # logo
    st.image('images/meyerslab_logo_circle.png')
with col2:
    # description
    f"## {database_info["web_description"]}"

st.divider()

# emoji keys
st.header("What does the emoji before each page mean?")
st.markdown(":telescope: real-world data")
st.markdown(":hammer_and_wrench: simulated data")
st.divider()


# contact info
st.header("Contact Us")
# embedded meyers lab
iframe_src = "http://www.bio.utexas.edu/research/meyers/index.html"
components.iframe(iframe_src, height=400, scrolling=True)
# linkedin link
st.link_button(f"Contact Web Creator 👈", "https://www.linkedin.com/in/anjie-liu-a73574253/")