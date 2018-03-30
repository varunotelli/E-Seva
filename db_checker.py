from dbconnector import connection
from MySQLdb import escape_string as esc
import gc
def check(uid,name):
	z=None
	c,conn=connection()
	row_count = c.execute("select schemes_applied from USER where id='"+str(uid)+"'")
	if row_count>0:

		results=c.fetchall()
		arr=[]
		temp={}
		for row in results:
			#print(row[0].split(','))
			schemes=row[0].split(',')

		for s in schemes:
			print(s)
			c.execute("select * from SCHEMES where id="+s)
			results=c.fetchall()
			for row in results:
				temp[row[1]]=row[4]

		print(temp)

		c.execute("select category from SCHEMES where name='"+name+"'")
		results=c.fetchall()
		for row in results:
			z=row[0]
		'''
		for key_a,vals_a in temp.items():
			for key_b,vals_b in temp.items():
				if temp[key_a]==temp[key_b]:
					print("conflict")
					return True
		'''
		for key,value in temp.items():
			print(key,temp[key])
			if temp[key]==z:
				print("hello")
				return False,key
			else:
				print("no")

		return True,''
	else:
		return True,''

def authuser(username, password):
	c,conn = connection()
	ct=c.execute("select password from EMPS where username = '"+username+"'")
	if ct>0:
		results = c.fetchall()
		for row in results:
			z = row[0]
		'''if password == passwd:
			return True
		else:
			return False'''
		if(z == password):
			return True
		else:
			return False
	return False

def add_scheme(name, description, eligibility, category):
	c,conn = connection()
	#ins = c.execute("insert into SCHEMES values (%s,%s,%s,%s)",(esc(name),esc(description),esc(eligibility),esc(category)))
	ins = c.execute("insert into SCHEMES (name, description, eligibility, category) values (%s,%s,%s,%s);",(esc(name),esc(description),esc(eligibility),esc(category)))
	conn.commit()
	c.close()

def update_scheme(name, description, eligibility, category):
	#return "Update Function"
	c,conn = connection()
	ct = c.execute("select * from SCHEMES where name = (%s)",(esc(name),))
	results = c.fetchall()
	for row in results:
		#n = row[1]
		d = row[2]
		e = row[3]
		ca = row[4]

	if description != "" and description is not None:
		d = description
	if eligibility != "" and eligibility is not None:
		e = eligibility
	if category != "" and category is not None:
		ca = category

	rt = c.execute ("""
   UPDATE SCHEMES
   SET description=%s, eligibility=%s, category=%s
   WHERE name=%s
""", (d,e,ca,name))
	conn.commit()
	c.close()
