# flask , scikit-learn , pandas , pickle-mixin --> pip install

#creating a template for flask
import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)
data= pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl",'rb'))
#opening in read mode


@app.route('/')
def index():

    #to get the values listed in the data
    locations= sorted(data['location'].unique())

    #to send the value
    return render_template('index.html', locations=locations)

#to get the predicted value
@app.route('/predict' , methods=['POST'])

def predict():
    #given the name in the form to get the data

    # Get data from the form with default values if empty
    location = request.form.get('location', 'Unknown')  # Default to 'Unknown' if empty
    bhk = float(request.form.get('bhk') or 0)  # Default to 0 if empty
    bath = float(request.form.get('bath') or 0)  # Default to 0 if empty
    sqft = float(request.form.get('total_sqft') or 0)  # Default to 0 if empty

    #correct to do : convert BHK and bath to float

    print(location , bhk , bath , sqft)

    #feeding the columns the pipe was trained on
    input = pd.DataFrame([[location, sqft, bath, bhk]],columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipe.predict(input)[0] * 1e5

    return str(np.round(prediction,2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)