import io
import streamlit as st


def download_fig(fig, title):
    st.warning('Save your work!', icon="⭐")
    buffer = io.StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    html_bytes = buffer.getvalue().encode()

    st.download_button(
        label='Download HTML',
        data=html_bytes,
        file_name=f'{title}.html',
        mime='text/html'
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        plt_width = st.text_input(
            "Enter Desired Plot Width in Pixels",
            value="900",
            placeholder="900",
            # label_visibility='collapsed'
        )
    with col2:
        plt_height = st.text_input(
            "Enter Desired Plot Height in Pixels",
            value="500",
            placeholder="500",
            # label_visibility='collapsed'
        )
    # update fig height
    width = int(plt_width)
    height = int(plt_height)
    fig.update_layout(height=height, width=width)

    # buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        # PDF
        buffer = io.BytesIO()
        fig.write_image(file=buffer, format="pdf")
        st.download_button(
            label="Download PDF",
            data=buffer,
            file_name=f"{title}.pdf",
            mime="application/pdf",
        )
    with col2:
        # PNG
        buffer = io.BytesIO()
        fig.write_image(file=buffer, format="png")
        st.download_button(
            label="Download PNG",
            data=buffer,
            file_name=f"{title}.png",
            mime="application/png",
        )