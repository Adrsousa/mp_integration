from flask import Flask, render_template

app = Flask(__name__)

@app.route("/products")
def products():
    return render_template("e_commerce.html")


if __name__ == '__main__':
    app.run(debug=True)