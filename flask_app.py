

# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="",
    password="",
    hostname=".",
    databasename="",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

class Average(db.Model):

    __tablename__ = "averages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    time = db.Column(db.Integer)
    value = db.Column(db.String(6))

class Lonaverage(db.Model):

    __tablename__ = "london"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Biraverage(db.Model):

    __tablename__ = "birmingham"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Briaverage(db.Model):

    __tablename__ = "bristol"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Covaverage(db.Model):

    __tablename__ = "coventry"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Leiaverage(db.Model):

    __tablename__ = "leicester"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Livaverage(db.Model):

    __tablename__ = "liverpool"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Manaverage(db.Model):

    __tablename__ = "manchester"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

class Notaverage(db.Model):

    __tablename__ = "nottingham"

    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.String(10))
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)
    windspeed = db.Column(db.Integer)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", averages=Average.query.all(),lonaverages=Lonaverage.query.all(),manaverages=Manaverage.query.all(),biraverages=Biraverage.query.all(),briaverages=Briaverage.query.all(),covaverages=Covaverage.query.all(),notaverages=Notaverage.query.all(),leiaverages=Leiaverage.query.all(),livaverages=Livaverage.query.all(),comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

