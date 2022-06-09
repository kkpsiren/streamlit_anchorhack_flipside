import plotly.express as px
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def cluster_plot(data):
    return sns.clustermap(data.T.corr())

def number_plot(df):
    fig,ax = plt.subplots()
    df.reset_index()['TOKENID'].plot(ax=ax)
    #plt.xticks([])
    plt.xlabel('Addresses')
    plt.ylabel('Number of NFTs Minted')
    sns.despine(fig=fig)
    return fig


def nft_plot(df):
    fig,ax = plt.subplots()
    df.reset_index()['NFT_ADDRESS'].plot(ax=ax)
    #plt.xticks([])
    plt.xlabel('Addresses')
    plt.ylabel('Number of NFTs Bought')
    sns.despine(fig=fig)
    return fig

def plot_scatter(df):
    i = df['USER_ADDRESS'].unique()[0]
    df['BALANCE_DATE'] = pd.to_datetime(df['BALANCE_DATE'])
    df['SYMBOL'] = df['SYMBOL'].fillna(df['CONTRACT_ADDRESS'])
    fig = px.scatter(df, x="BALANCE_DATE", y="BALANCE", color="SYMBOL",
                     color_discrete_sequence=px.colors.qualitative.G10,
                     template='simple_white',title=i,
                hover_data=['SYMBOL'])
    fig.update_layout(legend=dict(
    yanchor="top",
    y=-0.5,
    xanchor="left",
    x=0.01
))
    return fig

def eth_plot(df):
    fig,ax = plt.subplots()
    df.plot(x='USER_ADDRESS',y='BALANCE',ax=ax)
    plt.xticks([])
    plt.xlabel('Addresses')
    plt.ylabel('ETH balance')
    sns.despine()
    return fig