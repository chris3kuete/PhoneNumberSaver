import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

#currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

all_contact = []

# configure the SQLite database, relative to the app instance folder, create database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ContactList.db"

# create the extension
db = SQLAlchemy()

# initialize the app with the extension
db.init_app(app)


class phoneBook_tbl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    number = db.Column(db.String(250), nullable=False)
    print("created chris table successfully")


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

app.route("/")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contactpage")
def contactpage():
    return render_template("add.html")


@app.route("/addcontact", methods=['POST', 'GET'])
def addcontact():
    if request.method == 'POST':
        # CREATE RECORD
        new_contact = phoneBook_tbl(
            name=request.form["name"],
            number=request.form["number"],
        )
        db.session.add(new_contact)
        all_contact.append(new_contact)
        db.session.commit()
        return render_template("result.html", contacts=all_contact)



if __name__ == "__main__":
    app.run(debug=True)
