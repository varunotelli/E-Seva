import MySQLdb

def connection():
	conn=MySQLdb.connect(host="localhost",user="root",passwd="agpk2424",db="test")
	c=conn.cursor()
	return c,conn