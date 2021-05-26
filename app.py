from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_classifier.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        satisfaction = float(request.form['satisfaction'])
        if(satisfaction<0 or satisfaction>1):
            return render_template('index1.html',prediction_texts="Please,enter values between 0 to 1 for satisfaction level.")
        last_evaluation=float(request.form['last_evaluation'])
        if(last_evaluation<0 or last_evaluation>1):
            return render_template('index1.html',prediction_texts="Please,enter values between 0 to 1 for last evaluation.")
        number_project=int(request.form['number_project'])
        if(number_project<0):
            return render_template('index1.html',prediction_texts="Please,enter a valid numbers for projects.")
        average_montly_hours=int(request.form['average_montly_hours'])
        if(average_montly_hours<0):
            return render_template('index1.html',prediction_texts="Please,enter valid number of hours for average monthly hours.")
        time_spend_company=int(request.form['time_spend_company'])
        if(time_spend_company<0):
            return render_template('index1.html',prediction_texts="Please,enter valid years for time spent in company.")
        Work_accident=int(request.form['Work_accident'])
        promotion=int(request.form['promotion'])
        Department=int(request.form['Department'])
        salary=int(request.form['salary'])
        prediction=model.predict([[satisfaction,last_evaluation,number_project,average_montly_hours,time_spend_company,Work_accident,promotion,Department,salary]])
        output=int(prediction)
        if output==0:
            return render_template('index1.html',prediction_texts="The employee will not leave the job.")
        elif output==1:
            return render_template('index1.html',prediction_texts="The employee will leave the job.")
        else:
            return render_template('index1.html',prediction_text="Please,enter valid values.")
    else: 
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)