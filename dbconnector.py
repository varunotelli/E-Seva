import MySQLdb

def connection():
	conn=MySQLdb.connect(host="localhost",user="root",passwd="sonu",db="test")
	c=conn.cursor()
	return c,conn