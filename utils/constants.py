########################################################################################################################
#                                              starter page info                                                       #
########################################################################################################################



########################################################################################################################
#                                              COVID                                                                   #
########################################################################################################################


########################################################################################################################
#                                              FLU                                                                   #
########################################################################################################################

flu_file_names = {
    "flu_1": "Age_Specific_Coverage_Flu_RD4_2023_24_Sc_A_B_C_D_E_F.csv"
}

flu_page_names = {
    "flu_1": "Age Specific Coverage Flu RD4 2023-24"
}

flu_url = {
    "flu_1": "https://github.com/midas-network/flu-scenario-modeling-hub_resources/blob/main/Rd4_datasets/Age_Specific_Coverage_Flu_RD4_2023_24_Sc_A_B_C_D_E_F.csv"
}

flu_descriptions = {
    "flu_1": "This dataset contains _simulated_ influenza vaccine coverage data in fall-winter 2023-2024. The data provides weekly cumulative coverages by state and adult and child age groups. Estimates are based on the reported coverage of the flu vaccine in the 2021-2022 fall season by month, state, and age. We used a Piecewise Cubic Hermite Interpolating Polynomial to generate weekly coverage estimates from monthly data. Dates have been shifted to reflect projection weeks in the 2023-2024 season. The data in this file can be used as is (no adjustment to coverage should be needed). Age groups can be collapsed based on provided population sizes."
}
########################################################################################################################
#                                              rsv                                                                   #
########################################################################################################################

rsv_file_names = {
    "rsv_1": "Weekly_Rates_of_Laboratory-Confirmed_RSV_Hospitalizations_from_the_RSV-NET_Surveillance_System_22_24_overall.csv",
    "rsv_2": "Weekly_Rates_of_Laboratory-Confirmed_RSV_Hospitalizations_from_the_RSV-NET_Surveillance_System_22_24.csv"
}

rsv_page_names = {
    "rsv_1": "Weekly Rates of Laboratory Confirmed RSV Hospitalizations from the RSV-NET Surveillance System 2022-24 Overall",
    "rsv_2": "Weekly Rates of Laboratory Confirmed RSV Hospitalizations from the RSV-NET Surveillance System 2022-24"
}

rsv_url = {
    "rsv_1": "https://data.cdc.gov/Public-Health-Surveillance/Weekly-Rates-of-Laboratory-Confirmed-RSV-Hospitali/29hc-w46k"
}

rsv_descriptions = {
    "rsv_1": "The Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) is a network that conducts active, population-based surveillance for laboratory-confirmed RSV-associated hospitalizations in children younger than 18 years of age and adults. The network currently includes 58 counties in 12 states, and data are collected and reported during the October 1-April 30 season each year. In some years, additional months of data are collected. In adults, RSV hospitalization tracking began in the 2016–2017 season. In children less than 18 years of age, surveillance began in the 2018–19 season. Because the surveillance areas and age groups included in surveillance have changed over time, trends should be interpreted with caution. Hospitalization data are preliminary and subject to change as more data become available. In particular, case counts and rates for recent hospitalizations are subject to lag. Lag for RSV-NET case identification and reporting might increase around holidays or during periods of increased hospitalization utilization. Check the source link for the most updated dataset.",
    "rsv_2": ""
}
########################################################################################################################
#                                              PLOT                                                                   #
########################################################################################################################

fig_height = 800
title_fontsize = 40
tick_fontsize = 20

# state - abbreviation : full name
state_abbr_full = {'AL': 'Alabama',
 'AK': 'Alaska',
 'AS': 'American Samoa',
 'AZ': 'Arizona',
 'AR': 'Arkansas',
 'CA': 'California',
 'CO': 'Colorado',
 'CT': 'Connecticut',
 'DE': 'Delaware',
 'DC': 'District of Columbia',
 'FL': 'Florida',
 'GA': 'Georgia',
 'HI': 'Hawaii',
 'ID': 'Idaho',
 'IL': 'Illinois',
 'IN': 'Indiana',
 'IA': 'Iowa',
 'KS': 'Kansas',
 'KY': 'Kentucky',
 'LA': 'Louisiana',
 'ME': 'Maine',
 'MD': 'Maryland',
 'MA': 'Massachusetts',
 'MI': 'Michigan',
 'MN': 'Minnesota',
 'MS': 'Mississippi',
 'MO': 'Missouri',
 'MT': 'Montana',
 'NE': 'Nebraska',
 'NV': 'Nevada',
 'NH': 'New Hampshire',
 'NJ': 'New Jersey',
 'NM': 'New Mexico',
 'NY': 'New York',
 'NC': 'North Carolina',
 'ND': 'North Dakota',
 'OH': 'Ohio',
 'OK': 'Oklahoma',
 'OR': 'Oregon',
 'PA': 'Pennsylvania',
 'RI': 'Rhode Island',
 'SC': 'South Carolina',
 'SD': 'South Dakota',
 'TN': 'Tennessee',
 'TX': 'Texas',
 'UT': 'Utah',
 'VT': 'Vermont',
 'VA': 'Virginia',
 'WA': 'Washington',
 'WV': 'West Virginia',
 'WI': 'Wisconsin',
 'WY': 'Wyoming',
 'PR': 'Puerto Rico',
 'VI': 'U.S. Virgin Islands'}




