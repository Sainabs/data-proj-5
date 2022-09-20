
from re import X
from this import s
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


title = st.title("Sainab's Admin Dashboard")

df = pd.read_csv("supermarket.csv")
# st.dataframe(df)
# st.table(df)


st.subheader('Stores with the highest number of customers')
df.sort_values(["daily_customer_count"],
axis=0,
ascending=[False],
inplace=True)
st.dataframe(df[['store_id','daily_customer_count']].head(n=10)) #makes it interactive
# st.table(df[['store_id','daily_customer_count']].head(n=10)) #makes table



st.subheader('Stores with the lowest number of customers')
df.sort_values(["daily_customer_count"],
axis=0,
ascending=[True],
inplace=True)
st.dataframe(df[['store_id','daily_customer_count']].head(n=10))
# ##st.table(df[['store_id','daily_customer_count']].head(n=10))



st.subheader('Stores with the highest sales')
df.sort_values(["store_sales"],
axis=0,
ascending=[False],
inplace=True)
st.dataframe(df[['store_id','store_sales']].head(n=10))
# st.table(df[['store_id','store_sales']].head(n=10))


st.subheader('Stores with the lowest sales')
df.sort_values(["store_sales"],
axis=0,
ascending=[True],
inplace=True)
st.dataframe(df[['store_id','store_sales']].head(n=10))
st.table(df[['store_id','store_sales']].head(n=10))


st.subheader("Available Items in Store")
# st.bar_chart(df['items_available'].head(n=10))

# st.bar_chart(df[['items_available','store_area']].head(n=10))
df.sort_values(["items_available"],
axis=0,
ascending=[False],
inplace=True)
st.dataframe(df[['store_id','items_available']].head(n=10))
st.bar_chart(data=df.head(n=10), x='store_id' , y='items_available')



ch = st.checkbox('I understand this data')
if ch:
    st.write("Thanks for visiting Sainab's Admin Dashboard")