

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

# Vulnerabilities and their exploitation

### XSS

### Unrestricted File Upload

### SQL Injection Auth Bypass
' OR 1=1 --
When successful, you'll notice the welcome messge "Welcome, admin!" at the top of the screen.
