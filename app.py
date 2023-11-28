from st_pages import Page, Section, add_page_title, show_pages
from utils.constants import page_title, web_description, \
    covid_page_names, flu_page_names, rsv_page_names

show_pages(
    [
        Page("app.py", page_title, "🤘"),

        Section(name="COVID-19", icon=":microbe:"),
        Page("pages/covid_1.py", covid_page_names["covid_1"], icon=":jigsaw:"),

        Section(name="Flu", icon=":microbe:"),
        Page("pages/flu_1.py", flu_page_names["flu_1"], icon=":jigsaw:"),

        Section(name="RSV", icon=":microbe:"),
        Page("pages/rsv_1.py", rsv_page_names["rsv_1"], icon=":jigsaw:"),
        Page("pages/rsv_2.py", rsv_page_names["rsv_2"], icon=":jigsaw:"),
        # You can also pass in_section=False to a page to make it un-indented
        #Page("example_app/example_five.py", "Example Five", "🧰", in_section=False),
    ]
)

add_page_title(layout="wide")

f"## {web_description}"