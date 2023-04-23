# boston-house-price-prediction-streamlit
 This is a web application that predicts the median value of owner-occupied homes in Boston using an XGBoost model. The app is built using Streamlit and can be accessed through a web browser. 

# Description
This is a web application that predicts the median value of owner-occupied homes in Boston using an XGBoost model. The app is built using Streamlit and can be accessed through a web browser. Users can input values for various features of a house and the app will return a predicted price. 

In order to avoid any discrepancies between the model and app versions, I have created a Python virtual environment (venv) where I have installed the necessary libraries and dependencies including Jupyter notebook, Streamlit, Pandas, Matplotlib, XGBoost, and Scikit-learn. Both the model and app will be using the same requirements to ensure compatibility and smooth functioning. 

### How to Use
#### To run the app, first clone the repository:
    git clone https://github.com/actuaryhafeez/boston-house-price-prediction-streamlit.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment. 
    source venv/bin/activate
#### Next, install the required packages using pip:
    pip install -r requirements.txt
### Run Jupyter Notebook using the following command to open notebook.ipynb
    jupyter notebook
#### Then, run the app:
    streamlit run app.py

![xg_boost](https://user-images.githubusercontent.com/55107467/233838979-b69b8a4b-85a2-41ea-8e91-cf22e471e0dc.png)

## Project Structure 

    movie-recommender-system-streamlit/
        ├── data/
        │   
        ├── model/
        │   └── xgb_model.pkl
        ├── app.py/
        │  
        ├── notebook.ipynb/
        ├── requirements.txt/
        ├── README.md/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).


# References

### Acknowledgements
This project was built using the following tools and resources:

* Python
* Streamlit
