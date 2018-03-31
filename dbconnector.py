import MySQLdb

def connection():
	conn=MySQLdb.connect(host="localhost",user="root",passwd="vasi1997@ssn",db="test")
	c=conn.cursor()
	return c,conn
