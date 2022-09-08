
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import MySQLdb.cursors
import re
import pandas as pd
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
import speech_recognition as sr
import gtts
from playsound import playsound
import os
import speech
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)
app.secret_key = "mykeys"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)

dfreader = pd.read_csv('rec_sheet.csv')


@app.route('/yor', methods=['GET', 'POST'])
def yoru():
    if request.method == 'POST':
        result = request.form

        text = result['text']
        source = request.form.get('sourc')
        destination = request.form.get('destination')

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        if source == 'English' and destination == 'Yoruba':
            translator = Translator()
            result = translator.translate(
                text=text, src='en', dest='yo')
            res = result.text

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)

            return render_template("home.html", result=res, username=[session['username']][0])

        elif source == 'Yoruba' and destination == 'English':
            translator = Translator()
            result = translator.translate(
                text=text, src='yo', dest='en')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()

# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Yoruba' and destination == 'Igbo':
            translator = Translator()
            result = translator.translate(
                text=text, src='yo', dest='ig')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()

# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Yoruba' and destination == 'Hausa':
            translator = Translator()
            result = translator.translate(
                text=text, src='yo', dest='ha')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()

# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Igbo' and destination == 'English':
            translator = Translator()
            result = translator.translate(
                text=text, src='ig', dest='en')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()

# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'English' and destination == 'Igbo':
            translator = Translator()
            result = translator.translate(
                text=text, src='en', dest='ig')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Igbo' and destination == 'Hausa':
            translator = Translator()
            result = translator.translate(
                text=text, src='ig', dest='ha')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Igbo' and destination == 'Yoruba':
            translator = Translator()
            result = translator.translate(
                text=text, src='ig', dest='yo')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Hausa' and destination == 'English':
            translator = Translator()
            result = translator.translate(
                text=text, src='ha', dest='en')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Hausa' and destination == 'Igbo':
            translator = Translator()
            result = translator.translate(
                text=text, src='ha', dest='ig')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'English' and destination == 'Hausa':
            translator = Translator()
            result = translator.translate(
                text=text, src='en', dest='ha')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        elif source == 'Hausa' and destination == 'Yoruba':
            translator = Translator()
            result = translator.translate(
                text=text, src='ha', dest='yo')

            cursor.execute(
                'INSERT INTO records VALUES (%s, %s, %s)', ([session['id']], [session['username']], text))
            mysql.connection.commit()
# =================================================================================================================
            id = [session['id']]
            username = [session['username']]
            word = text

            data = [[id[0], username[0], word]]
            df = pd.DataFrame(data, columns=['id', 'username', 'word'])
            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('rec_sheet.csv', index=False)
# =================================================================================================================
            speech.spk(source=source, destination=destination, texting=text)
            return render_template("home.html", result=result.text, username=[session['username']])

        else:
            error = 'kindly go back to the home page and pick the correct language'
            return render_template("home.html", result=error)

    return render_template('home.html')


@app.route('/medai/home', methods=['POST', 'GET'])
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM account WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'

    return render_template('index.html', msg="")


@app.route('/spky', methods=['GET', 'POST'])
def spk_yor():
    if request.method == 'POST':

        source = request.form.get('source')

        sou = "'" + source + "'"

        print(sou)

        # try:
        translated = speech.new_spk(sou)
        print(translated)
        # except:
        #   mes = 'an error occurred. no voice recieved.'
        #  return render_template('home.html', msg=mes)

    return render_template('home.html', translated=translated)


@app.route('/medai/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/medai/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM account WHERE username = %s OR password = %s', (username, password))
        account = cursor.fetchone()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg == 'Please fill out the form!'
        else:
            cursor.execute(
                'INSERT INTO account VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('register.html', msg=msg)


@app.route('/medai/ehr', methods=['GET', 'POST'])
def ehr():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'age' in request.form and 'drug' in request.form:

        username = request.form['username']
        age = request.form['age']
        med_condition = request.form['med']
        drug = request.form['drug']
        date = request.form['date']

        # Check if account exists using MySQL

        # If account exists show error and validation checks
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO emr VALUES (%s, %s, %s, %s, %s)', (username, age, med_condition, drug, date))
        mysql.connection.commit()
        msg = 'record added successfully'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('ehr.html', msg=msg)


@app.route('/medai/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/medai/admin')
def admin():

    db = MySQLdb.connect("localhost",
                         "root", "", "pythonlogin")
    cursor = db.cursor()
    cursor.execute("SELECT * from records")
    data = cursor.fetchall()
    db.close()

    # Show the profile page with account info
    return render_template('admin.html', account=data)
    # User is not loggedin redirect to login page


@app.route('/media/sht', methods=['GET', 'POST'])
def sheet():
    os.system("start EXCEL.EXE rec_sheet.csv")

    return render_template('admin.html')


@app.route('/medai/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        username = request.form['username']
        # search by author or book

        conn = MySQLdb.connect(
            "localhost", "root", "", "pythonlogin")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT username, age, medical_condition, drug_prescription, date from emr WHERE username LIKE % s OR medical_condition LIKE % s", (username, username))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and username == 'all':
            cursor.execute(
                "SELECT username, age, medical_condition, drug_prescription, date from records")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)

    return render_template('search.html')


app.run(host='0.0.0.0', port=8080, debug=True)
