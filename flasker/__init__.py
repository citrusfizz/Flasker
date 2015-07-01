from observe import observeAccount
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os
import random

app = Flask(__name__)



@app.route('/observe.html', methods=['GET', 'POST'])
def return_imgur_image():
    if request.method == 'POST':
        if not request.form['text']:
                return "You need to put something after the command"
        text = request.form['text']
        #req = {'text': get_imgur_image(text)}
        #return jsonify(**req)
        #print request.form[1]
        f = request.form
#        for key in f.keys():
#           for value in f.getlist(key):
#                print  key, ":",value
	print("hellow!!!")
        return observeAccount(text) + "test"
    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
