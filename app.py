from flask import Flask, request, render_template
import os
import numpy as np
import pandas as pd
from wine_quality_prediction_project.pipeline.prediction import PredictionPipeline

# initialize the flask app
app = Flask(__name__)

# route to display the home page
@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

# route to train the pipeline
@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training completed!"

# route to predict the wine quality and show the result in the web page
@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity']) # same as what's in the index.html file
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
            # converting the inputs to a numpy array and reshape it to 1, 11, because the model expects the input in this shape
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            # do the prediction
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # show the result in the web page
            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    # if the method is GET, then return the home page
    else:
        return render_template('index.html')
    

# run the app
if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True) # debug=True will reload the server when the code changes