from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operator = request.form['operation']
        if operator == 'add':
            result = float(num1) + float(num2)
        elif operator == 'subtract':
            result = float(num1) - float(num2)
        elif operator == 'multiply':
            result = float(num1) * float(num2)
        elif operator == 'divide':
            result = float(num1) / float(num2)
        return render_template('results.html', result=result)  

@app.route('/postman_action', methods=['POST'])
def math_ops1():
    if request.method == 'POST':
        num1 = request.json['num1']
        num2 = request.json['num2']
        operator = request.json['operation']
        if operator == 'add':
            result = float(num1) + float(num2)
        elif operator == 'subtract':
            result = float(num1) - float(num2)
        elif operator == 'multiply':
            result = float(num1) * float(num2)
        elif operator == 'divide':
            result = float(num1) / float(num2)
        return jsonify(result)
        

if __name__ == '__main__':
    app.run(host="0.0.0.0")