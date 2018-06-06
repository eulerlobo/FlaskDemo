from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

from sqlalchemy.engine.url import URL
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)
mysql = MySQL()

#MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = '{{user}}'
app.config['MYSQL_DATABASE_PASSWORD'] = '{{password}}'
app.config['MYSQL_DATABASE_DB'] = 'bucketlist'
#app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'

mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

@app.route("/signUp", methods=['POST'])
def signUp():

    #read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    _hashed_password = generate_password_hash(_password)

    query = ("INSERT INTO user (user_name, user_username, user_password) VALUES (%s, %s, %s)")


    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute(query, (_name, _email, _hashed_password))
    data = cursor.fetchall()

    #validate the received values
    if len(data) is 0:
        connection.commit()

        return json.dumps({'html': '<span>All fields good!!</span>'})
    else:
        return json.dumps({'error': str(data[0])})

if __name__ == "__main__":
    app.run()