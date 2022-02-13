from flask import Flask, render_template, request, redirect
import api_refresh
import datetime
import json
from backend import employee
from backend.coords_api_func import get_coords
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html", title="Dashboard", dashboard="active")


@app.route("/employees", methods=["GET", "POST"])
def emp():
    if request.method == "POST":
        api_refresh.refresh(today = datetime.date.today())
    with open("database/db.json", "r") as f:
        db = json.load(f)
    return render_template("employees.html", title="Employees", emp="active", db = db)


@app.route("/add_employee", methods=["GET", "POST"])
def add_emp():
    if request.method == "POST":
        emp_num, first, last, email, phone_number, city, post_code = request.form.get("emp_no"), request.form.get("first"), request.form.get("last"), request.form.get("email"), request.form.get("phone_number"), request.form.get("city"), request.form.get("post_code")
        employee.user_Create(get_coords, user_EmployeeNumber=emp_num, firstname=first, lastname=last, email=email, phone_number=phone_number, city=city, post_code=post_code, weather=None, news=None)
    return render_template("add_emp.html", title="Add Employee", add_emp="active")


@app.route("/remove_employee/<int:employee_num>")
def remove_emp(employee_num):
    employee.user_Delete(int(employee_num))
    return redirect("/employees")


if __name__ == "__main__":
    app.run(debug=True)
