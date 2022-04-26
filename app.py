from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model3.pkl', 'rb'))


@app.route('/',methods=['POST','GET'])
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    data1=int(request.form['b'])
    data2=int(request.form['gender'])
    data3=int(request.form['smoking'])
    data4=int(request.form['fingers'])
    data5=int(request.form['anxiety'])
    data6=int(request.form['chronic'])
    data7=int(request.form['peer'])
    data8=int(request.form['alcohol'])
    data9=int(request.form['fatigue'])
    data10=int(request.form['allergy'])
    data11=int(request.form['coughing'])
    data12=int(request.form['wheezing'])
    data13=int(request.form['shortness_of_breath'])
    data14=int(request.form['chest_pain'])
    data15=int(request.form['swallowing_difficulty'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15])
    pred = model.predict([features])

    def statement():
        if pred == 0:
            return 'Result:- The model has predicted that you will not suffer from any cancer but you should take care of your self.'
        elif pred == 1:
            return 'Result:- You should consult with doctor, The model has predicted that you will suffer form cancer.'
    
    return render_template('index.html',statement=statement())


if __name__ == "__main__":
    app.run(debug=True)