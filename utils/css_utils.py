import streamlit as st

download_button_css = """ <style> 
                            div.stDownloadButton > button:first-child {
                                background-color: #005f86;
                                color:#FFFFFF;
                            }
                          </style>"""

select_box_css = """ <style>
                            .stSelectbox:first-of-type > div[data-baseweb=\"select\"] > div {
                                background-color: #bf5700;
                                color:#FFFFFF;
                                padding: 10px;
                            }
                        </style>"""

multiselection_box_css = """ <style>
                                span[data-baseweb="tag"] {
                                    background-color: #bf5700 !important;
                                    color:#FFFFFF; padding: 10px;
                                }
                             </style> """
def display_download_button(file_name, date=None):
    st.markdown(download_button_css, unsafe_allow_html=True)

    columns = st.columns([1,1,1,1,1])
    with columns[0]:
        with open(f"data/{file_name}") as f:
            st.download_button(
                label="Download Full Data",
                data=f,
                file_name=file_name,
                mime="text/csv",
            )
    with columns[1]:
        if date:
            st.caption(f"Last Update:  \n %s" % date)



def selection_box(txt, lst, index):  # bf5700
    st.markdown(select_box_css, unsafe_allow_html=True)
    box = st.selectbox(txt, lst, index=index)
    return box


def multiselection_box(txt, lst, *default):
    st.markdown(multiselection_box_css, unsafe_allow_html=True)
    if len(default) > 0:
        box = st.multiselect(txt, lst, default=list(default))
    else:
        box = st.multiselect(txt, lst, default=None)
    return box


def markdown_background(txt):
    # font-size:24px;border-radius:5%;
    st.markdown(f'<p style="background-color:#d6d2c4;color:#333f48;padding: 18px;border-radius: 8px;">{txt}</p>',
                unsafe_allow_html=True)


