from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'hellstern@waasedemo'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Naimo6868/?'
app.config['MYSQL_DATABASE_DB'] = 'companyusers'
app.config['MYSQL_DATABASE_HOST'] = 'waasedemo.mysql.database.azure.com' 
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser',(_name, _email , _password))
            conn.commit()

    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run()