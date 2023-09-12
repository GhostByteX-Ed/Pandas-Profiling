from flask import Flask,render_template
import pandas as pd
from pandas_profiling import ProfileReport

app = Flask('__name__',template_folder='template')
@app.route('/')
def home():
   
    data = pd.read_csv("IRIS.csv")
    profile = ProfileReport(data)
    print(profile)
    profile.to_file("Profiling_Report_Results.html")
    return render_template("Profiling_Report_Results.html")

if(__name__=='__main__'):
    app.run(debug=True,host="0.0.0.0",port=5000)

