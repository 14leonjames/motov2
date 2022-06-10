
import cv2
import numpy as np
import time
import imutils
import yolo_test
import test
import mo
from flask import Flask, render_template, Response,request


# from ocr import ocr 




# Define a flask app
app = Flask(__name__)





@app.route('/helmet')
def index():
    return render_template('helmet.html')



@app.route('/triples')
def tripl():
    return render_template('triples.html')


@app.route('/mobile')
def mob():
    return render_template('mobile.html')


@app.route('/')
def detec():
    return render_template("main.html")



@app.route('/helpredict', methods=['GET', 'POST']) 
def helemt():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        f.save("img.jpg")
        yolo_test.detect()
        return render_template('result.html')

@app.route('/triplepredict', methods=['GET', 'POST']) 
def trip():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        f.save("img.jpg")
        test.trip()
        return render_template('result.html')

@app.route('/mobilepredict', methods=['GET', 'POST']) 
def mobile():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        f.save("img1.jpg") 
        mo.mobile()
        return render_template('result.html')
        

if __name__=='__main__':
    app.run(debug=True)