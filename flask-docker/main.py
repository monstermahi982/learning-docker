from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "hello monster"

@app.route('/monster')
def monster():
    return {"data" : "hello monster"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
 