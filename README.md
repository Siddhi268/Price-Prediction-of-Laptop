# Price-Prediction-of-Laptop

1.Designed a web app that predicts the price of the laptop given the configurations.
2.Scraped the laptops data from flipkart.com using python and BeautifulSoup package.
3.Developed Linear, Random Forest Regressors, and XGBoost Regressors model and also XGBoost with GridsearchCV to get the best model.
4.Deployed the Machine Learning model using streamlit library

## Web Scraping
This is the Flipkart website comprising of different laptops. This page contains the specifications of 24 laptops. So now looking at this, we try to extract the different features of the laptops such as:

1.Title	
2.Price	
3.Rating	
4.Processors	
5.RAM	
6.OS	
7.Storage	
8.Display	
9.Warranty
So we extract the data from 30 pages so our dataset now consists of the information the 709 different laptops.

## Feature Engineering
We go through all the features one by one and keep adding new features. I have made the following changes and created new variables: RAM - Made columns for Ram Capacity in GB
Processor - Made columns for Name of the Processor, Type of the Processor, Generation
Operating System - Parsed the Operating System from this column and made a new column
Storage - Made new columns for the type of Disk Drive 
Display - Made new columns for touchscreen
Description - Made new columns for the company and graphic card

## Data Preprocessing
There are a few columns which are categorical here but they actually contain numerical values.So we need to convert few categorical columns to numerical columns and also need to handle missing values.

## Model Building
Applied label encoding and converted the categorical variables into numerical ones.Then I splited the data into training and test sets with a test size of 30%. I tried three different models ( Linear Regression, Random Forest Regression, XGBoost) and evaluated them using R-square.

## Model Deployment
I have deployed the model using Streamlit library.
