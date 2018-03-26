from dbconnector import connection
def check(uid,name):
	z=None
	c,conn=connection()
	row_count = c.execute("select schemes_applied from user where id='"+str(uid)+"'")
	if row_count>0:

		results=c.fetchall()
		arr=[]
		temp={}
		for row in results:
			#print(row[0].split(','))
			schemes=row[0].split(',')

		for s in schemes:
			print(s)
			c.execute("select * from schemes where id="+s)
			results=c.fetchall()
			for row in results:
				temp[row[1]]=row[4]

		print(temp)

		c.execute("select category from schemes where name='"+name+"'")
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


