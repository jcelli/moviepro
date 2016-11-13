# Repository: 2016-09.template.project-4
# Assignment #4: SQL  

> Course: **[CS 1656 - Introduction to Data Science](http://cs1656.org)** (CS 2056) -- Fall 2016    
> Instructor: [Alexandros Labrinidis](http://labrinidis.cs.pitt.edu)  
> 
> Assignment: #4
> Released: November 13, 2016  
> **Due:      December 2, 2016**

### Description
This is the **fourth assignment** for the CS 1656 -- Introduction to Data Science (CS 2056) class, for the Fall 2016 semester.

### Goal
The goal of this assignment is for you to gain familiarity with SQL.

---

### What to do

In this assignment you are asked to:  
* update a skeleton Python script (`moviepro.py`) in order to read input from CSV files and insert the data into the `cs1656.sqlite` database, and   
* provide SQL queries that answer 12 questions.

The provided skeleton Python script includes database initialization commands and also includes commands to run the SQL queries and store their output in separate output files, which you should not modify. What you should update are the parts of the script that are responsible for reading in the input data and for specifying the 12 SQL queries.

### Database Schema

The schema of the database is embedded in the `moviepro.py` Python script and should not be modified. It is as follows:
* Actors (aid, fname, lname, gender)  
* Movies (mid, title, year, rank)  
* Directors (did, fname, lname)  
* Cast (aid, mid, role)  
* Movie_Director (did, mid)  


### Reading input from CSV files

Your program should read input from the following CSV files:
* `all_actors.csv`, containing data for the Actors table,  
* `all_cast.csv`, containing data for the Movies table,  
* `all_directors.csv`, containing data for the Directors table,  
* `all_movie_dir.csv`, containing data for the Cast table, and  
* `all_movies.csv`, containing data for the Movie_Director table.
All the data should be inserted into the appropriate tables into the `cs1656.sqlite` database. Sample insert statements have been provided in the `moviepro.py` script, but you are not restricted to doing the insertions in exactly the same way.

Samples of all these files are provided as part of this repository.


### Queries

You are asked to provide SQL queries that provide answers for the following questions. Note that **actors** refers to both male and female actors, unless explicitely specified otherwise.

* **[Q1]** List all the actors (first and last name) who acted in at least one film in the 1st half of the 20th century (1901-1950) and at least one film in the 2nd half of the 20th century (1951 - 2000).  
* **[Q2]** List all the movies (title, year) that were released in the same year as the movie `"Rogue One"`, but had a better rank (Note: the higher the value in the *rank* attribute, the better the rank of the movie).  
* **[Q3]** List all the actors (first and last name) who played in the movie `"Star Wars VII: The Force Awakens"`.   
* **[Q4]** Find the actor(s) (first and last name) who **only** acted in films released before 1985.   
* **[Q5]** List all the directors in descending order of the number of films they directed (first name, last name, number of films directed). 
* **[Q6]** Find the movie(s) with the largest cast (title, number of cast members). Note: show all movies in case of a tie.  
* **[Q7]** Find the movie(s) whose cast has more actresses than actors (i.e., gender=female vs gender=male).  Show the title, the number of actresses, and the number of actors in the results.  
* **[Q8]** List all the actors who were casted in movies  
* **[Q9]** List all  
* **[Q10]** List all  
* **[Q11]** List all  
* **[Q12]** List all  

---

### Important notes about grading
It is absolutely imperative that your python program:  
* runs without any syntax or other errors (using Python 2.7) -- we will run it using the following command:  
`python moviepro.py`  
* strictly adheres to the format specifications for input and output, as explained above.     

Failure in any of the above will result in **severe** point loss. 


### Allowed Python Libraries
You are allowed to use the following Python libraries:
```
argparse
collections
csv
glob
os
pandas
re
string
sqlite3
sys
```
If you would like to use any other libraries, you must ask permission by Sunday, November 18, 2016, using [piazza](http://piazza.cs1656.org).

---

### How to submit your assignment
For this assignment, you must use the repository that was created for you after visiting the classroom link. You need to update the  file `moviepro.py` as described above, and add other files that are needed for running your program. You need to make sure to commit your code to the repository provided. We will clone all repositories shortly after midnight:  
* the day of the deadline **Friday, December 2nd, 2016 (i.e., at 12:15am, Saturday, December 3rd, 2016)**  
* 24 hours later (for submissions that are one day late / -5 points), and  
* 48 hours after the first deadline (for submissions that are two days late / -15 points). 

Our assumption is that everybody will submit on the first deadline. If you want us to consider a late submission, you need to email us at `cs1656-staff@cs.pitt.edu`


### About your github account
It is very important that:  
* Your github account can do **private** repositories. If this is not already enabled, you can do it by visiting <https://education.github.com/>  
* You use the same github account for the duration of the course.  
* You use the github account that you specified during the test assignment.    
