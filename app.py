from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Engineering',
    'location': 'India',
    'salary': 'Rs. 15,00,000'
}]

@app.route("/")
def hello():
    return render_template('home.html', jobs=jobs)


@app.route("/home")
def jobs_list():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


@app.route("/jobs")
def jobs():
    return render_template('home.html')
