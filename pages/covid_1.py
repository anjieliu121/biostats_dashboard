from st_pages import add_page_title

from utils.constants import covid_file_names, covid_page_names
from visualization.covid_1_vis import dispaly_page, visualization

key = "covid_1"

add_page_title(page_title=covid_page_names[key], layout="wide")

dispaly_page(key, "12/9/2023")

visualization(covid_file_names[key])

