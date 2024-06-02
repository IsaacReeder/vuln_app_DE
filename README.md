

               ______________
             /             /|
            /             / |
           /____________ /  |
          | ___________ |   |
          ||           ||   |
          ||           ||   |
          ||           ||   |
          ||___________||   |
          |   _______   |  /
         /|  (_______)  | /
        ( |_____________|/
         \
     .=======================.
     | ::::::::::::::::  ::: |
     | ::::::::::::::[]  ::: |
     |   -----------     ::: |
     `-----------------------'

     ___      ___  _      ____  __ __    ___  ____     ___     __ ______ 
    |   \    /  _]| T    l    j|  T  |  /  _]|    \   /  _]   /  ]      T
    |    \  /  [_ | |     |  T |  |  | /  [_ |  D  ) /  [_   /  /|      |
    |  D  YY    _]| l___  |  | |  |  |Y    _]|    / Y    _] /  / l_j  l_j
    |     ||   [_ |     T |  | l  :  !|   [_ |    \ |   [_ /   \_  |  |  
    |     ||     T|     | j  l  \   / |     T|  .  Y|     T\     | |  |  
    l_____jl_____jl_____j|____j  \_/  l_____jl__j\_jl_____j \____j l__j  

# Install

### Start the app
cd my_flask_app

### Create virtual environment
python3 -m venv venv

### Activate virtual environment
source venv/bin/activate

### Install Flask
pip install Flask

### Run Flask app
python app.py

### Set up SQL, Enter Shell (MacOS)
sqlite3 mydatabase.db

### Create a Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

### Insert Data
INSERT INTO users (username, password) VALUES
    ('admin', 'admin123'),
    ('user', 'password123');

### Exit SQLite Shell
.exit

# Vulnerabilities and their Mitigation

### XSS

#### How to exploit

Submit Malicious Script: An attacker submits a form with a malicious script as the email input, such as: <script>alert('Hello Pieter and Rui!');</script>

#### Explanation

The code for the home and signup routes is vulnerable to Cross-Site Scripting (XSS) because user input (the email parameter) is directly rendered in the signup_success.html template without sanitization. This allows an attacker to inject malicious scripts that can be executed in the user's browser.

#### Mitigation

- Input Validation: Validate and sanitize user inputs on the server-side to ensure they don't contain malicious code.
- Output Encoding: Ensure that user input is properly escaped in templates to prevent script execution.
- Use Templating Engines: Use templating engines like Jinja2, which auto-escape variables by default.

### Unrestricted File Upload

#### How to exploit

Uploading any type of file, including those with malicious content.

#### Explanation

The code in the `/upload` route is vulnerable to unrestricted file upload because it saves any uploaded file without validating its type or content. This can lead to the execution of malicious files on the server. To fix this, validate the file type and size, use a secure filename, and store files in a secure location.

#### Mitigation

- ALLOWED_EXTENSIONS defines a set of allowed file extensions. E.G 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'
- The allowed_file() function checks if the uploaded file extension is allowed.
- secure_filename() can be used to sanitize the file name.
- MAX_CONTENT_LENGTH limits the maximum file size.

- Limit File Types: Allow only specific file types to be uploaded.
- Validate File Size: Set a maximum file size limit for uploads.
- Sanitize File Names: Remove potentially dangerous characters from file names.
- Scan for Malicious Content: Implement file content scanning for malicious content detection.
- Store Uploaded Files Securely: Store files outside the web root directory with proper permissions.
- Use a Content Delivery Network (CDN): Serve uploaded files through a CDN for added security.
- Implement User Authentication and Authorization: Require authentication and restrict uploads to authorized users.
- Monitor and Log Upload Activities: Log file upload activities for monitoring and detecting suspicious behavior.

### SQL Injection Auth Bypass

#### How to exploit
Enter ' OR 1=1 -- into both the username and password fields. If successful, you'll see the message "Welcome, admin!" at the top of the screen.

#### Explanation

Lines 86 and 87 in this code are vulnerable to SQL injection because the SQL query is constructed using string concatenation, directly incorporating user input without any sanitization.

Line 86: query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
Line 87: cursor.execute(query)

#### Mitigation:

- Use Parameterized Queries: Prevent SQL injection by using parameterized queries, which separate SQL code from data.
- Sanitize User Input: Ensure that user inputs are sanitized and validated before use.
- Use ORM: Leverage an Object-Relational Mapping (ORM) tool like SQLAlchemy to abstract SQL queries and automatically escape inputs.
