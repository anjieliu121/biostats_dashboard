import streamlit as st


def display_download_button(file_name, date=None):
    st.markdown(
        """ 
        <style>
        div.stDownloadButton > button:first-child {
            background-color: #bf5700;
            color:#FFFFFF;
        }
        </style>
        """, unsafe_allow_html=True)

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
    css = "<style>.stSelectbox:first-of-type > div[data-baseweb=\"select\"] > div {" + \
          "background-color: #bf5700;" + \
          "color:#FFFFFF; padding: 10px;}</style>"
    st.markdown(css, unsafe_allow_html=True)
    box = st.selectbox(txt, lst, index=index)
    return box


def markdown_background(txt):
    # font-size:24px;border-radius:5%;
    st.markdown(f'<p style="background-color:#d6d2c4;color:#333f48;padding: 18px;border-radius: 8px;">{txt}</p>',
                unsafe_allow_html=True)


def multiselect_css(txt, lst):
    st.markdown(
        """
    <style>
    span[data-baseweb="tag"] {
      background-color: #bf5700 !important;
      color:#FFFFFF; padding: 10px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    box = st.multiselect(txt, lst)
    return box
