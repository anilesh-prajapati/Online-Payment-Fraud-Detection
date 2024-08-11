

from flask import Flask,render_template,request
import pickle
import numpy as np



app = Flask(__name__)


#load the model
model_path = 'fraud_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)



#home page
@app.route('/')
def home():
    return render_template('index.html', **locals())


@app.route('/predict', methods = ['POST','GET'])
def predict ():
    v1 = float ( request.form['type'] ) 
    v2 = float ( request.form['amount']  ) 
    v3 = float ( request.form['oldbalanceOrg'] ) 
    v4 = float ( request.form['newbalanceOrig']  ) 
     
    


    result = model.predict ([[v1,v2,v3,v4]]) [0]

    return render_template('index.html', **locals())



if __name__ == '__main__':
    app.run ()








