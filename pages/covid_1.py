from st_pages import add_page_title

from utils.constants import covid_file_names, covid_page_names, covid_descriptions, covid_url
from utils.css_utils import display_data_description, display_download_button
from utils.visualization_utils import univariate_distribution, multivariate_distribution, display_dataset, display_source

key = "covid_1"
file_name = covid_file_names[key]

add_page_title(page_title=covid_page_names[key], layout="wide")

display_data_description(covid_descriptions[key])

display_download_button(file_name)


univariate_distribution(file_name)
multivariate_distribution(file_name)
display_dataset(file_name)
display_source(covid_url[key])
