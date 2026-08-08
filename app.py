from flask import Flask, render_template

app = Flask(__name__)

todos = [
    {"sno":1,"title":"Sample task","desc":"This is a sample task for todo list","status":"Pending"}

]

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


