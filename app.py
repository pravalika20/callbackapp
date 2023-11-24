from flask import Flask, render_template, request, session, redirect, url_for   
  
app = Flask(__name__)  
app.secret_key = 'secret-key' # this should be a long, random string  


users = {  
    'john': 'qwerty@123',  
    'jane': 'qwerty@113'  
}  


# @app.route('/')  
# def success():  
#     return render_template('success.html')

@app.route('/')  
def home():  
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])  
def login():  
    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  
        if username in users and users[username] == password:  
            session['username'] = username  
            return redirect(url_for('dashboard'))  
        else:  
            return render_template('login.html', error='Invalid username or password')  
    else:  
        return render_template('login.html')
    
@app.route('/logout')  
def logout():  
    session.pop('username', None)  
    return redirect(url_for('login'))
  
if __name__ == '__main__':  
    app.run(debug=True)