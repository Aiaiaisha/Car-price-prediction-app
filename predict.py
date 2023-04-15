import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error

@st.cache()
def prediction(cars_df,car_width,engine_size,horse_power,drive_wheel_fwd,car_comp_buick):
	X = cars_df.iloc[:,:-1]
	y = cars_df["price"]
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size =0.3,random_state =42)

	lr=LinearRegression()
	lr.fit(X_train,y_train)
	lr_score = lr.score(X_train,y_train)
	lr_price = lr.predict([[car_width,engine_size,horse_power,drive_wheel_fwd,car_comp_buick]])
	price = lr_price[0]
	y_test_pred = lr.predict(X_test)
	test_r2 = r2_score(y_test,y_test_pred)
	test_mae = mean_absolute_error(y_test,y_test_pred)
	test_msle = mean_squared_log_error(y_test,y_test_pred)
	test_rmse = np.sqrt(mean_squared_error(y_test,y_test_pred))

	return price,lr_score,test_r2,test_mae,test_msle,test_rmse


def app(cars_df):
	st.markdown("<p style='font-family:calibri;font-size:30;color:blue'>this app uses <b>Linear Regression</b> to predict car price based on your input",unsafe_allow_html = True)
	st.subheader("select values")
	car_width = st.slider("Car width",float(cars_df["carwidth"].min()),float(cars_df["carwidth"].max()))
	engine_size = st.slider("Engine size",float(cars_df["enginesize"].min()),float(cars_df["enginesize"].max()))
	horse_power = st.slider("Horse Power",float(cars_df["horsepower"].min()),float(cars_df["horsepower"].max()))
	drive_wheel_fwd = st.radio("is it a Forward drive wheel car?",("Yes","No"))
	car_comp_buick = st.radio("is the car manufactured by Buick?",("Yes","No"))

	if drive_wheel_fwd == "No":
		drive_wheel_fwd = 0
	else:
		drive_wheel_fwd = 1

	if car_comp_buick == "No":
		car_comp_buick = 0
	else:
		car_comp_buick = 1

	if st.button("predict"):
		st.subheader("prediction results: ")
		price,score,test_r2,test_mae,test_msle,test_rmse = prediction(cars_df,car_width,engine_size,horse_power,drive_wheel_fwd,car_comp_buick)
		st.success(f" the predicted pric of the car is: {price}")
		st.info(f"""model score: {score}
			r2 score: {test_r2}
			Mean absolute Error: {test_mae}
			Mean Squared log error: {test_msle}
			root mean squared error {test_rmse}""")