from flask import Flask,render_template,request,redirect,url_for,session
app = Flask(__name__)
app.secret_key = 'super-secret-key'
@app.route('/')
def home():
    if 'logged_in' in session and session['logged_in'] == True:
        return render_template('welcome.html')



@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if 'logged_in' in session and session['logged_in']==True:
        print("Already logged in ")
        return render_template('welcome.html')
    if request.method=='POST':
        if request.form['uname']!='abc' or request.form['pass']!='abc':
            error="Invalid credentials"
        else:
            session['logged_in']=True
            print("Post method")
            return redirect('/welcome')
    print("Here as well")
    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    if 'logged_in' in session and session['logged_in'] == True:
        return render_template('welcome.html')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('login'))


app.run(debug=True)