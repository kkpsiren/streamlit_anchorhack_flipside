import streamlit as st
#from scripts.utils import read_flipside
from plots import plot_scatter

def address_page(df,df_minted,df_images):
    
    addresses = st.selectbox('Select Address', df_images.sort_values('TOKEN_METADATA_URI')['BUYER_ADDRESS'].unique())

    selected_df = df.query('USER_ADDRESS in @addresses')

    selected_minted = df_minted.query('USER_ADDRESS in @addresses')
    selected_previous_nfts =  df_images.query('BUYER_ADDRESS in @addresses')
    images = [i for _,i in selected_previous_nfts['IMAGE_URL'].iteritems() if i is not None]
    names = [i for _,i in selected_previous_nfts['PROJECT_NAME'].iteritems() if i is not None]
        
    # st.write(selected_df)
    # st.write(selected_previous_nfts)
    # st.write(selected_minted)

    st.write(f'Address {addresses} minted {selected_minted.shape[0]} GodMode NFTs') 
    st.write(f'This address has in the past 6 months purchased {selected_previous_nfts.shape[0]} NFTs')
    i = df['USER_ADDRESS'].unique()[0]
    address = f'https://etherscan.io/address/{addresses}'
    st.markdown(f'link to [EtherScan]({address})')
    l,r = st.columns(2)
    with l:
        st.plotly_chart(plot_scatter(selected_df),use_container_width=True)
    with r:
        if len(images)>0:
            for name,image_url in zip(names,images):
                st.image(image_url,use_column_width=True)
                st.write(name)
        else:
            st.write('no images')
    # st.dataframe(df)

    # st.dataframe(df_images)
    