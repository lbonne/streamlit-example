from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import datetime
import yfinance as yf

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to change this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.write("Yowkes!!!")
mylist = st.secrets.YF.ThickerList
--st.write(mylist[0])
--symbol1 = yf.Ticker(mylist[0])
--st.write(symbol1.info)

option = st.selectbox(
    'Select your thicker: ',
    (mylist))
myticker = yf.Ticker(option)
st.write("Info :")
st.write(myticker.info)    


with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")       
    )
    
