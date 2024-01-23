import streamlit as st

def display_data_description(long_description):
    st.markdown(f">{long_description}")
    # st.markdown(
    #    """<style> .data_long_description {font-size:25px ;} </style>""",
    #    unsafe_allow_html=True,
    # )
    # st.markdown(f'<p class="data_long_description">{long_description}</p>', unsafe_allow_html=True)

def display_source(url):
    # components.iframe(link)
    st.markdown("Source: [link](%s)" % url)