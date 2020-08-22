from flask import Flask,render_template

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    nm="rohan das"
    return render_template('about.html',name=nm)

app.run(debug=True)