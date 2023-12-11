import pandas as pd
import plotly.graph_objs as go


def clean_data(df):
    df['Date'] = pd.to_datetime(df['Unix'] // 1000, unit='s')
    df.set_index('Date', inplace=True)
    return df

df_btc = pd.read_csv('../historical_yahoo/BTC-USD.csv')

def exploratory_check(df):
    # print(df.isnull().sum())
    print(df.head())
    print(df.tail())
    print(df.dtypes)
    print(df.describe)
    
exploratory_check(df_btc)
