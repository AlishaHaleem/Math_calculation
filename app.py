from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sliding-puzzle')
def sliding_puzzle():
    return render_template('sliding_puzzle.html')

if __name__ == '__main__':
    app.run(debug=True)
