ut_colors = {
    "burnt_orange": "#bf5700"
}
# web page title
page_title = "Bioinformatics Database"
# table of contents
overview_tabs = [
    "Overview",
    # "🦈",
    "Data",
    # "A long loooooong tab",
    # "🎨",
    # "x²"
]
# whitespace between tabs
whitespace = 9
# webpage description
web_description = "This database contains the datasets and interactive data visualization."
# data name
# file name : [tab name, readable header]
data_names = {
    "COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries__RAW_ (1).csv":
        ["COVID-19",
         "COVID-19 Reported Patient Impact and Hospital Capacity by State Timeseries",
         "1-sentence description",
         "longer description"],
    "Age_Specific_Coverage_Flu_RD4_2023_24_Sc_A_B_C_D_E_F.csv":
        ["Flu",
         "Age Specific Coverage Flu RD4 2023-24",
         "1-sentence description",
         "longer description"],
    "Weekly_Rates_of_Laboratory-Confirmed_RSV_Hospitalizations_from_the_RSV-NET_Surveillance_System_22_24_overall.csv":
        ["RSV Overall",
         "Weekly Rates of Laboratory Confirmed RSV Hospitalizations from the RSV-NET Surveillance System 2022-24 Overall",
         "1-sentence description",
         "longer description"],
    "Weekly_Rates_of_Laboratory-Confirmed_RSV_Hospitalizations_from_the_RSV-NET_Surveillance_System_22_24.csv":
        ["RSV",
         "Weekly Rates of Laboratory Confirmed RSV Hospitalizations from the RSV-NET Surveillance System 2022-24",
         "1-sentence description",
         "longer description"],
}

covid_file_names = {
    "covid_1": "COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries__RAW_ (1).csv"
}

covid_page_names = {
    "covid_1": "COVID-19 Reported Patient Impact and Hospital Capacity by State Timeseries"
}

covid_url = {
    "covid_1" : "https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh"

}

covid_descriptions = {
    "covid_1": "The following dataset provides state-aggregated data for hospital utilization in a timeseries format dating back to January 1, 2020. These are derived from reports with facility-level granularity across three main sources: (1) HHS TeleTracking, (2) reporting provided directly to HHS Protect by state/territorial health departments on behalf of their healthcare facilities and (3) National Healthcare Safety Network (before July 15). Check the source link for the most updated dataset."
}

flu_file_names = {
    "flu_1": "Age_Specific_Coverage_Flu_RD4_2023_24_Sc_A_B_C_D_E_F.csv"
}

flu_page_names = {
    "flu_1": "Age Specific Coverage Flu RD4 2023-24"
}

flu_descriptions = {
    "flu_1": "longer description"
}

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
    "rsv_2": "longer description"
}

fig_height = 1200
title_fontsize = 40
tick_fontsize = 20