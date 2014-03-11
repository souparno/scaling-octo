# all the imports
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import session
from flask import url_for
from flask import abort
from flask import flash
from flask import g
import sqlite3
import os


app = Flask(__name__)
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='1222FGGRF43557CDV',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()

    cur = db.execute('select count(*) as strength,current_location from resume group by current_location limit 10')
    current_location = cur.fetchall()

    cur = db.execute('select count(*) as strength,preferred_location from resume group by preferred_location limit 10')
    preferred_location = cur.fetchall()

    cur = db.execute('select count(*) as strength,current_employer from resume group by current_employer limit 10')
    current_employer = cur.fetchall()

    cur = db.execute(
        'select count(*) as strength, current_designation from resume group by current_designation limit 10')
    current_designation = cur.fetchall()

    cur = db.execute('select count(*) as strength, ug_course from resume group by ug_course limit 10')
    ug_course = cur.fetchall()

    cur = db.execute('select count(*) as strength, pg_course from resume group by pg_course limit 10')
    pg_course = cur.fetchall()

    cur = db.execute('select count(*) as strength, ppg_course from resume group by ppg_course limit 10')
    ppg_course = cur.fetchall()

    return render_template('search.html',
                           current_location=current_location,
                           preferred_location=preferred_location,
                           current_employer=current_employer,
                           current_designation=current_designation,
                           ug_course=ug_course,
                           pg_course=pg_course,
                           ppg_course=ppg_course)


@app.route('/result', methods=("GET", "POST"))
def result():
    searchQuery = []
    if request.method == 'POST':

        if request.form.getlist('Inp_currentlocation'):
            searchQuery.append("current_location in (" + ",".join(
                request.form.getlist('Inp_currentlocation')) + ")")

        if request.form.getlist('Inp_preferredLocation'):
            searchQuery.append("preferred_location in (" + ",".join(
                request.form.getlist('Inp_preferredLocation')) + ")")

        if request.form.getlist('Inp_currentemployer'):
            searchQuery.append("current_employer in (" + ",".join(
                request.form.getlist('Inp_currentemployer')) + ")")

        if request.form.getlist('Inp_currentdesignation'):
            searchQuery.append("current_designation in (" + ",".join(
                request.form.getlist('Inp_currentdesignation')) + ")")

        if request.form.getlist('Inp_ugcourse'):
            searchQuery.append("current_designation in (" + ",".join(
                request.form.getlist('Inp_ugcourse')) + ")")

        if request.form.getlist('Inp_pgcourse'):
            searchQuery.append("pg_course in (" + ",".join(
                request.form.getlist('Inp_pgcourse')) + ")")

        if request.form.getlist('Inp_ppgcourse'):
            searchQuery.append("ppg_course in (" + ",".join(
                request.form.getlist('Inp_ppgcourse')) + ")")

        searchQuery = " select * from resumes where " + " and ".join(searchQuery) + ";"
    return render_template('result.html',searchQuery=searchQuery)
    #return redirect(url_for('show_entries'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
