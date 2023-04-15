import streamlit as st
import numpy as np
import pandas as pd

def app(car_df):
	st.header("View Data")
	with st.expander("View Dataset: "):
		st.table(car_df)
	st.subheader("Columns Description")
	if st.checkbox("Show Summary"):
		st.table(car_df.describe())

