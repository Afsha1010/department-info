from flask import Flask, render_template,request, url_for, redirect
import pymysql

hostname = "localhost"
user = "root"
password = "asma"

db = pymysql.connections.Connection(
    host=hostname,
    user=user,
    password=password,
    database='student'
)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")


@app.route("/check", methods=["POST"])
def check():
    username = request.form.get("username")
    passwd = request.form.get("password")
    cursor = db.cursor()
    cursor.execute(f"select password from users where username='{username}';")
    password = list(cursor)[0][0]
    if password == passwd:
        return redirect("/admin")
    else:
        return redirect("/login")

@app.route('/logout')
def logout():
    # Clear the session variables upon logout
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/curriculum")
def curriculum():
    return render_template("curriculum.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/insertdata", methods=['POST'])
def adddata():
    username = request.form.get("username")
    email = request.form.get("email")
    passwd = request.form.get("password")
    cursor = db.cursor()
    try:
        cursor.execute(f"insert into users(username, email, password) values('{username}','{email}','{passwd}');")
        db.commit()
        return redirect("/admin")
    except Exception as e:
        return redirect("/signup")



@app.route("/developers")
def developers():
    return render_template("developers.html")


@app.route("/timetable")
def timetable():
    return render_template("timetable.html")


@app.route("/staffs")
def staffs():
    return render_template("staffs.html")


if __name__ == "__main__":
    app.run(debug=True)