from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():

    return render_template('homepage.html')


@app.route('/form')
def show_form():

    return render_template("form.html")


@app.route('/save-name', methods=['POST'])
def save_name():

    user_name = request.form.get("name")

    session["name"] = user_name

    return redirect('/form')


@app.route('/results', methods=['POST'])
def show_results():

    cheery = request.form.get("cheery")
    honest = request.form.get("honest")
    dreary = request.form.get("dreary")

    if cheery and honest and dreary:
        msg = "With fewer humans on the planet, at least nature has a better chance of surviving."
    elif cheery and honest and not dreary:
        msg = "You are a wonderful human being."
    elif cheery and not honest and not dreary:
        msg = "All humans are good people."
    elif not cheery and honest and dreary:
        msg = "Most humans act in their own self interest, sometimes at the expense of others."
    elif not cheery and not honest and dreary:
        msg = "Climate change will soon render the human population extinct."
    elif not cheery and not honest and not dreary:
        msg = "Tomorrow will be the same as yesterday."

    return render_template("results.html", msg=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
