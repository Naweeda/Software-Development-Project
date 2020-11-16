# THIS IS HOME BLUEPRINT for home, about, login and signup
from flask import Blueprint, render_template, request, session, redirect, url_for
# from db import SearchingDB

# db = SearchingDB()

def initHome(db):
# create a blue print
    home = Blueprint('home', __name__)

    @home.route('/', methods=['GET'])
    def homepage():
        postings = db.getAllPostings()
        lst = db.getPostingOrganizedData(postings)
        recent_posts = db.getPostingbyOrderedDate()
        ordered_lst = db.getPostingOrganizedData(recent_posts)
        for l in lst:
            s = l['image'].split("/")[-1]
            l['image'] = "media/" + s 
        if 'name' in session:
            user = db.getAUser("All",session['name'])
            favorites = db.getfavoritePostings(session['email'])
            fav_postings = db.getPostingOrganizedData(favorites)
            return render_template('home/home.html', data = lst, recent = ordered_lst, fav = fav_postings, user=user)
        return render_template('home/home.html', data = lst, recent = ordered_lst)
        
    @home.route('/about')
    def about():
        if 'loggedin' in session:
            return render_template("home/about.html",user=session['firstname'])
        return render_template("home/about.html")

    @home.route('/about/<name>')
    def getPerson(name):
        item = f"home/about/{name}.html"
        if 'loggedin' in session:
            return render_template(item, name = name,user=session['firstname'])
        return render_template(item, name = name)

    @home.route('/login',methods =['GET','POST'])
    def login():
        if request.method == 'POST':
            email =request.form['email']
            password =request.form['password']
            account = db.checkAUser(email,password)
            if account :
                # session['loggedin'] = True
                session['email'] = request.form['email']
                user = db.getUserOrganizedData(account)
                session['name'] = user[0]['fname']
                return redirect(url_for('home.homepage'))
            else :
                return render_template("home/login.html", message = "email or password is incorrect")
        return render_template("home/login.html")


    @home.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            user = {}
            user['email'] = request.form['email']
            user['password'] = request.form['password']
            user['fname'] = request.form['fname']
            user['lname'] = request.form['lname']
            db.insertAUser(user)
            return render_template("home/login.html" , message = "Account is created")
        return render_template("home/signup.html")

    @home.route('/logout')
    def logout():
        session.pop('email',None)
        session.pop('name',None)
        return redirect(url_for("home.homepage"))

    return home




