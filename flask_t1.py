#!/usr/bin/env python3
# Author : Annamalai Rajeev Chinnikannu  rajeev.chinnikannu@colorado.edu
# name   : Homework 7 (flask_server )
# purpose: Data Communications Python Assignment
# date   : 07-11-2018
# version: 3.7
#!/usr/bin/env python3

from flask import Flask, render_template, Markup
from flask import request
from prettytable import PrettyTable
import sqlite3


def pretty_table(row_p, db):

    table = PrettyTable(["planet", "distance", "mass"])
    for row in row_p:
        table.add_row([row[0], row[1], row[2]])
    db.close()
    return table


def perform_a():

    try:
        db = sqlite3.connect('rajeev1-dbplanet.sql3.db')
        db.row_factory = sqlite3.Row
        query_st = "select * from planetdata order by planet"
        c = db.cursor()
        c.execute(query_st)
        row = c.fetchall()
        table = pretty_table(row, db)
        return table

    except sqlite3.OperationalError:
        print('Error file doesnt exist')


def perform_d(st1):

    try:
        db = sqlite3.connect('rajeev1-dbplanet.sql3.db')
        db.row_factory = sqlite3.Row
        query_st = "select * from planetdata where planet=?"
        t = (st1,)
        c = db.cursor()
        c.execute(query_st, t)
        row = c.fetchall()
        table = pretty_table(row, db)
        return row
    except sqlite3.OperationalError:
        print("file not available")
        return []


app = Flask(__name__)


@app.errorhandler(404)
def pageNotFound(e):
    return "page not found"


@app.errorhandler(500)
def error_page(e):
    return "Oops   ENTRY NOT FOUND IN DATABASE"


@app.route('/', methods=['GET'])
def index():
    data = '''<!DOCTYPE html>
<html lang="en">



<head>
    <meta charset="UTF-8">
    <title>PLANETS</title>
</head>
<style>
a:link {
    color: green;
    background-color: transparent;
    text-decoration: none;
}
a:visited {
    color: darkorange;
    background-color: transparent;
    text-decoration: none;
}
a:hover {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}
a:active {
    color: yellow;
    background-color: transparent;
    text-decoration: underline;
}
</style>
<body style="background-color:powderblue;">
HOME
<br />
<a href="all_planets">
    gets all  planet info </a>
<br /> <br />
<a href="specific_planets" >
    gets a specific planet info </a>
</body>
</html>'''
    return data


@app.route('/all_planets', methods=['GET', 'POST'])
def all_planets():
    if request.method == 'GET':
        table1 = perform_a()
        print(table1)
        data = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>
<h2>Planets</h2>
<table style="width:100%">
  <tr>
    <th>planet</th>
    <th>distance</th>
    <th>mass</th>
  </tr>
  <tr>
    <td>earth</td>
    <td>149.6</td>
    <td>5.97</td>
  </tr>
  <tr>
    <td>jupiter</td>
    <td>778.6</td>
    <td>1898</td>
  </tr>
  <tr>
    <td>mars</td>
    <td>227.9</td>
    <td>0.642</td>
  </tr>
  <tr>
    <td>mercury</td>
    <td>57.9</td>
    <td>0.33</td>
  </tr>
  <tr>
    <td>neptune</td>
    <td>4495.1</td>
    <td>102</td>
  </tr>
  <tr>
    <td>pluto</td>
    <td>5906.4</td>
    <td>0.0146</td>
  </tr>
  <tr>
    <td>saturn</td>
    <td>1433.5</td>
    <td>568</td>
  </tr>
  <tr>
    <td>saturn</td>
    <td>1433.5</td>
    <td>568</td>
  </tr>
  <tr>
    <td>uranus</td>
    <td>2872.5</td>
    <td>86.8</td>
  </tr>
  <tr>
    <td>venus</td>
    <td>108.2</td>
    <td>4.87</td>
  </tr>
</table>
</body>
</html>'''
        return data


@app.route('/specific_planets', methods=['GET', 'POST'])
def specific_planets():

    if request.method == 'GET':
        return render_template("planetsform.html")


@app.route('/one_planet', methods=['GET', 'POST'])
def one_planet():

    if request.method == 'GET':
        return render_template("planetsform.html")

    if request.method == 'POST':
        message_received = request.form.get('message')
        print("the message is:" + message_received)
        message_received = message_received.lower()

        row = perform_d(message_received)
        if len(row) != 0:

            for row in row:
                return render_template("planets.html", planet=row[0], distance=row[1], mass=row[2])
        else:
            print("Entry not found")
    else:
        print()


if __name__ == '__main__':

    app.debug = True
    app.run(host='0.0.0.0', port=80)
