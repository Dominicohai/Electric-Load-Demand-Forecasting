# Electric-Load-Demand-Forecasting
This code uses Neural Networks to forecast an hour ahead the electric load demand of a typical site

The Multi-Layer Perceptron (MLP) has an input layer with a total of seven input nodes, two hidden layers with each layer consisting of four perceptrons, and an output layer. The optimizer used is the Adam Optimizer and Stochastic Gradient Descent is the Loss Function employed.
The seven input nodes are classified into: temperature, previous load data, business day, day and hour pointers. They are broken down into:
	•	Temperature forecast data 
	•	Load demand for previous hour of same day and week
	•	Load demand for same hour of previous day
	•	Load demand for same hour of same day of previous week
	•	Business Day or Non-Business Day
	•	Day of the Week (1 for Mondays, 7 for Sundays)
	•	Hour of the Day

Load profile data of the University of Ibadan for the year 2017 was used. 70% of the data was used to train the model while 30% was used for testing and validation. 
