# Importing Funtion for prediction.
from ml_model.predict_flair import pred
from services.predict_url_service import predict_url
from services.predict_file_service import predict_file

import os
from flask import Flask, render_template, request, make_response, jsonify, send_file


app = Flask(__name__, template_folder='templates')


# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return(render_template('main.html'))
    
	if request.method == 'POST':
		prediction = predict_url(request.form['url'])
		return render_template('main.html', result=prediction)


@app.route('/automated_testing', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['upload_file']
		success = predict_file(file)
		if(success["success"] == True):
			return success["data"]
		else:
			return(render_template('404.html'))
if __name__ == '__main__':
    app.run()
