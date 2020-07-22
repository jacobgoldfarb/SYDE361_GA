from flask import Flask, request
from main import *
from Fitness import *
from Composition import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/GA_api', methods=['GET','POST']) # Replace with POST
def GA_api():
    composition_str = request.args['Composition']
    # composition_str = request.form['Composition']
    composition = composition_str.strip('][').split(',')
    final_comp = getOutput(composition) # send in list of note strings
    return {
        "input": composition,
        "output": final_comp[0],
        "output_score": final_comp[1]
    }
    # return '''The input composition is {}, the GA output is {}'''.format(composition_str, final_comp) # replace with "return {JSON}"

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, port=5000)