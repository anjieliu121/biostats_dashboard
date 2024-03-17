import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
from utils.constants import page_title, web_description
from utils.data_io import read_json
from utils.page_setup import add_sidebar_image

# initiate a list of pages
pages = [Page("app.py", page_title)]

# load database information
database_info = read_json("database_info")
dataset_cnt = database_info["dataset_count"]
sections = database_info["sections"]

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

# unclassified section

# Page("pages/rsv_2.py", rsv_page_names["rsv_2"], icon=":jigsaw:"),
# You can also pass in_section=False to a page to make it un-indented
# Page("example_app/example_five.py", "Example Five", "🧰", in_section=False),

# display all pages
show_pages(pages)
add_page_title(layout="wide")

# add UT logo to the sidebar
add_sidebar_image()

########################################################################################################################
#                                               Introductory Page                                                      #
########################################################################################################################
f"## {web_description}"
st.divider()

# emoji keys
st.header("What does the emoji before each page mean?")
st.markdown(":telescope: real-world data")
st.markdown(":hammer_and_wrench: simulated data")
