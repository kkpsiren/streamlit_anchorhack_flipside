import streamlit as st
#from scripts.utils import read_flipside
from landing import landing_page
from address import address_page

from beautify import flipside_logo, discord_logo
import os
from scripts import load_queries
from plots import plot_scatter
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Flipside", layout="wide")

# df = read_flipside(url)



df, df_images, df_minted = load_queries()

radio_choice = st.sidebar.radio("Choose", ("Main", "Individual Addresses"), index=0)
if radio_choice == "Main":
    landing_page(df,df_minted,df_images)
elif radio_choice == "Individual Addresses":
    address_page(df,df_minted,df_images)
    
    
    st.sidebar.markdown(
        """ # Header
    ## Subheader
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris iaculis, magna a lacinia molestie, tortor diam malesuada tortor, ut eleifend est neque vel dui."""
    )

    with st.expander("Show Summary"):
            st.markdown(
                """## Subheader
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris iaculis, magna a lacinia molestie, tortor diam malesuada tortor, ut eleifend est neque vel dui. Cras eu turpis sodales, fringilla leo sed, porttitor erat. Nullam ut sodales nunc. Praesent maximus at eros sed interdum. Donec urna leo, ornare quis ligula in, vestibulum maximus tortor. Morbi auctor lobortis posuere. Phasellus et vehicula enim. Phasellus laoreet lacus cursus enim egestas, sed pulvinar mi porta. Cras posuere consectetur ex, eu bibendum nunc hendrerit quis. Sed gravida mi et sodales porttitor. Duis id lobortis massa. Donec nisi magna, finibus at tellus sed, consequat convallis sapien. Phasellus placerat porttitor vehicula. In rhoncus commodo libero, a mollis risus ultricies et. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean nec congue nunc, quis mattis magna.

    Curabitur condimentum est lectus, eu sodales mauris facilisis vel. Proin nec dapibus urna, vel imperdiet dui. Pellentesque porttitor urna justo, ac tincidunt nisl tincidunt et. Integer ipsum orci, gravida sed tristique vel, posuere elementum nisi. Aenean efficitur magna augue, sit amet condimentum nisi sodales pharetra. Sed id arcu quis nibh vehicula scelerisque et nec turpis. Donec id augue eget arcu dapibus finibus. Aenean volutpat cursus libero, a iaculis elit condimentum dignissim. Aenean id accumsan velit, at euismod purus. Pellentesque blandit ultrices diam sit amet consectetur. Ut efficitur nisi ac felis gravida, at sodales nisl finibus. Nulla tincidunt blandit tincidunt. Aliquam vehicula venenatis turpis sed accumsan. Curabitur at elit sollicitudin, pellentesque enim in, blandit dolor.

    Proin quis lectus aliquet, varius nibh vel, egestas nisi. Cras viverra convallis risus, ut euismod tortor vestibulum eu. Nunc aliquam ultricies risus vitae tincidunt. Sed suscipit mollis nunc at scelerisque. In sodales efficitur maximus. Vestibulum faucibus ante metus. Etiam blandit lacus id consectetur suscipit.

    Cras dapibus sapien eget turpis tristique faucibus. Phasellus vehicula lectus et turpis porttitor, rhoncus ultricies lectus luctus. Pellentesque vestibulum risus a nibh pellentesque placerat eget a nunc. Quisque blandit ac nibh at porta. Nullam neque enim, iaculis et elit ut, auctor pretium ipsum. Integer accumsan, nulla ut semper pharetra, nisl nibh condimentum ex, id hendrerit nunc nunc eu libero. Integer eget ante eu mauris finibus consequat. Donec efficitur efficitur suscipit. Suspendisse vitae dolor et purus tincidunt auctor id id tellus. Vivamus vitae suscipit tortor. Sed eget mollis ipsum. Aliquam erat volutpat. Donec in gravida sapien. Aliquam cursus, lorem nec hendrerit convallis, ipsum odio faucibus lacus, at luctus risus eros at justo. Aenean sit amet enim convallis diam venenatis imperdiet sed sed nulla.

    Etiam at erat quis ante venenatis sagittis interdum non lorem. Phasellus vel nibh dolor. Donec tortor turpis, porttitor non sodales vel, semper a lectus. Donec sit amet tellus nec mi dignissim blandit id a mauris. In sit amet porttitor est. Praesent eu quam euismod, facilisis augue in, eleifend nibh. Phasellus venenatis porta risus, id ornare felis ultrices sagittis. Curabitur a felis nulla. Etiam bibendum massa ac libero euismod, id bibendum velit rutrum. Aenean porta mi magna, in condimentum neque tristique sed. Fusce ultricies lectus eros, ut dictum risus volutpat nec. Ut dictum nulla dolor, at finibus mauris aliquam sit amet.    """
            )
        
else:
    st.write("shouldn't be here")


st.sidebar.markdown("#### Connect")
discord_logo(os.getenv('DISCORD_USERNAME'))
flipside_logo()