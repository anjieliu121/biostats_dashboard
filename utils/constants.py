########################################################################################################################
#                                              starter page info                                                       #
########################################################################################################################
# web page title
page_title = "Meyers Database"
# webpage description
web_description = "Meyers Database portal provides description and interactive visualization of data used in \
                   scenario hub, forecast or other scientific projects."

########################################################################################################################
#                                              PLOT                                                                    #
########################################################################################################################
graph_options = ["Timeseries Plot", "Multi-Line Plot"]

########################################################################################################################
#                                              COVID                                                                   #
########################################################################################################################
covid_file_names = {
    "covid_1": "COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries__RAW.csv"
}

covid_page_names = {
    "covid_1": "COVID-19 Reported Patient Impact and Hospital Capacity by State Timeseries"
}

covid_url = {
    "covid_1": "https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh"

}

covid_descriptions = {
    "covid_1": "This dataset provides state-aggregated data for __hospital utilization__ in a timeseries format dating back to _January 1, 2020_. These are derived from reports with facility-level granularity across three main sources: (1) HHS TeleTracking, (2) reporting provided directly to HHS Protect by state/territorial health departments on behalf of their healthcare facilities and (3) National Healthcare Safety Network (before July 15). After _Friday September 29th, 2023_, as a result of changes in reporting cadence, this dataset will be updated twice a week on Wednesdays and Fridays."
}

covid_1_description = {
    'critical_staffing_shortage_today_yes': 'Number of hospitals reporting a critical staffing shortage today in this state.',
    'critical_staffing_shortage_today_no': 'Number of hospitals reporting as not having a critical staffing shortage today in this state.',
    'critical_staffing_shortage_today_not_reported': 'Number of hospitals not reporting staffing shortage today status in this state.',
    'critical_staffing_shortage_anticipated_within_week_yes': 'Number of hospitals reporting that they anticipate a critical staffing shortage within a week in this state.',
    'critical_staffing_shortage_anticipated_within_week_no': 'Number of hospitals reporting that they do not anticipate a critical staffing shortage within a week in this state.',
    'critical_staffing_shortage_anticipated_within_week_not_reported': 'Number of hospitals not reporting staffing shortage within week status in this state.',
    'hospital_onset_covid': 'Total current inpatients with onset of suspected or laboratory-confirmed COVID-19 fourteen or more days after admission for a condition other than COVID-19 in this state.',
    'hospital_onset_covid_coverage': 'Number of hospitals reporting "hospital_onset_covid" in this state',
    'inpatient_beds': 'Reported total number of staffed inpatient beds including all overflow and surge/expansion beds used for inpatients (includes all ICU beds) in this state',
    'inpatient_beds_coverage': 'Number of hospitals reporting "inpatient_beds" in this state',
    'inpatient_beds_used': 'Reported total number of staffed inpatient beds that are occupied in this state',
    'inpatient_beds_used_coverage': 'Number of hospitals reporting "inpatient_beds_used" in this state',
    'inpatient_beds_used_covid': 'Reported patients currently hospitalized in an inpatient bed who have suspected or confirmed COVID-19 in this state',
    'inpatient_beds_used_covid_coverage': 'Number of hospitals reporting "inpatient_beds_used_covid" in this state',
    'previous_day_admission_adult_covid_confirmed': 'Number of patients who were admitted to an adult inpatient bed on the previous calendar day who had confirmed COVID-19 at the time of admission in this state',
    'previous_day_admission_adult_covid_confirmed_coverage': 'Number of hospitals reporting "previous_day_admission_adult_covid_suspected" in this state',
    'previous_day_admission_adult_covid_suspected': 'Number of patients who were admitted to an adult inpatient bed on the previous calendar day who had suspected COVID-19 at the time of admission in this state',
    'previous_day_admission_adult_covid_suspected_coverage': 'Number of hospitals reporting "previous_day_admission_adult_covid_suspected" in this state',
    'previous_day_admission_pediatric_covid_confirmed': 'Number of pediatric patients who were admitted to an inpatient bed, including NICU, PICU, newborn, and nursery, on the previous calendar day who had confirmed COVID-19 at the time of admission in this state',
    'previous_day_admission_pediatric_covid_confirmed_coverage': 'Number of hospitals reporting "previous_day_admission_pediatric_covid_confirmed" in this state',
    'previous_day_admission_pediatric_covid_suspected': 'Number of pediatric patients who were admitted to an inpatient bed, including NICU, PICU, newborn, and nursery, on the previous calendar day who had suspected COVID-19 at the time of admission in this state',
    'previous_day_admission_pediatric_covid_suspected_coverage': 'Number of hospitals reporting "previous_day_admission_pediatric_covid_suspected" in this state',
    'staffed_adult_icu_bed_occupancy': 'Reported total number of staffed inpatient adult ICU beds that are occupied in this state',
    'staffed_adult_icu_bed_occupancy_coverage': 'Number of hospitals reporting "staffed_adult_icu_bed_occupancy" in this state',
    'staffed_icu_adult_patients_confirmed_and_suspected_covid': 'Reported patients currently hospitalized in an adult ICU bed who have suspected or confirmed COVID-19 in this state',
    'staffed_icu_adult_patients_confirmed_and_suspected_covid_coverage': 'Number of hospitals reporting "staffed_icu_adult_patients_confirmed_and_suspected_covid" in this state',
    'staffed_icu_adult_patients_confirmed_covid': 'Reported patients currently hospitalized in an adult ICU bed who have confirmed COVID-19 in this state',
    'staffed_icu_adult_patients_confirmed_covid_coverage': 'Number of hospitals reporting "staffed_icu_adult_patients_confirmed_covid" in this state',
    'total_adult_patients_hospitalized_confirmed_and_suspected_covid': 'Reported patients currently hospitalized in an adult inpatient bed who have laboratory-confirmed or suspected COVID-19. This include those in observation beds.',
    'total_adult_patients_hospitalized_confirmed_and_suspected_covid_coverage': 'Number of hospitals reporting "total_adult_patients_hospitalized_confirmed_and_suspected_covid" in this state',
    'total_adult_patients_hospitalized_confirmed_covid': 'Reported patients currently hospitalized in an adult inpatient bed who have laboratory-confirmed COVID-19. This include those in observation beds.',
    'total_adult_patients_hospitalized_confirmed_covid_coverage': 'Number of hospitals reporting "total_adult_patients_hospitalized_confirmed_covid" in this state',
    'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid': 'Reported patients currently hospitalized in a pediatric inpatient bed, including NICU, newborn, and nursery, who are suspected or laboratory-confirmed-positive for COVID-19. This include those in observation beds',
    'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_coverage': 'Number of hospitals reporting "total_pediatric_patients_hospitalized_confirmed_and_suspected_covid" in this state',
    'total_pediatric_patients_hospitalized_confirmed_covid': 'Reported patients currently hospitalized in a pediatric inpatient bed, including NICU, newborn, and nursery, who are laboratory-confirmed-positive for COVID-19. This include those in observation beds.',
    'total_pediatric_patients_hospitalized_confirmed_covid_coverage': 'Number of hospitals reporting "total_pediatric_patients_hospitalized_confirmed_covid" in this state',
    'total_staffed_adult_icu_beds': 'Reported total number of staffed inpatient adult ICU beds in this state',
    'total_staffed_adult_icu_beds_coverage': 'Number of hospitals reporting "total_staffed_adult_icu_beds" in this state',
    'inpatient_beds_utilization': 'Percentage of inpatient beds that are being utilized in this state. This number only accounts for hospitals in the state that report both "inpatient_beds_used" and "inpatient_beds" fields.',
    'inpatient_beds_utilization_coverage': 'Number of hospitals reporting both "inpatient_beds_used" and "inpatient_beds"',
    'inpatient_beds_utilization_numerator': 'Sum of "inpatient_beds_used" for hospitals reporting both "inpatient_beds_used" and "inpatient_beds"',
    'inpatient_beds_utilization_denominator': 'Sum of "inpatient_beds" for hospitals reporting both "inpatient_beds_used" and "inpatient_beds"',
    'percent_of_inpatients_with_covid': 'Percentage of inpatient population who have suspected or confirmed COVID-19 in this state. This number only accounts for hospitals in the state that report both "inpatient_beds_used_covid" and "inpatient_beds_used" fields.',
    'percent_of_inpatients_with_covid_coverage': 'Number of hospitals reporting both "inpatient_beds_used_covid" and "inpatient_beds_used".',
    'percent_of_inpatients_with_covid_numerator': 'Sum of "inpatient_beds_used_covid" for hospitals reporting both "inpatient_beds_used_covid" and "inpatient_beds_used".',
    'percent_of_inpatients_with_covid_denominator': 'Sum of "inpatient_beds_used" for hospitals reporting both "inpatient_beds_used_covid" and "inpatient_beds_used".',
    'inpatient_bed_covid_utilization': 'Percentage of total (used/available) inpatient beds currently utilized by patients who have suspected or confirmed COVID-19 in this state. This number only accounts for hospitals in the state that report both "inpatient_beds_used_covid" and "inpatient_beds" fields.',
    'inpatient_bed_covid_utilization_coverage': 'Number of hospitals reporting both "inpatient_beds_used_covid" and "inpatient_beds".',
    'inpatient_bed_covid_utilization_numerator': 'Sum of "inpatient_beds_used_covid" for hospitals reporting both "inpatient_beds_used_covid" and "inpatient_beds".',
    'inpatient_bed_covid_utilization_denominator': 'Sum of "inpatient_beds" for hospitals reporting both "inpatient_beds_used_covid" and "inpatient_beds".',
    'adult_icu_bed_covid_utilization': 'Percentage of total staffed adult ICU beds currently utilized by patients who have suspected or confirmed COVID-19 in this state. This number only accounts for hospitals in the state that report both "staffed_icu_adult_patients_confirmed_and_suspected_covid" and "total_staffed_adult_icu_beds" fields.',
    'adult_icu_bed_covid_utilization_coverage': 'Number of hospitals reporting both both "staffed_icu_adult_patients_confirmed_and_suspected_covid" and "total_staffed_adult_icu_beds".',
    'adult_icu_bed_covid_utilization_numerator': 'Sum of "staffed_icu_adult_patients_confirmed_and_suspected_covid" for hospitals reporting both "staffed_icu_adult_patients_confirmed_and_suspected_covid" and "total_staffed_adult_icu_beds".',
    'adult_icu_bed_covid_utilization_denominator': 'Sum of "total_staffed_adult_icu_beds" for hospitals reporting both "staffed_icu_adult_patients_confirmed_and_suspected_covid" and "total_staffed_adult_icu_beds".',
    'adult_icu_bed_utilization': 'Percentage of staffed adult ICU beds that are being utilized in this state. This number only accounts for hospitals in the state that report both "staffed_adult_icu_bed_occupancy" and "total_staffed_adult_icu_beds" fields.',
    'adult_icu_bed_utilization_coverage': 'Number of hospitals reporting both both "staffed_adult_icu_bed_occupancy" and "total_staffed_adult_icu_beds".',
    'adult_icu_bed_utilization_numerator': 'Sum of "staffed_adult_icu_bed_occupancy" for hospitals reporting both "staffed_adult_icu_bed_occupancy" and "total_staffed_adult_icu_beds".',
    'adult_icu_bed_utilization_denominator': 'Sum of "total_staffed_adult_icu_beds" for hospitals reporting both "staffed_adult_icu_bed_occupancy" and "total_staffed_adult_icu_beds".',
    'geocoded_state': 'The geocoded centroid of the given state.',
    'previous_day_admission_adult_covid_confirmed_18-19': 'Number of patients admitted to adult inpatient bed on previous calendar day with confirmed COVID-19, age 18-19 years',
    'previous_day_admission_adult_covid_confirmed_18-19_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 18 to 19',
    'previous_day_admission_adult_covid_confirmed_20-29': 'Number of patients admitted to adult inpatient bed on previous calendar day with confirmed COVID-19, age 20-29 years',
    'previous_day_admission_adult_covid_confirmed_20-29_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 20 to 29',
    'previous_day_admission_adult_covid_confirmed_30-39': 'Number of patients admitted to adult inpatient bed on previous calendar day with confirmed COVID-19, age 30-39 years',
    'previous_day_admission_adult_covid_confirmed_30-39_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 30 to 39',
    'previous_day_admission_adult_covid_confirmed_40-49': 'Number of patients admittied to adult inpatient bed on previous calendar day with confirmed COVID-19, age 40-49 years',
    'previous_day_admission_adult_covid_confirmed_40-49_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 40 to 49',
    'previous_day_admission_adult_covid_confirmed_50-59': 'Number of patients admittied to adult inpatient bed on previous calendar day with confirmed COVID-19, age 50-59 years',
    'previous_day_admission_adult_covid_confirmed_50-59_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 50 to 59',
    'previous_day_admission_adult_covid_confirmed_60-69': 'Number of patients admittied to adult inpatient bed on previous calendar day with confirmed COVID-19, age 60-69 years',
    'previous_day_admission_adult_covid_confirmed_60-69_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 60 to 69',
    'previous_day_admission_adult_covid_confirmed_70-79': 'Number of patients admitted to adult inpatient bed on previous calendar day with confirmed COVID-19, age 70-79 years',
    'previous_day_admission_adult_covid_confirmed_70-79_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 70 to 79',
    'previous_day_admission_adult_covid_confirmed_80+': 'Number of patients admitted to adult inpatient bed on previous calendar day with confirmed COVID-19, age 80 years and older',
    'previous_day_admission_adult_covid_confirmed_80+_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages 80+',
    'previous_day_admission_adult_covid_confirmed_unknown': 'Number of patients admitted to adult inpatient bed on previous calendar day with confirmed COVID-19, age unknown',
    'previous_day_admission_adult_covid_confirmed_unknown_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 confirmed ages unknown',
    'previous_day_admission_adult_covid_suspected_18-19': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 18-19 years',
    'previous_day_admission_adult_covid_suspected_18-19_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 18 to 19',
    'previous_day_admission_adult_covid_suspected_20-29': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 20-29 years',
    'previous_day_admission_adult_covid_suspected_20-29_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 20 to 29',
    'previous_day_admission_adult_covid_suspected_30-39': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 30-39 years',
    'previous_day_admission_adult_covid_suspected_30-39_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 30 to 39',
    'previous_day_admission_adult_covid_suspected_40-49': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 40-49 years',
    'previous_day_admission_adult_covid_suspected_40-49_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 40 to 49',
    'previous_day_admission_adult_covid_suspected_50-59': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 50-59 years',
    'previous_day_admission_adult_covid_suspected_50-59_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 50 to 59',
    'previous_day_admission_adult_covid_suspected_60-69': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 60-69 years',
    'previous_day_admission_adult_covid_suspected_60-69_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 60 to 69',
    'previous_day_admission_adult_covid_suspected_70-79': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 70-79 years',
    'previous_day_admission_adult_covid_suspected_70-79_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 70 to 79',
    'previous_day_admission_adult_covid_suspected_80+': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age 80 years and older',
    'previous_day_admission_adult_covid_suspected_80+_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages 80+',
    'previous_day_admission_adult_covid_suspected_unknown': 'Number of patients admitted to adult inpatient bed on previous calendar day with suspected COVID-19, age unknown',
    'previous_day_admission_adult_covid_suspected_unknown_coverage': 'Number of hospitals reporting previous day admission adult COVID-19 suspected ages unknown',
    'deaths_covid': 'Number of patients with suspected or confirmed COVID-19 who died on the previous calendar day in the hospital, ED, or overflow location',
    'deaths_covid_coverage': 'The number of hospital facilities that reported deaths_covid for the given time period.',
    'on_hand_supply_therapeutic_a_casirivimab_imdevimab_courses': 'onhand supply therapeutic a',
    'on_hand_supply_therapeutic_b_bamlanivimab_courses': 'onhand supply therapeutic b',
    'on_hand_supply_therapeutic_c_bamlanivimab_etesevimab_courses': 'onhand supply therapeutic c',
    'previous_week_therapeutic_a_casirivimab_imdevimab_courses_used': 'previous week onhand supply therapeutic a',
    'previous_week_therapeutic_b_bamlanivimab_courses_used': 'previous week onhand supply therapeutic b',
    'previous_week_therapeutic_c_bamlanivimab_etesevimab_courses_used': 'previous week onhand supply therapeutic c',
    'icu_patients_confirmed_influenza': 'icu patients confirmed influenza',
    'icu_patients_confirmed_influenza_coverage': 'icu patients confirmed influenza Coverage',
    'previous_day_admission_influenza_confirmed': 'previous day admission influenza confirmed ',
    'previous_day_admission_influenza_confirmed_coverage': 'previous day admission influenza_confirmed coverage',
    'previous_day_deaths_covid_and_influenza': 'previous day deaths covid and influenza',
    'previous_day_deaths_covid_and_influenza_coverage': 'previous day deaths covid and influenza coverage',
    'previous_day_deaths_influenza': 'previous day deaths influenza',
    'previous_day_deaths_influenza_coverage': 'previous day deaths influenza coverage',
    'total_patients_hospitalized_confirmed_influenza': 'total patients hospitalized confirmed influenza',
    'total_patients_hospitalized_confirmed_influenza_and_covid': 'total patients hospitalized confirmed influenza and covid',
    'total_patients_hospitalized_confirmed_influenza_and_covid_coverage': 'total patients hospitalized confirmed influenza and covid coverage',
    'total_patients_hospitalized_confirmed_influenza_coverage': 'total patients hospitalized confirmed influenza coverage',
    'all_pediatric_inpatient_bed_occupied': 'Total number of set-up and staffed inpatient pediatric beds that are occupied by a patient. Includes both PICU and med-surge beds (beds in which medical or surgical pediatric patients may be routinely placed). Include any occupied surge/hallway/overflow beds that are open for use. This count excludes NICU, newborn nursery, and outpatient surgery beds. This is a subset of #4a, and reflects occupancy levels for beds reported in #3c. This field is required as of 2/2/2022.',
    'all_pediatric_inpatient_bed_occupied_coverage': 'Total number of set-up and staffed inpatient pediatric beds that are occupied by a patient (coverage). Includes both PICU and med-surge beds (beds in which medical or surgical pediatric patients may be routinely placed). Include any occupied surge/hallway/overflow beds that are open for use. This count excludes NICU, newborn nursery, and outpatient surgery beds. This is a subset of #4a, and reflects occupancy levels for beds reported in #3c. This field is required as of 2/2/2022.',
    'all_pediatric_inpatient_beds': 'Total number of pediatric beds in the facility that are currently set-up, staffed and able to be used for a patient within the reporting period. This count includes occupied and unoccupied inpatient pediatric beds including both PICU and med-surge beds (beds in which medical or surgical pediatric patients may be routinely placed). Include any surge/hallway/overflow beds that are open for use for a patient, regardless of whether they are occupied or available. This count excludes NICU, newborn nursery beds, and outpatient surgery beds. This is a subset of #3a. This field is required as of 2/2/2022.',
    'all_pediatric_inpatient_beds_coverage': 'Total number of pediatric beds in the facility that are currently set-up, staffed and able to be used for a patient within the reporting period (coverage). This count includes occupied and unoccupied inpatient pediatric beds including both PICU and med-surge beds (beds in which medical or surgical pediatric patients may be routinely placed). Include any surge/hallway/overflow beds that are open for use for a patient, regardless of whether they are occupied or available. This count excludes NICU, newborn nursery beds, and outpatient surgery beds. This is a subset of #3a. This field is required as of 2/2/2022.',
    'previous_day_admission_pediatric_covid_confirmed_0_4': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission. The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_0_4_coverage': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission (coverage). The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_12_17': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission. The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_12_17_coverage': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission (coverage). The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_5_11': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission. The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_5_11_coverage': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission (coverage). The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_unknown': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission. The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'previous_day_admission_pediatric_covid_confirmed_unknown_coverage': 'Enter the number of patients, by age group, who were admitted to an inpatient or ICU bed on the previous calendar day who had laboratory-confirmed COVID19 at the time of admission (coverage). The summary of age breakdowns should be identical to #18a. This includes patients ages 0-4, 5-11, and 12-17 years old admitted to any inpatient bed, regardless of whether the bed is designated as pediatric vs. adult. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'staffed_icu_pediatric_patients_confirmed_covid': 'Total number of pediatric ICU beds occupied by laboratory confirmed positive COVID-19 patients. This is a subset of #6c, occupied pediatric ICU beds. This count excludes NICU, newborn nursery, and outpatient surgery beds. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'staffed_icu_pediatric_patients_confirmed_covid_coverage': 'Total number of pediatric ICU beds occupied by laboratory confirmed positive COVID-19 patients (coverage). This is a subset of #6c, occupied pediatric ICU beds. This count excludes NICU, newborn nursery, and outpatient surgery beds. This field is required as of 2/2/2022. See Appendix D for the definition of laboratory-confirmed COVID-19.',
    'staffed_pediatric_icu_bed_occupancy': 'Total number of set-up and staffed pediatric ICU beds occupied by a patient. This count excludes NICU, newborn nursery, and outpatient surgery beds. This is subset of #4c and #6a. This field is required as of 2/2/2022. Note: All occupied pediatric ICU beds should be considered, regardless of the unit on which the bed is housed. This includes ICU beds located in non-ICU locations, such as mixed acuity units.',
    'staffed_pediatric_icu_bed_occupancy_coverage': 'Total number of set-up and staffed pediatric ICU beds occupied by a patient (coverage). This count excludes NICU, newborn nursery, and outpatient surgery beds. This is subset of #4c and #6a. This field is required as of 2/2/2022. Note: All occupied pediatric ICU beds should be considered, regardless of the unit on which the bed is housed. This includes ICU beds located in non-ICU locations, such as mixed acuity units.',
    'total_staffed_pediatric_icu_beds': 'Total number of pediatric ICU beds in the facility that are currently set-up, staffed and are or could be used for a patient within the reporting period. This count includes occupied and unoccupied ICU beds, including any ICU beds that are, or could be, staffed and used for a pediatric patient. This count excludes NICU, newborn nursery, and outpatient surgery beds. This is a subset of #3c and #5a. Any beds counted in #5c should NOT be counted in #5b. This field is required as of 2/2/2022. Note: All pediatric ICU beds should be considered, regardless of the unit on which the bed is housed. This includes ICU beds located in non-ICU locations, such as mixed acuity units.',
    'total_staffed_pediatric_icu_beds_coverage': 'Total number of pediatric ICU beds in the facility that are currently set-up, staffed and are or could be used for a patient within the reporting period (coverage). This count includes occupied and unoccupied ICU beds, including any ICU beds that are, or could be, staffed and used for a pediatric patient. This count excludes NICU, newborn nursery, and outpatient surgery beds. This is a subset of #3c and #5a. Any beds counted in #5c should NOT be counted in #5b. This field is required as of 2/2/2022. Note: All pediatric ICU beds should be considered, regardless of the unit on which the bed is housed. This includes ICU beds located in non-ICU locations, such as mixed acuity units.'
}
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




