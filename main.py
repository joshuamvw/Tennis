from flask import Flask, redirect, url_for, render_template
import Test 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def test():
    data = Test.displayEvents()
    return render_template("test.html", events=data)

@app.route("/fundraisers", methods=['GET', 'POST'])
def test2():
    data = Test.displayFundRaiserEvents()
    return render_template("test.html", events=data)


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)