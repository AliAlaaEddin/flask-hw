#!/usr/bin/env python
# encoding: utf-8
import json,pickle
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'name': 'alice','email': 'alice@outlook.com'})

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    record = json.loads(request.data)
    inputParams = [record['gender'],record['married'],record['dependents'],record['education'],record['selfEmployed'],record['applicantIncome'],record['coapplicantIncome'],record['loanAmount'],record['loanAmountTerm'],record['creditHistory']]
    return jsonify({
        "dt": predictResult([inputParams],"dt"),
        "knn": predictResult([inputParams],"knn"),
        "lr": predictResult([inputParams],"lr"),
        "nb": predictResult([inputParams],"nb"),
        "svm": predictResult([inputParams],"svm")
    })


def predictResult(input, model_name):
    try: 
        model = pickle.load(open(model_name+'.sav', 'rb'))
    except:
        print("Unrecognized model name")
        return None
    result = model.predict(input)[0]
    if result == 1:
        return 'Yes'
    else: 
        return 'No'



# . .\adm\Scripts\activate 
# pip install flask  
# $env:FLASK_APP = "main.py"
# flask run