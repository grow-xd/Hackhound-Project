from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'hackhoundusers'

# Initialize MySQL
mysql = MySQL(app)

# Configure session
app.secret_key = 'secret_key'

# Define login route
@app.route('/', methods=['GET', 'POST'])
def login():
    # Check if user is already logged in
    if 'email' in session:
        return redirect('/dashboard')
    # Check if user has submitted the login form
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Query database for user credentials
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cur.fetchone()
        # Check if user exists and password is correct
        if user:
            # Store user email in session
            session['email'] = email
            # Redirect user to dashboard
            return redirect('/dashboard')
        else:
            # Show error message if credentials are invalid
            return render_template('login.html', error='Invalid email or password')
    # Show login form if user has not submitted it
    return render_template('login_signup.html')


if __name__ == '__main__':
    app.run(debug=True)
