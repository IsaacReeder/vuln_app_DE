from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']  # This input should be sanitized but is not for this example
        return render_template('signup_success.html', email=email)
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])  # Add route decorator for signup page
def signup():
    if request.method == 'POST':
        email = request.form['email']  # This input should be sanitized but is not for this example
        return render_template('signup_success.html', email=email)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


