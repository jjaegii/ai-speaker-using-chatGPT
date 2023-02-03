from flask import Flask, render_template, request, jsonify
import chat

app = Flask(__name__)


@app.route('/')
def a():
    return render_template('speaker.html')


@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        prompt = request.json
        print(prompt)
        answer = chat.ask(prompt)
        print(answer)
        return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
