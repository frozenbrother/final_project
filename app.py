from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#Home
@app.route('/',methods=['POST','GET'])
def home():
    return render_template("index.html")

#Index
@app.route('/index.html')
def index():
    return render_template('index.html')

#Info
@app.route('/info.html')
def info():
        return render_template('info.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    data1=int(request.form['a'])
    data2=int(request.form['b'])
    data3=int(request.form['c'])
    data4=int(request.form['d'])
    data5=int(request.form['e'])
    data6=int(request.form['f'])
    data7=int(request.form['g'])
    data8=int(request.form['h'])
    data9=int(request.form['i'])
    data10=int(request.form['j'])
    data11=int(request.form['k'])
    data12=int(request.form['l'])
    data13=int(request.form['m'])
    data14=int(request.form['n'])
    data15=int(request.form['o'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15])
    pred = model.predict([features])

    def statement():
        if pred == 0:
            return 'Result:- The model has predicted that you may not suffer from lung cancer but you should take care of your health.'
        elif pred == 1:
            return 'Result:- You should consider to consult with a doctor. The model has predicted that you may suffer from lung cancer.'
    
    return render_template('index.html',statement=statement())


if __name__ == "__main__":
    app.run(debug=True)