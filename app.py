from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import requests
import json
from imdb import Cinemagoer, helpers
import sqlite3
from flask import g
from datetime import datetime
from extras import message, login_required
from werkzeug.security import check_password_hash, generate_password_hash

# References for using sqlite3 with python and flask
# 1) https://pythonbasics.org/flask-sqlite/
# 2) https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/


app = Flask(__name__)
# Configure session to use filesystem (instead of signed cookies)
# This part was used the same as CS50's Finance exercise
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    #Ensure responses aren't cached
    # This part was used the same as CS50's Finance exercise
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


genresList = ["Action","Comedy","Drama","Nonsense","Romance","Sci-Fi","History","Fantasy","Adventure","Crime","Family","Mystery","Music","Documentary",\
              "Animation","Biography","Film-Noir","Horror","Musical","Short-Film","Sport","Superhero","Thriller","War","Western"]

@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    connect = sqlite3.connect("bookmovie.db")
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM records WHERE user_id =? ORDER BY id DESC;",[user_id])
    movieData = cursor.fetchall()
    cursor.execute("SELECT username FROM users WHERE id = ?;", [user_id])
    username = cursor.fetchall()
    return render_template("index.html", movieData=movieData, genresList=genresList, username=username)


@app.route("/edit", methods = ["GET", "POST"])
@login_required
def edit():
    user_id = session["user_id"]
    if request.method == "POST":
        
        recordId = request.form.get("recordId")
        print("this is the current record being edited: ", recordId)
        GenresList = request.form.getlist("cbGenre")
        Genres = ",".join(GenresList)
        Title = request.form.get("textMovieTitle")
        Rating = request.form.get("textMovieRating")
        Duration = request.form.get("selectMovieDuration")
        Type = request.form.get("selectMovieType")
        Platform = request.form.get("selectMoviePlatform")
        Trailer = request.form.get("textMovieTrailer")
        Country = request.form.get("textMovieCountry")
        Writer = request.form.get("textMovieWriter")
        Cast = request.form.get("textMovieCast")
        Poster = request.form.get("textMoviePoster")
        Watched = request.form.get("cbWatched")
        if Watched == "on":
            Watched = "yes"
        else:
            Watched = "no"
        Plot = request.form.get("textMoviePlot")
        Comment = request.form.get("textMovieComment")
        Year = request.form.get("textMovieYear")
        recordDate = current_dateTime = datetime.now()
        
        # Adjusts the URL to be embedded in the website
        urlTrailer1 = "https://youtu.be/"
        urlTrailer2 = "https://www.youtube.com/embed/"
        urlTrailer3 = "https://www.youtube.com/watch?v="
        
        if urlTrailer1 in Trailer:
            youtubeId = Trailer[17:]
            Trailer = urlTrailer2 + youtubeId
        elif urlTrailer3 in Trailer:
            youtubeId = Trailer[32:]
            Trailer = urlTrailer2 + youtubeId

        with sqlite3.connect("bookmovie.db") as db:
            cursor = db.cursor()
        cursor.execute("UPDATE records SET genres = ?,title = ?,rating = ?,duration = ?,type = ?,\
                    platform = ?,trailer = ?,country = ?,writer = ?,cast = ?,poster = ?,watched = ?,\
                    plot = ?,comment = ?,year = ? WHERE id = ? AND user_id = ?;",\
                        (Genres,Title,Rating,Duration,Type,Platform,Trailer,Country,Writer,Cast,Poster,Watched,Plot,Comment,Year, recordId, user_id))
        db.commit()
            
        return redirect("/")
    
    else:
        # Method is GET
        recordId = request.args.get("recordIdEdit")
        print("the ID of the current record is: ",recordId)

        connect = sqlite3.connect("bookmovie.db")
        connect.row_factory = sqlite3.Row
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM records WHERE id = ? AND user_id = ?", (recordId, user_id))
        recordData = cursor.fetchall() 

        return render_template("edit.html",d=recordData, genresList=genresList, user_id=user_id)
    

@app.route("/watched", methods=["POST"])
@login_required
def watched():
    user_id = session["user_id"]
    recordId = request.form.get("recordIdWatched")
    print("this is the current record being edited: ", recordId)

  
    with sqlite3.connect("bookmovie.db") as db:
        cursor = db.cursor()
    
    cursor.execute("SELECT watched FROM records WHERE id = ? AND user_id = ?", (recordId,user_id))
    recordData = cursor.fetchall()

    Watched = recordData[0][0]
    if Watched == 'yes':
        Watched = 'no'
    elif Watched == 'no':
        Watched = 'yes'

    cursor.execute("UPDATE records SET watched = ? WHERE id = ? AND user_id = ?;",(Watched,recordId, user_id))
    db.commit()
        
    return redirect("/")    


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    user_id = session["user_id"]
    recordId = request.form.get("recordIdDelete")
    print("this is the current record being deleted: ", recordId)
    
    with sqlite3.connect("bookmovie.db") as db:
        cursor = db.cursor()
    cursor.execute("DELETE FROM records WHERE id = ?", [recordId])  # When 
    db.commit()
        
    return redirect("/")    


@app.route("/write", methods=["POST"])
@login_required
def write():
    user_id = session["user_id"]
    GenresList = request.form.getlist("cbGenre")
    Genres = ",".join(GenresList)
    Title = request.form.get("textMovieTitle")
    Rating = request.form.get("textMovieRating")
    Duration = request.form.get("selectMovieDuration")
    Type = request.form.get("selectMovieType")
    Platform = request.form.get("selectMoviePlatform")
    Trailer = request.form.get("textMovieTrailer")
    Country = request.form.get("textMovieCountry")
    Writer = request.form.get("textMovieWriter")
    Cast = request.form.get("textMovieCast")
    Poster = request.form.get("textMoviePoster")
    Watched = request.form.get("cbWatched")
    if Watched == "on":
        Watched = "yes"
    else:
        Watched = "no"
    Plot = request.form.get("textMoviePlot")
    Comment = request.form.get("textMovieComment")
    initialtext = "Try to answer why should you watch it and expend your precious time of life with it."
    if Comment == initialtext:
        Comment = ""

    Year = request.form.get("textMovieYear")
    recordDate = current_dateTime = datetime.now()
    

    # Adjusts the URL to be embedded in the website
    urlTrailer1 = "https://youtu.be/"
    urlTrailer2 = "https://www.youtube.com/embed/"
    urlTrailer3 = "https://www.youtube.com/watch?v="
    
    if urlTrailer1 in Trailer:
        youtubeId = Trailer[17:]
        Trailer = urlTrailer2 + youtubeId
    elif urlTrailer3 in Trailer:
        youtubeId = Trailer[32:]
        Trailer = urlTrailer2 + youtubeId


    with sqlite3.connect("bookmovie.db") as db:
        cursor = db.cursor()
    cursor.execute("INSERT INTO records (user_id,genres,title,rating,duration,type,platform,trailer,country,writer,cast,poster,watched,plot,comment,year,recordDate)\
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(user_id,Genres,Title,Rating,Duration,Type,Platform,Trailer,Country,Writer,Cast,Poster,Watched,\
                                                            Plot,Comment,Year, recordDate))
    db.commit()
        
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    ia = Cinemagoer()
    listData = []
    dictData = {}
       

    if request.method == "POST":
        #CINEMAGOER API, easier and simpler, but i found it to be a litle slow to retrieve data.
        title = request.form.get("textSearchIMDB")
        movieSearch = ia.search_movie(title)
        movie_id = movieSearch[0].movieID
        movie = ia.get_movie(movie_id)

        #get 20 casts first names in a single string object
        
        try:
            dictData["cast"] = movie.data["cast"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["cast"]=""
                
        try:
            dictData["movieTitle"] = movie.data["title"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["movieTitle"] = ""
                    
        try:
            dictData["kind"] = movie.data["kind"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["kind"] = ""

        try:
            coverurl= movie.data["cover url"]
            dictData["imageurl"] = helpers.resizeImage(coverurl,280)
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["imageurl"] = ""

        try:
            dictData["genres"] = movie.data["genres"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["genres"] = ""

        try:
            dictData["duration"] = movie.data["runtimes"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["duration"] = ""
        
        try:
            dictData["rating"] = movie.data["rating"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["rating"] = ""
        
        try:
            dictData["plot"] = movie.data["plot"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["plot"] = ""

        try:
            dictData["countries"] = movie.data["countries"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["countries"] = ""

        try:
            dictData["writer"] = movie.data["writer"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["writer"] = ""

        try:
            dictData["year"] = movie.data["year"]
        except(IndexError, KeyError, AttributeError, NameError):
            dictData["year"] = ""
        
        
                   
        return render_template("add.html", dictData=dictData, genresList=genresList, movieInfoState="ligado")
    else:
        dictData["cast"]=""
        dictData["movieTitle"] = ""
        dictData["kind"] = ""
        dictData["imageurl"] = "/static/images/no_image.png"
        dictData["genres"] = ""
        dictData["duration"] = ""
        dictData["rating"] = ""
        dictData["plot"] = ""
        dictData["writer"] = ""
        dictData["countries"] = ""
        dictData["year"] = ""
        return render_template("add.html", dictData=dictData, genresList=genresList, movieInfoState="desligado")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    #Log user in

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Sets up database connection
        connect = sqlite3.connect("bookmovie.db")
        connect.row_factory = sqlite3.Row
        cursor = connect.cursor()

        username = request.form.get("username")
        
        # Ensure username was submitted
        if not username:
            return message("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return message("must provide password", 403)

        # Query database for username
        cursor.execute("SELECT * FROM users WHERE username = ?", [username])
        row = cursor.fetchall()
        print("1.row: ",row)
        print("2.row[0]: ",row[0])
        print("3.row[0]['id']: ",row[0]['id'])
        # Ensure username exists and password is correct
        if len(row) != 1 or not check_password_hash(row[0]["hash"], request.form.get("password")):
            return message("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = row[0]["id"]
        print("4. user logged in for user_id:", row[0]["id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    #Log user out

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Sets up database connection
        with sqlite3.connect("bookmovie.db") as db:
            cursor = db.cursor()
                
        # Sets up variable names
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        email= request.form.get("email")

        # Check if email is blank
        if not email:
            return message("must provide email", 400)

        # Check if username is blank
        if not username:
            return message("must provide username", 400)

        # Check if username already exists      
        cursor.execute("SELECT * FROM users WHERE username = ?", [username])
        usernameDB = cursor.fetchall()
        print("1.usernameDB: ",usernameDB)

        if usernameDB:
            return message("User already exists", 400)

        # Checks if password is null or if confirmation matches password
        if not password:
            return message("Must provide password", 400)

        # Checks if confirmation matches password
        if password != confirmation:
            return message("Both passwords must match", 400)

        # Hash the password
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # Insert new user to database
        cursor.execute("INSERT INTO users (username,hash,email) VALUES (?,?,?)",(username,hash,email))
        db.commit()
        print("2.new user successfully added")

        # Starts session for the newest registered user
        cursor.execute("SELECT id FROM users WHERE username = ?", [username])
        recordData = cursor.fetchall()
        user_id = recordData[0][0]
        print("3.user_id: ",user_id)
        session["user_id"] = user_id#[0]["id"]
        print("4.session started for user_id: ", user_id)

        # Redirect user to home page
        return redirect("/")

    else:
        # method is GET
        return render_template("register.html")


@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    if request.method == "POST":
        return message("sorry, functionality not implemented yet")
    else:
        return render_template("forgot.html")


    @app.route("/settings", methods=["GET"])
def settings():
    return message("sorry, functionality not implemented yet")


if __name__ == '__app__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
