# bookmovie
#### Video Demo:  <URL HERE>
#### Description:
Bookmovie is a lightweight and intuitive movie bookmarker, aimed to be used whenever need. Simple as that.
  
## Why was this webapp created?
  This project was innitially conceived as [CS50's](https://cs50.harvard.edu/) course final project. And I decided to build a movie bookmarker because it is based on a simple issue I frequently deal with: what is my next movie or tv series I want to watch? There are three main reasons that supported this choice:
1. Whenever a friend recommended a movie or tv show, I would write it somewhere, and by the time I had finally the availability to watch it, I just couldn't find it, wasting quite some time.
2. I realized that there are two main factors that guides the decision of what to watch next: the current mood of the viewers and the available time they have. This process of deciding often takes quite some time as well. That's why this webapp has filters for Genres and Duration to aid selecting faster and more accuratelly what is really needed.
3. I wanted a computer science project that would challenge myself and that I could showcase to others, as I am constantly improving my backend software engineering skills.
 
## Tools and resources used:
+ **Flask:** the used backend framework is [Flask](https://flask.palletsprojects.com/en/2.2.x/), as it is simple to implement, reliable and light.
+ **SQLite3:** used sqlite3 as the database, and found the following implementation guidelines referenced [here](https://pythonbasics.org/flask-sqlite/) and [here](https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/). This webapp uses two SQLite tables: USERS, that holds users data and RECORDS, that holds all data from each user.
+ **Cinemagoer API:** to make it easy to add new entries, the [Cinemagoer](https://cinemagoer.github.io/) IMDB API was used, to fill in the add items forms and improve usability.
+ **Skeleton:** used [Skeleton](http://getskeleton.com/) CSS framework to increase frontend development speed. The Skeleton project seems to be no longer active, but for the basic usage of this webapp where I wanted a minimalistic approach, it worked and suited my needs perfectly well.
Memegen: used the [Memegen](https://memegen.link/) meme generator for writing automatic error messages and information.

## Files description:
  - **aap.py:** main part of the webapp, that invokes all libraries, manages logged in users sessions and manages all Flask routes.
  - **extras.py:** additional python code, to aid the main code anda make it lighter.
  - **bookmovie.db:** SQLite3 data base, that holds two tables: _users_ for username, password and user related information; _records_ to store all movie/tv series records, with all information the user has inserted in.
  - **add.html:** HTML page for adding new movie entries. In this page, the user can search for the movie title and retrieve automatic data information, provided by the [Cinemagoer](https://cinemagoer.github.io/) IMDB API. There are many fields and the user has the choice to write as much as wanted.
  - **edit.html:** HTML page that is similar to add.html, but it only called when the user wants to edit an already inserted movie. It shows all form fields as in add.html, but showed in a different way.
  - **forgot.html:** this HTML page is still under development, but it will be the place where the user asks for receiving her/his password in the provided email.
  - **index.html:** main page of the webapp, that shows all the inserted movies, holds the filters to aid selecting the best choice, and shows specific details for each item when clicked. This page also allows the user to mark the items as watched, edit them or delete them.
  - **layout.html:** this is the base html code that all other pages refer to and that tells basic HTML information, like headers and reference to external files.
  - **login.html:** this is the page that is loaded when the user is not logged in, and it gives the user the opportunity to log in or register. It also explains basic webapp functionality, resources and tools used.
  - **message.html:** this page manages the [Memegen](https://memegen.link/) meme generator, and returns a proper error mesage, whenever needed.
  - **register.html:** this page is where each new user that wants to use this webapp can register and login later.
