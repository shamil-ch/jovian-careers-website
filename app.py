from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'banglore',
  'salary': 'Rs. 30000'
},
{
  'id': 2,
  'title': 'Data Scientist',
  'location': 'mumbai',
  'salary': 'Rs. 50000'
},
{
  'id': 3,
  'title': 'software developer',
  'location': 'banglore',
  'salary': 'Rs. 15000'
},
  {
  'id': 4,
  'title': 'frontend developer',
  'location': 'delhi',
  'salary': 'Rs. 25000'
},
  {
  'id': 5,
  'title': 'backend developer',
  'location': 'kochi',
  'salary': 'Rs. 30000'
},
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS)
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)