from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model2.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['e'])
    data6=float(request.form['f'])
    data7=float(request.form['g'])
    data8=float(request.form['h'])
    data9=float(request.form['i'])
    data10=float(request.form['j'])
    data11=float(request.form['k'])
    data12=float(request.form['l'])
    data13=float(request.form['m'])
    data14=float(request.form['n'])
    data15=float(request.form['o'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15])
    pred = model.predict([features])

    def statement():
        if pred == 0:
            return 'Result:- The model has predicted that you will not suffer from any cancer but you should take care of your self.'
        elif pred == 1:
            return 'Result:- You should consult with doctor, The model has predicted that you will suffer form cancer.'
    
    return render_template('home.html',statement=statement())


if __name__ == "__main__":
    app.run(debug=True)