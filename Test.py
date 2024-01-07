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


df = yf.download('MMM', start = '2020-01-01')

conn = sqlite3.connect('test.db')
df.to_sql(df, conn, if_exists = 'replace')

df2 = pd.read_sql('MMM', conn)

st.dataframe(df2.head())
