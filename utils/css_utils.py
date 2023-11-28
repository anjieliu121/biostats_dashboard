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
    #st.markdown(
    #    """<style> .data_short_description {font-size:40px ;} </style>""",
    #    unsafe_allow_html=True,
    #)
    st.markdown(
        """<style> .data_long_description {font-size:25px ;} </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(f'<p class="data_long_description">{long_description}</p>', unsafe_allow_html=True)


def display_download_button(file_name):
    st.markdown(
        """ 
        <style>
        div.stDownloadButton > button:first-child {
            background-color: #bf5700;
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