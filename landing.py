import streamlit as st
from plots import number_plot, eth_plot, nft_plot

def landing_page(df,df_minted,df_images):
    st.image('https://openseauserdata.com/files/e22c98856cf40d4efb9d2dcb69d25c9b.png')
    st.write("GodMode by FlipsideCrypto")
    st.markdown(
        """
        ### Analyze the Ethereum profile of those who minted during the first hour after launch. 
        146 addresses minted 264 NFTs during the first hour
        """ 
    )
    ser = df_minted.groupby('USER_ADDRESS')['TOKENID'].count().sort_values(ascending=False)
    l,r = st.columns(2)
    with r:
        st.pyplot(number_plot(ser),use_container_width=True)
    with l:
        for i,val in ser.iloc[:7].iteritems():
            address = f'https://etherscan.io/address/{i}'
            st.markdown(f'[{i[:7]}...{i[-5:]}]({address})  Minted {val} GodMode NFTs')
        st.write(f'rest of the {264-7} remaining also minted 1 GodMode NFT. See the individual address page for the full list')


    eth_df = df.query('SYMBOL=="ETH"')
    ser = eth_df.query("BALANCE_DATE=='2022-06-07'").sort_values('BALANCE',ascending=False)
    st.markdown(f"""
                
                        
### How many of them moved the minimum .1 ETH into their minting wallet vs. already had at least .1 ETH in that wallet? 
{(ser['BALANCE']>1).sum()} addresses had more than 1 ETH  
{(ser['BALANCE']>0.1).sum()} addresses had more than 0.1 ETH  
{(ser['BALANCE']>0.01).sum()} addresses had more than 0.01 ETH  
""")
    

    l,r = st.columns(2)
    with r:
        st.pyplot(eth_plot(ser),use_container_width=True)
    with l:
        #st.dataframe(ser)
        for i, val in ser.iloc[:7,:].iterrows():
            address = f'https://etherscan.io/address/{val["USER_ADDRESS"]}'
            # st.write(val)
            st.markdown(f'[{val["USER_ADDRESS"][:7]}...{val["USER_ADDRESS"][-5:]}]({address}) Had {val["BALANCE"]:.5f} ETH on 2022-06-07 ')
        #st.write(f'rest of the {df.shape[0]-7} also minted 1. See the individual address page for the full list')


    st.markdown(f"""             
             ### How many of them have been active in NFT purchases over the past six months? 
             
             """)

    ser = df_images.groupby('BUYER_ADDRESS')['NFT_ADDRESS'].count().sort_values(ascending=False)
    l,r = st.columns(2)
    with r:
        st.pyplot(nft_plot(ser),use_container_width=True)
    with l:
        for i,val in ser.iloc[:7].iteritems():
            address = f'https://etherscan.io/address/{i}'
            st.markdown(f'[{i[:7]}...{i[-5:]}]({address})  Minted {val} GodMode NFTs')
        st.write(f'In total 48 addresses have minted an NFT that cost more than 0 ETH or WETH.')
        with st.expander("show addresses"):
            for i in ser.index.tolist():
                st.markdown(f'[{i}](https://etherscan.io/address/{i})')

