import streamlit as st

tab_css = """
            <style>
                .stTabs [data-baseweb="tab-list"] {gap: 20px;}

                .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {font-size:2rem;}
            </style>"""


def display_header(logo, page_title):
    col0, col1 = st.columns([0.8, 0.2])
    with col0:
        # set up the burnt orange font
        st.markdown(
            """<style> .font {font-size:90px ; font-family: 'Cooper Black'; color: #f8971f;} </style>""",
            unsafe_allow_html=True,
        )
        # display page title
        st.markdown(f'<p class="font">{page_title}</p>', unsafe_allow_html=True)
    with col1:
        st.image(logo, use_column_width="always")

    # st.markdown(f"> {descriptions['header']} ")


def display_data_description(long_description):
    # st.markdown(
    #    """<style> .data_title {font-size:60px} </style>""",
    #    unsafe_allow_html=True,
    # )
    # st.markdown(
    #    """<style> .data_short_description {font-size:40px ;} </style>""",
    #    unsafe_allow_html=True,
    # )
    st.markdown(
        """<style> .data_long_description {font-size:25px ;} </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(f'<p class="data_long_description">{long_description}</p>', unsafe_allow_html=True)


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

    with open(f"data/{file_name}") as f:
        st.download_button(
            label="Download Full Data",
            data=f,
            file_name=file_name,
            mime="text/csv",
        )
    if date:
        st.markdown("Last Update: %s" % date)


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
