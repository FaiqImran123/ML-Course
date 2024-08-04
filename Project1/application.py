from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

application =Flask(__name__)
app =application


## Import ridge regressor and scaler pickle
ridge_reg =pickle.load(open("Models/ridge.pkl", "rb"))
standard_scaler =pickle.load(open("Models/scaler.pkl", "rb"))
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/pred", methods =["GET", "POST"])
def prediction():
    if request.method=="GET":
        return render_template("predict.html")
    else:
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_reg.predict(new_data_scaled)
        return render_template("predict.html", results =round(result[0], 2))




if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)


    