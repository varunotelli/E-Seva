import MySQLdb

def connection():
<<<<<<< HEAD
	conn=MySQLdb.connect(host="localhost",user="root",passwd="rootsql",db="test")
=======
	conn=MySQLdb.connect(host="localhost",user="root",passwd="vasi1997@ssn",db="test")
>>>>>>> e0072890cb22cc32edc48d0939ebe0fb9cf62fdf
	c=conn.cursor()
	return c,conn