from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html", title="Dashboard", dashboard="active")


@app.route("/employees")
def emp():
    return render_template("employees.html", title="Employees", emp="active")


@app.route("/add_employee")
def add_emp():
    return render_template("add_emp.html", title="Add Employee", add_emp="active")


if __name__ == "__main__":
    app.run(debug=True)
