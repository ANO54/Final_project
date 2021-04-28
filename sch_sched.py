from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_bootstrap import Bootstrap

import sqlite3 as sql 

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def welcome():
    return "Welcome"

@app.route("/Home/")
def Home_page():
    return render_template("Home.html")

@app.route("/index/")
def index_page():
    return render_template("index.html")

@app.route("/welcome/")
def welcome_page():
    return "Welome to my world"

@app.route("/greetings/")
def greetings_page():
    return "My Greetings"

@app.route("/greetings/christmas")
def christmas_page():
    return "Merry Christmas"

@app.route("/greetings/newyear")
def newyear_page():
    return "Happy New Year"

@app.route("/number/<int:num>")
def page_num(num):
    return "You entered {0}". format(num)

# 
@app.route("/save/<string:student_name>/<string:classes>/<string:years>")
def save_data(student_name, contact, years):
    with sql.connect("schoolschedule.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO STfill (student_names, classes, years) VALUES (?, ?, ?)", [student_names, classes, years])
    con.commit()

    return "Record successfully added {0} {1} {2}".format(student_names, classes, years)

@app.route("/save/<string:student_name>/<string:classes>/<string:grades>")
def save_info(student_name, contact, grades):
    with sql.connect("staffresult.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO STI (student_names, classes, grades) VALUES (?, ?, ?)", [student_names, classes, grades])
    con.commit()

    return "Record successfully added {0} {1} {2}".format(student_names, classes, grades)

@app.route("/STschedule")
def STschedule_data():
    con = sql.connect("schoolschedule.db")
    con.row_factory = sql.Row
        
    cur = con.cursor()
    cur.execute("SELECT * FROM STfill")

    rows = cur.fetchall()
    return render_template("STschedule.html", rows = rows)

@app.route("/Staffinfo")
def Staffinfo_data():
    con = sql.connect("staffresult.db")
    con.row_factory = sql.Row
        
    cur = con.cursor()
    cur.execute("SELECT * FROM STI")

    rows = cur.fetchall()
    return render_template("Staffinfo.html", rows = rows)

# People to see the form
@app.route("/STfilling")
def new_STfilling():
    return render_template("STfilling.html")

@app.route("/Staff")
def new_Staff():
    return render_template("Staff.html")

@app.route("/login")
def new_login():
    return render_template("login.html")


# Adding new student 
@app.route("/addrec", methods=["POST"])
def addrec():
    if request.method == "POST":
        student_names = request.form["sn"]
        classes = request.form["clas"]
        years = request.form["yr"]

        with sql.connect("schoolschedule.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO STfill (student_names, classes, years) VALUES (?, ?, ?)", [student_names, classes, years])
        con.commit()

        return render_template("STschedule.html")

@app.route("/addrecord", methods=["POST"])
def addrecord():
    if request.method == "POST":
        student_names = request.form["sn"]
        classes = request.form["clas"]
        grades = request.form["gd"]

        with sql.connect("staffresult.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO STI (student_names, classes, grades) VALUES (?, ?, ?)", [student_names, classes, grades])
        con.commit()

        return render_template("Staffinfo.html")

#def create_database():
 #  conn = sql.connect("schoolschedule.db")
  # conn.execute("CREATE TABLE STfill (student_names TEXT, classes TEXT, years TEXT)")
   #conn.close()
#create_database()

#def create_database():
   #conn = sql.connect("staffresult.db")
   #conn.execute("CREATE TABLE STI (student_names TEXT, classes TEXT, grades TEXT)")
   #conn.close()
#create_database()

if __name__ == '__main__':
    app.run(debug=True)