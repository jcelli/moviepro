import sqlite3 as lite
import csv
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

	########################################################################		
	### INSERT DATA INTO DATABASE ##########################################
	########################################################################		
	# UPDATE THIS
	cur.execute("INSERT INTO Actors VALUES(1001, 'Harrison', 'Ford', 'Male')") 
	cur.execute("INSERT INTO Actors VALUES(1002, 'Daisy', 'Ridley', 'Female')")   

	cur.execute("INSERT INTO Movies VALUES(101, 'Star Wars VII: The Force Awakens', 2015, 8.2)") 
	cur.execute("INSERT INTO Movies VALUES(102, 'Rogue One: A Star Wars Story', 2016, 8.0)")
	
	cur.execute("INSERT INTO Cast VALUES(1001, 101, 'Han Solo')")  
	cur.execute("INSERT INTO Cast VALUES(1002, 101, 'Rey')")  

	cur.execute("INSERT INTO Directors VALUES(5000, 'J.J.', 'Abrams')")  
	
	cur.execute("INSERT INTO Movie_Director VALUES(5000, 101)")  

	con.commit()	

	########################################################################		
	### QUERY SECTION ######################################################
	########################################################################		
	queries = {}

	# DO NOT MODIFY - START 	
	# DEBUG: all_movies ########################
	queries['all_movies'] = '''
SELECT * FROM Movies
'''	
	# DEBUG: all_actors ########################
	queries['all_actors'] = '''
SELECT * FROM Actors
'''	
	# DEBUG: all_cast ########################
	queries['all_cast'] = '''
SELECT * FROM Cast
'''	
	# DEBUG: all_directors ########################
	queries['all_directors'] = '''
SELECT * FROM Directors
'''	
	# DEBUG: all_movie_dir ########################
	queries['all_movie_dir'] = '''
SELECT * FROM Movie_Director
'''	
	# DO NOT MODIFY - END

	########################################################################		
	### INSERT YOUR QUERIES HERE ###########################################
	########################################################################		

	# Q1 ########################		
	
	# Q2 ########################		

	# Q3 ########################		

	# Q4 ########################		

	# Q5 ########################		

	# Q6 ########################		

	# Q7 ########################		

	# Q8 ########################		

	# Q9 ########################		

	# Q10 ########################		

	# Q11 ########################		

	# Q12 ########################		


	########################################################################		
	### SAVE RESULTS TO FILES ##############################################
	########################################################################		
	# DO NOT MODIFY - START 	
	for (qkey, qstring) in queries.items():
		try:
			cur.execute(qstring)
			all_rows = cur.fetchall()
			
			print "=========== ",qkey," QUERY ======================"
			print qstring
			print "=========== ",qkey," RESULTS ===================="
			for row in all_rows:
				print row
			print " "

			with open(qkey+'.csv', 'wb') as f:
				writer = csv.writer(f)
				writer.writerows(all_rows)
				f.close()
		
		except lite.Error as e:
			print "An error occurred:", e.args[0]
	# DO NOT MODIFY - END
	
