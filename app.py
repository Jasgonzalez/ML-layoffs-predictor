from flask import Flask, render_template, request

app = Flask(__name__)

#home route
@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/predict')
def Predict():
    return

if __name__ == '__main__':
    app.run(debug=True)