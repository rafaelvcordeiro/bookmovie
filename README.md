# bookmovie
#### Video Demo:  <URL HERE>
#### Description:
Bookmovie is a lightweight and intuitive movie bookmarker, aimed to be used. Simple as that.

## Why was this webapp created?
### There are three main reasons:
1. Whenever a friend recommended a movie or tv show, I would write it somewhere, and by the time I had finally the availability to watch it, I just couldn't find it, wasting quite some time.
2. I realized that there are two main factors that guides the decision of what to watch next: the current mood of the viewers and the available time they have. This process of deciding often takes quite some time as well. That's why this webapp has filters for Genres and Duration to aid selecting faster and more accuratelly what is really needed.
3. I wanted a computer science project that would challenge myself and that I could showcase to others, as I am constantly improving my backend software engineering skills.

## Tools and resources used:
+ Flask: the used backend framework is [Flask](https://flask.palletsprojects.com/en/2.2.x/), as it is simple to implement, reliable and light.
+ SQLite3: this webapp uses two SQLite tables, referenced [here](https://pythonbasics.org/flask-sqlite/) and [here](https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/): USERS, that holds users data and RECORDS, that holds all data from each user.
+ Cinemagoer API: to make it easy to add new entries, the [Cinemagoer](https://cinemagoer.github.io/) IMDB API was used, to fill in the add items forms and improve usability.
+ Skeleton: used [Skeleton](http://getskeleton.com/) CSS framework to increase frontend development and design speed. The project seems to be no longer active, but for the basic usage of this webapp where I wanted a minimalistic approach, it suited me perfectly well.
Memegen: used the [Memegen](https://memegen.link/) meme generator for writing automatic error messages and information.
