# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:34:31 2024

@author: Emil Jakobsen
"""

## Data handling
import pandas as pd
import numpy as np
import statistics
import sqlite3

## SQL
from sqlalchemy import create_engine

## Data
import yfinance as yf

## UI
import streamlit as st

def update_sql(df, ticker):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    
    c.execute(f'CREATE TABLE IF NOT EXISTS "{ticker}" (Date INTEGER, Open INTEGER, High INTEGER, Low INTEGER, Close INTEGER, Volume INTEGER, Dividends INTEGER, "Stock Splits" INTEGER);')
    
    for index, row in df.iterrows():
        c.execute(f'INSERT INTO "{ticker}" (Date, Open, High, Low, Close, Volume, Dividends, "Stock Splits") VALUES (:date, :open, :high, :low, :close, :volume, :dividends, :splits);', 
                  {'date': str(row['Date']), 'open': row['Open'], 'high': row['High'], 'low': row['Low'], 'close': row['Close'], 'volume': row['Volume'], 'dividends': row['Dividends'], 'splits': row['Stock Splits']})

    conn.commit()
    conn.close()
    

def retrieve_df(ticker):
    conn = sqlite3.connect('test.db')
    
    df = pd.read(f'SELECT * FROM "{ticker}"', conn)
    
    conn.close()
    
    return df

stock = yf.Ticker('JNJ')
df = stock.history('JNJ', start = '2020-01-01')
df.reset_index(inplace=True)

update_sql(df, 'JNJ')

df2 = retrieve_df('JNJ')

df2.index = pd.to_datetime(df2.index)

print(df2.head())

st.dataframe(df2.head())
