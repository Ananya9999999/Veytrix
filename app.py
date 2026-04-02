from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression  # Train on admissions data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        gpa = float(request.form['gpa'])
        projects = int(request.form['projects'])  
        budget = float(request.form['budget'])  

        pred = min(95, 50 + gpa*8 + projects*15)  
        
        total_cost = 42000000 
        roi_years = total_cost / (150000*1200000 - 2000000*1200000)  
        
        return render_template('result.html', pred=pred, cost=total_cost/1e6, roi=roi_years)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)