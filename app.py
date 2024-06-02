from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder where uploaded files will be stored
app.secret_key = 'your_secret_key'  # Secret key for flashing messages

# Configure SQLAlchemy to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

# Create the SQLAlchemy database instance
db = SQLAlchemy(app)

# Function to check if the uploaded file contains potentially malicious content

def check_file_content(file_path):
    # Here you would implement checks for malicious content in the uploaded file
    # For demonstration purposes, let's assume we're checking for the presence of JavaScript code
    with open(file_path, 'r') as file:
        content = file.read()
        if 'script' in content:
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']  # This input should be sanitized but is not for this example
        return render_template('signup_success.html', email=email)
    return render_template('index.html')

# XSS

@app.route('/signup', methods=['GET', 'POST'])  # Add route decorator for signup page
def signup():
    if request.method == 'POST':
        email = request.form['email']  # This input should be sanitized but is not for this example
        return render_template('signup_success.html', email=email)
    return render_template('signup.html')

# Unrestricted file upload

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            flash('File uploaded successfully!', 'success')
            return redirect(url_for('home'))  # Redirect to home page after upload
    return render_template('upload.html')

# SQLI 

# Test if it's connected

class User(db.Model):
    __tablename__ = 'users'  # Explicitly specify the table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


@app.route('/test')
def test_db_connection():
    # Query all users from the users table
    all_users = User.query.all()
    if all_users:
        usernames = [user.username for user in all_users]
        return f"Usernames: {', '.join(usernames)}"
    else:
        return "No users found in the database"




@app.route('/login', methods=['GET'])
def login():
    try:
        username = request.args.get('username')
        password = request.args.get('password')

        # Vulnerable SQL query with string concatenation
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Welcome, {user[1]}!"
        else:
            return "Invalid username or password."
    except Exception as e:
        # Log the error
        print(f"An error occurred: {e}")
        # Return an error response
        return "An error occurred while processing your request."




if __name__ == '__main__':
    app.run(debug=True)
