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
* update a skeleton Python script (`moviepro.py`) in order to read input from CSV files, and   
* provide SQL queries that answer 12 questions.

The provided skeleton Python script includes database initialization commands and also includes output commands, which you should not modify. What you should update are the parts of the script that are responsible for reading in the input data and for running the 12 SQL queries.

### Database Schema

The schema of the database is embedded in the `moviepro.py` Python script and should not be modified. It is as follows:
* ACTOR (id, fname, lname, gender)  
* MOVIE (id, name, year, rank)  
* DIRECTOR (id, fname, lname)  
* CAST (pid, mid, role)  
* MOVIE_DIRECTOR (did, mid)  


### Reading input from CSV files

Your program should read input from the following CSV files:


Samples of all these files are provided as part of this repository.


### Queries

You are asked to provide SQL queries that provide answers for the following questions: 






---

### Important notes about grading
It is absolutely imperative that your python program:  
* runs without any syntax or other errors (using Python 2.7) -- we will run it using the following command:  
`python `  
* strictly adheres to the format specifications for input and output, as explained above.     

Failure in any of the above will result in **severe** point loss. 


### Allowed Python Libraries
You are allowed to use the following Python libraries:
```
argparse
collections
csv
glob
itertools
math 
os
pandas
re
string
sys
```
If you would like to use any other libraries, you must ask permission by Sunday, October 16, 2016, using [piazza](http://piazza.cs1656.org).

---

### How to submit your assignment
For this assignment, you must use the repository that was created for you after visiting the classroom link. You need to update the repository to include file `apriori.py` as described above, and other files that are needed for running your program. You need to make sure to commit your code to the repository provided. We will clone all repositories shortly after midnight:  
* the day of the deadline **Friday, December 2nd, 2016 (i.e., at 12:15am, Saturday, December 3rd, 2016)**  
* 24 hours later (for submissions that are one day late / -5 points), and  
* 48 hours after the first deadline (for submissions that are two days late / -15 points). 

Our assumption is that everybody will submit on the first deadline. If you want us to consider a late submission, you need to email us at `cs1656-staff@cs.pitt.edu`


### About your github account
It is very important that:  
* Your github account can do **private** repositories. If this is not already enabled, you can do it by visiting <https://education.github.com/>  
* You use the same github account for the duration of the course.  
* You use the github account that you specified during the test assignment.    
