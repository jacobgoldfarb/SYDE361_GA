from flask import Flask, request
from main import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/GA_api', methods=['GET','POST']) # Replace with POST
def GA_api():
    composition_str = request.args['Composition']
    # composition_str = request.form['Composition']
    composition = composition_str.strip('][').split(',')
    final_comp = run_GA(composition) # send in list of note strings

    return '''The input composition is {}, the GA output is {}'''.format(composition_str, final_comp) # replace with "return {JSON}"

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, port=5000)