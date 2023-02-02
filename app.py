from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def a():
    return render_template('test.html')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        prompt = request.json
        print(prompt)
    return jsonify({"hello":prompt})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)