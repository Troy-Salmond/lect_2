from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/<string:name>")
def named(name):
    return render_template("index.html", name=name)

@app.route('/form', methods=["POST"])
def form():
    name_f = request.form.get('first_n')
    return f"<h1>{name_f}</h1>"





if __name__ == "__main__":
    app.run(debug=True)
