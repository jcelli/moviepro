import sqlite3 as lite
import csv
import argparse
import collections
import glob
import os
import pandas
import re
import string
import sys

con = lite.connect('cs1656.sqlite')

with con:
    cur = con.cursor()

    ########################################################################
    ### CREATE TABLES ######################################################
    ########################################################################
    # DO NOT MODIFY - START
    cur.execute('DROP TABLE IF EXISTS Actors')
    cur.execute("CREATE TABLE Actors(aid INT, fname TEXT, lname TEXT, gender CHAR(6), PRIMARY KEY(aid))")

    cur.execute('DROP TABLE IF EXISTS Movies')
    cur.execute("CREATE TABLE Movies(mid INT, title TEXT, year INT, rank REAL, PRIMARY KEY(mid))")

    cur.execute('DROP TABLE IF EXISTS Directors')
    cur.execute("CREATE TABLE Directors(did INT, fname TEXT, lname TEXT, PRIMARY KEY(did))")

    cur.execute('DROP TABLE IF EXISTS Cast')
    cur.execute("CREATE TABLE Cast(aid INT, mid INT, role TEXT)")

    cur.execute('DROP TABLE IF EXISTS Movie_Director')
    cur.execute("CREATE TABLE Movie_Director(did INT, mid INT)")
    # DO NOT MODIFY - END

    ########################################################################
    ### READ DATA FROM FILES ###############################################
    ########################################################################
    # actors.csv, movies.csv, directors.csv, cast.csv, movie_director.csv
    # UPDATE THIS

    # open files individually and read them into their own dataframes
    # use values from dataframes to insert them into the database
    actVals = ['aid', 'fname', 'lname', 'gender']
    actors = pandas.read_csv('all_actors.csv', header=None)
    actors.columns = actVals
    cast = pandas.read_csv('all_cast.csv', header=None)
    cast.columns = ['aid', 'mid', 'role']
    directors = pandas.read_csv('all_directors.csv', header=None)
    directors.columns = ['did', 'fname', 'lname']
    movies = pandas.read_csv('all_movies.csv', header=None)
    movies.columns = ['mid', 'title', 'year', 'rank']
    moviedir = pandas.read_csv('all_movie_dir.csv', header=None)
    moviedir.columns = ['did', 'mid']

    ########################################################################
    ### INSERT DATA INTO DATABASE ##########################################
    ########################################################################
    # UPDATE THIS
    # cur.execute("INSERT INTO Actors VALUES(1001, 'Harrison', 'Ford', 'Male')")
    # cur.execute("INSERT INTO Actors VALUES(1002, 'Daisy', 'Ridley', 'Female')")

    # cur.execute("INSERT INTO Movies VALUES(101, 'Star Wars VII: The Force Awakens', 2015, 8.2)")
    # cur.execute("INSERT INTO Movies VALUES(102, 'Rogue One: A Star Wars Story', 2016, 8.0)")

    # cur.execute("INSERT INTO Cast VALUES(1001, 101, 'Han Solo')")
    # cur.execute("INSERT INTO Cast VALUES(1002, 101, 'Rey')")

    # cur.execute("INSERT INTO Directors VALUES(5000, 'J.J.', 'Abrams')")

    # cur.execute("INSERT INTO Movie_Director VALUES(5000, 101)")

    ########################################################MY CODE ####################################
    # use to_sql to add the values in the dataframes to the databases
    actors.to_sql('Actors', con, if_exists='append', index=False)
    cast.to_sql('Cast', con, if_exists='append', index=False)
    directors.to_sql('Directors', con, if_exists='append', index=False)
    movies.to_sql('Movies', con, if_exists='append', index=False)
    moviedir.to_sql('Movie_Director', con, if_exists='append', index=False)

    cur.execute('DROP VIEW IF EXISTS actorearliest')

    ###################################################END MY CODE####################################
    con.commit()

    ########################################################################
    ### QUERY SECTION ######################################################
    ########################################################################
    queries = {}

    # DO NOT MODIFY - START
    # DEBUG: all_movies ########################
    # queries['all_movies'] = '''
    # SELECT * FROM Movies
    # '''
    # DEBUG: all_actors ########################
    # queries['all_actors'] = '''
    # SELECT * FROM Actors
    # '''
    # DEBUG: all_cast ########################
    # queries['all_cast'] = '''
    # SELECT * FROM Cast
    # '''
    # DEBUG: all_directors ########################
    # queries['all_directors'] = '''
    # SELECT * FROM Directors
    # '''
    # DEBUG: all_movie_dir ########################
    #	queries['all_movie_dir'] = '''
    # SELECT * FROM Movie_Director
    # '''
    # DO NOT MODIFY - END

    ########################################################################
    ### INSERT YOUR QUERIES HERE ###########################################
    ########################################################################

    # Q1 ########################
    # Thought for this one is do a query of two queries one for first half
    # another for the second half and return the intersection of the two
    queries['Q1'] = '''
SELECT fname, lname
FROM Actors JOIN "Cast" ON Actors.aid = "Cast".aid
JOIN Movies ON Movies.mid = "Cast".mid
WHERE Movies.year > 1900 AND Movies.year < 1951
INTERSECT
SELECT fname, lname
FROM Actors JOIN "Cast" ON Actors.aid = "Cast".aid
JOIN Movies ON Movies.mid = "Cast".mid
WHERE Movies.year > 1950 AND Movies.year < 2000
'''

    # Q2 ########################
    queries['Q2'] = '''
SELECT title, year
FROM Movies
WHERE year =
(SELECT year
FROM Movies
WHERE title = 'Rogue One: A Star Wars Story')
AND rank >
(SELECT rank
FROM Movies
WHERE title = 'Rogue One: A Star Wars Story')
'''

    # Q3 ########################
    queries['Q3'] = '''
SELECT fname, lname
FROM Actors JOIN "Cast" ON Actors.aid = "Cast".aid
JOIN Movies ON Movies.mid = "Cast".mid
WHERE Movies.title = 'Star Wars VII: The Force Awakens'
'''

    # Q4 ########################
    queries['Q4'] = '''
SELECT fname, lname
FROM Actors
WHERE aid NOT IN
(SELECT Actors.aid
FROM Actors JOIN "Cast" ON Actors.aid = "Cast".aid
JOIN Movies ON Movies.mid = "Cast".mid
WHERE Movies.year > 1984)
'''
    # Q5 ########################
    queries['Q5'] = '''
SELECT Directors.fname, Directors.lname, count(mid)
FROM Directors join Movie_Director on Directors.did = Movie_Director.did
GROUP BY Directors.did
ORDER BY count(mid) DESC
'''

    # Q6 ########################
    queries['Q6'] = '''
SELECT title, COUNT(Actors.aid) as curCount
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
GROUP BY title
HAVING curCount = (
    SELECT max(actcnt) as maxVal
    FROM (
        SELECT count(Actors.aid) as actcnt
        FROM Movies join "Cast" on Movies.mid = "Cast".mid
        Join Actors on "Cast".aid = Actors.aid
        GROUP BY title
    )
)
'''

    # Q7 ########################
    queries['Q7'] = '''
SELECT title, Female, Male
From(
SELECT title, SUM(Gender = 'Female') as Female, SUM(Gender = 'Male') as Male
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
GROUP by title
)
WHERE Female > Male
'''
    # Q8 ########################
    queries['Q8'] = '''
SELECT Actors.fname, Actors.lname, COUNT(DISTINCT did)
FROM Actors join "Cast" on Actors.aid = "Cast".aid
join Movie_Director on "Cast".mid = Movie_Director.mid
GROUP BY Actors.aid
Having Count(Distinct did) >  6
'''

    # Q9 ########################
    # table gets actor id and min year
    cur.execute('''
CREATE VIEW actorearliest as
SELECT Actors.aid as actid, MIN(year) as minyear
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
GROUP BY Actors.aid''')
    queries['Q9'] = '''
SELECT fname, lname, count(Movies.mid) as sort
FROM actorearliest join Actors on actorearliest.actid = Actors.aid
Join "Cast" on "Cast".aid = Actors.aid
Join Movies on "Cast".mid = Movies.mid
WHERE year = minyear
Group by Actors.aid
ORDER BY sort DESC
'''

    # Q10 ########################
    queries['Q10'] = '''
SELECT Actors.lname, title
FROM Actors join "Cast" on Actors.aid = "Cast".aid
Join Movie_Director on "Cast".mid = Movie_Director.mid
Join Directors on Movie_Director.did = Directors.did
Join Movies on "Cast".mid = Movies.mid
Where Actors.lname = Directors.lname
'''

    # Q11 ########################
    cur.execute('DROP VIEW IF EXISTS Bacon1')
    # create view for bacon degree 1 just aid
    cur.execute('''
CREATE VIEW Bacon1 as
SELECT ACTORS.aid
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
WHERE Movies.mid = (
SELECT Movies.mid
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
WHERE Actors.fname = "Kevin" AND Actors.lname = "Bacon")
''')

    queries['Q11'] = '''
SELECT role
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
WHERE Actors.aid in (
    SELECT Actors.aid
    FROM Movies join "Cast" on Movies.mid = "Cast".mid
    Join Actors on "Cast".aid = Actors.aid
    WHERE movies.mid in (
        SELECT Movies.mid
        FROM Movies join "Cast" on Movies.mid = "Cast".mid
        Join Actors on "Cast".aid = Actors.aid
        WHERE Actors.aid in Bacon1
        )
    )
AND Actors.aid not in Bacon1
'''
    # Q12 ########################
    queries['Q12'] = '''
SELECT Actors.fname, Actors.lname, AVG(rank) as sort
FROM Movies join "Cast" on Movies.mid = "Cast".mid
Join Actors on "Cast".aid = Actors.aid
Group By Actors.aid
ORDER BY sort DESC
LIMIT 20
'''


    ########################################################################
    ### SAVE RESULTS TO FILES ##############################################
    ########################################################################
    # DO NOT MODIFY - START
    for (qkey, qstring) in queries.items():
        try:
            cur.execute(qstring)
            all_rows = cur.fetchall()

            print "=========== ", qkey, " QUERY ======================"
            print qstring
            print "=========== ", qkey, " RESULTS ===================="
            for row in all_rows:
                print row
            print " "

            with open(qkey + '.csv', 'wb') as f:
                writer = csv.writer(f)
                writer.writerows(all_rows)
                f.close()

        except lite.Error as e:
            print "An error occurred:", e.args[0]
        # DO NOT MODIFY - END
