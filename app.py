from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            reading_score_str = request.form.get('reading_score')
            writing_score_str = request.form.get('writing_score')

            if not reading_score_str or not writing_score_str:
                return render_template('home.html', error="Please provide both reading and writing scores.", form_data=request.form)

            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(reading_score_str),
                writing_score=float(writing_score_str)
            )
            pred_df = data.get_data_as_dataframe()

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            formatted_result = round(float(results[0]), 2)
            return render_template('home.html', results=formatted_result, form_data=request.form)

        except Exception as e:
            return render_template('home.html', error=f"Prediction error: {str(e)}", form_data=request.form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

        