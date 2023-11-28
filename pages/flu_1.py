from st_pages import add_page_title
from utils.constants import flu_file_names, flu_page_names, flu_descriptions
from utils.css_utils import display_data_description, display_download_button
from utils.visualization_utils import univariate_distribution, multivariate_distribution, display_dataset

key = "flu_1"
file_name = flu_file_names[key]

add_page_title(page_title=flu_page_names[key], layout="wide")

display_data_description(flu_descriptions[key])

display_download_button(file_name)

univariate_distribution(file_name)
multivariate_distribution(file_name)
display_dataset(file_name)
