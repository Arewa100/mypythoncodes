from flask import Flask, make_response
from flask import redirect, abort

app: Flask = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    if name == "John":
        return redirect("/new_user")
    else:
        return "<h1>bad request %s</h1>" % name , 400

@app.route("/new_user")
def new_user():
    return "<h1>welcome new user </h1>"


#using the abort response function
@app.route("/testing_abort/<current_name>")
def testing_abort(current_name):
    if not current_name == "john":
        return abort(404)
    return "<h1>testing abort %s</h1>" % current_name


# @app.route("/")
# def test_response_object():
#     response = make_response("<h1>this contains a cookie</h1>")
#     response.set_cookie("name", "John")
#     return response

if __name__ == "__main__":
    app.run(debug=True)