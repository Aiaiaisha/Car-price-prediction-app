import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(cars_df):
	st.set_option("deprecation.showPyplotGlobalUse",False)
	st.header("Visualise Data")

	st.subheader("Scatter Plot")
	feat_x = st.multiselect("Select X-axis values ",("carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick","price"))
	for i in feat_x:
		plt.scatter(x=cars_df[i],y=cars_df["price"])
		st.pyplot()

	st.subheader("Visualisation Selector")
	plot_types = st.multiselect("Select charts or plots",("Histogram","Boxplot","Correlation Heatmap",))
	if "Histogram" in plot_types:
		st.subheader("Histograms")
		columns = st.selectbox("Select the column to create the Histogram",("carwidth","enginesize","horsepower"))
		plt.figure(figsize = (8,16))
		plt.title("Histogram for selected columns")
		plt.hist(cars_df[columns],bins = "sturges",edgecolor = "black")
		st.pyplot()
	if "Boxplot" in plot_types:
		st.subheader("Boxplot")
		columns = st.selectbox("Select the column to create the Boxplot",("carwidth","enginesize","horsepower"))
		plt.title("Boxplot for selected columns")
		plt.figure(figsize = (8,16))
		sns.boxplot(cars_df[columns])
		st.pyplot()	
	if "Correlation Heatmap" in plot_types:
		st.subheader("Correlation Heatmap")
		plt.title("Boxplot for selected columns")
		plt.figure(figsize = (8,16))
		sns.heatmap(cars_df.corr(),annot = True,fmt="g")
		st.pyplot()			