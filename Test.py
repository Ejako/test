# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:34:31 2024

@author: Emil Jakobsen
"""

## Data handling
import pandas as pd
import numpy as np
import statistics

## SQL
from sqlalchemy import create_engine

## Data
import yfinance as yf

## UI
import streamlit as st

engine = create_engine('sqlite:///test.db')

df = yf.download('MMM', start = '2020-01-01')

df.to_sql(df, engine)

df2 = pd.read_sql('MMM', engine, if_exists = 'replace')

st.dataframe(df2.head())
