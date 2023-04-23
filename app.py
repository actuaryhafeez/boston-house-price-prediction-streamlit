import joblib
import streamlit as st
import numpy as np

# Loading the saved model
filename = 'model/xgb_model.pkl'
model = joblib.load(filename)

# Define a function that will take in a set of features and 
# return the predicted price of the house
def predict_price(crim, zn, indus, nox, rm, age, dis, tax, ptratio, b, lstat):
    
    # Create a numpy array with the input features
    input_features = np.array([[crim, zn, indus, nox, rm, age, dis, tax, ptratio, b, lstat]])
    
    # Use the loaded model to make predictions
    price_pred = model.predict(input_features)[0]
    return price_pred

# Define a Streamlit app
def main():
    st.title('Boston House Price Prediction')
    st.write('This app predicts the median value of owner-occupied homes in Boston.')
    
    # Add input fields for each feature
    crim = st.number_input('Per capita crime rate by town', format='%f')
    zn = st.number_input('Proportion of residential land zoned for lots over 25,000 sq.ft.', format='%f')
    indus = st.number_input('Proportion of non-retail business acres per town', format='%f')
    nox = st.number_input('Nitric oxides concentration (parts per 10 million)', format='%f')
    rm = st.number_input('Average number of rooms per dwelling', format='%f')
    age = st.number_input('Proportion of owner-occupied units built prior to 1940', format='%f')
    dis = st.number_input('Weighted distances to five Boston employment centres', format='%f')
    tax = st.number_input('Full-value property-tax rate per $10,000', format='%f')
    ptratio = st.number_input('Pupil-teacher ratio by town', format='%f')
    b = st.number_input('1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town', format='%f')
    lstat = st.number_input('Lower status of the population (percent)', format='%f')
    
    # When the user clicks the 'Predict' button, make a prediction
    if st.button('Predict'):
        price_pred = predict_price(crim, zn, indus, nox, rm, age, dis, tax, ptratio, b, lstat)
        st.success('The predicted price of the house is $%.2f' % price_pred)

if __name__=='__main__':
    main()
