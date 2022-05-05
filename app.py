import streamlit as st
from scripts.utils import read_flipside
from pages.landing import landing_page
from config import url

st.set_page_config(page_title="Flipside <3 Anchor", layout="wide")

df = read_flipside(url)

st.sidebar.markdown(
    """ # Header
## Subheader
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris iaculis, magna a lacinia molestie, tortor diam malesuada tortor, ut eleifend est neque vel dui. Cras eu turpis sodales, fringilla leo sed, porttitor erat. Nullam ut sodales nunc. Praesent maximus at eros sed interdum. Donec urna leo, ornare quis ligula in, vestibulum maximus tortor. Morbi auctor lobortis posuere. Phasellus et vehicula enim. Phasellus laoreet lacus cursus enim egestas, sed pulvinar mi porta. Cras posuere consectetur ex, eu bibendum nunc hendrerit quis. Sed gravida mi et sodales porttitor. Duis id lobortis massa. Donec nisi magna, finibus at tellus sed, consequat convallis sapien. Phasellus placerat porttitor vehicula. In rhoncus commodo libero, a mollis risus ultricies et. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean nec congue nunc, quis mattis magna.
"""
)

radio_choice = st.sidebar.radio("Choose", ("Main", "Selection"), index=0)
if radio_choice == "Main":
    landing_page()
elif radio_choice == "Selection":
    with st.expander("Show Summary"):
        st.markdown(
            """## Subheader
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris iaculis, magna a lacinia molestie, tortor diam malesuada tortor, ut eleifend est neque vel dui. Cras eu turpis sodales, fringilla leo sed, porttitor erat. Nullam ut sodales nunc. Praesent maximus at eros sed interdum. Donec urna leo, ornare quis ligula in, vestibulum maximus tortor. Morbi auctor lobortis posuere. Phasellus et vehicula enim. Phasellus laoreet lacus cursus enim egestas, sed pulvinar mi porta. Cras posuere consectetur ex, eu bibendum nunc hendrerit quis. Sed gravida mi et sodales porttitor. Duis id lobortis massa. Donec nisi magna, finibus at tellus sed, consequat convallis sapien. Phasellus placerat porttitor vehicula. In rhoncus commodo libero, a mollis risus ultricies et. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean nec congue nunc, quis mattis magna.
    """
        )
else:
    st.write("shouldn't be here")
