from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():

    return render_template('homepage.html')


@app.route('/form')
def show_form():

    return render_template("form.html")


@app.route('/save-name')
def show_results():

    user_name = request.form.args("name")

    session["name"] = user_name

    return redirect('/')


@app.route('/results')
def show_results():

    return render_template("results.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
