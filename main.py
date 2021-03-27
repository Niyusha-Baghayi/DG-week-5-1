from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np

##creating a flask app and naming it "app"
app = Flask(__name__)

##loading the model from the saved file
with open('model_files/model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text="MEDV (Median value of owner-occupied homes in $1000's) should be $ {}".format(output))


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = round(prediction[0], 2)
    return jsonify(output)


if __name__ == '__main__':
    app.run()

    