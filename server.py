#flag=False
from flask import Flask,send_file,request,render_template,redirect,url_for,session,flash,jsonify
#from pdf import create
from fpdf import FPDF,HTMLMixin
import os
from json import dump
import xml.etree.ElementTree as ET
from db_checker import check, authuser
from dbconnector import connection
from sms import send
visible="readonly"
error=''
flag=False
schemeName=''
class MyFPDF(FPDF, HTMLMixin):
	pass


app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
#flag=False
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found</h1>", 404


@app.route("/", methods=["GET","POST"])
def index():
	if not session.get('logged_in'):
		if request.method == 'POST':
			username = request.form['username']
			password = request.form['password']
			#if request.form['password'] == 'password' and request.form['username'] == 'admin':
			if authuser(username,password) == True:
				session['logged_in'] = True

				session['user'] = username

				return redirect(url_for('schemeList'))

			else:
				flash('Wrong password!')
				#debug
			return str(username + " " + password)	
		return render_template("login.html")
	else:
		return redirect(url_for('schemeList'))

@app.route("/scheme",methods=["GET","POST"])
def schemeList():
	global error
	global flag
	if flag:
		flag=False
	else:
		error=''
	print("error=",error)
	return render_template("scheme.html",error=error)



'''@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		if request.form['password'] == 'password' and request.form['username'] == 'admin':
			session['logged_in'] = True
			return redirect(url_for('card'))
		else:
			flash('Wrong password!')
	return render_template("login.html")'''

@app.route("/card",methods=["GET","POST"])
def card():
	return render_template("upload.html")

'''@app.route("/card",methods=["GET","POST"])
def card():
	if request.method=="POST":
		if request.form["id-type"]=="aadhar-card":
			return render_template("upload.html")
		else:
			visible=""
			return render_template("complete.html",data="",vis=visible,error='')
	return render_template("card.html")
'''

@app.route("/upload", methods=['GET','POST'])
def upload():
	global error
	if request.method=='POST':
		target = os.path.join(APP_ROOT, 'file/')
		print(target)

		if not os.path.isdir(target):
			os.mkdir(target)
		try:

			for file in request.files.getlist("file"):
				print(file)
				filename = file.filename
				destination = "/".join([target, filename])
				print(destination)
				contents = file.read()
				value = contents.decode(encoding='UTF-8')
				root = ET.fromstring(value)
				print(root.attrib)
				print(value)

			return render_template("complete.html",data = root.attrib,vis=visible,error='')
		except:
		
			return render_template("upload.html",error=error)
	

	

	return render_template("complete.html",data="",vis=visible,error='')

@app.route("/getfile",methods=["POST"])
def getfile():
	#return "hi"

	if request.method=="POST":
		uid=request.form["uid"]
		name=request.form["name"]
		gender=request.form["gender"]
		yob=request.form["yob"]
		co=request.form["co"]
		loc=request.form["loc"]
		lm=request.form["lm"]
		vtc=request.form["vtc"]
		po=request.form["po"]
		dist=request.form["dist"]
		state=request.form["state"]
		pc=request.form["pc"]
		mobile=request.form["mobile"]
		inc=request.form["inc"]

		print("uid="+uid)

		html = """
		<!DOCTYPE html>
		<html lang="en">
		<body>
			<center>
			<img align="center" src="logo-gov.png" alt="logo-gov" width="72" height="72"/></center>
			<h2 align="center"><b>GOVERNMENT OF GUJARAT</b></h2>
			<br><hr><h2 align="center"><b>AADHAR DETAILS</b></h2><br>
			<table align="center" border="0" width="70%">
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>UID : </b></td>
					<td width="50%" align="right">"""+uid+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Name : </b></td>
					<td width="50%" align="right">"""+name+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Gender : </b></td>
					<td width="50%" align="right">"""+gender+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Year of Birth : </b></td>
					<td width="50%" align="right">"""+yob+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Care of : </b></td>
					<td width="50%" align="right">"""+co+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>House : </b></td>
					<td width="50%" align="right">"""+lm+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Landmark : </b></td>
					<td width="50%" align="right">"""+loc+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Village/Town/City : </b></td>
					<td width="50%" align="right">"""+vtc+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Post Office Name : </b></td>
					<td width="50%" align="right">"""+po+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>District : </b></td>
					<td width="50%" align="right">"""+dist+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>State : </b></td>
					<td width="50%" align="right">"""+state+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Pincode : </b></td>
					<td width="50%" align="right">"""+pc+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Income : </b></td>
					<td width="50%" align="right">"""+inc+"""</td>
				</tr>
				<br>
				<tr>
					<td width="10%"></td>
					<td width="40%"><b>Phone Number : </b></td>
					<td width="50%" align="right">"""+mobile+"""</td>
				</tr>
				<br>
			 </table>
		</body>
	</html>
		"""		
	
		global schemeName
		x,y=check(uid,schemeName)
		print(x,y)
		if(x==True):
			pdf = MyFPDF()
			#First page
			pdf.add_page()
			pdf.write_html(html)
			pdf.output(os.getcwd()+'/'+uid+'.pdf', 'F')
			print(os.listdir(os.getcwd()))
			with open('values.json', "a") as f:
				dump(request.form, f)
				f.write("\n")
			print("mobile=",mobile.lstrip(' '))
			send(number=mobile.lstrip(' '),scheme=schemeName)
			return send_file(os.getcwd()+'/'+uid+'.pdf',attachment_filename=uid+'.pdf',as_attachment=True)
		else :
			#flash("Already enrolled for "+y)
			global error
			global flag
			error="Already enrolled for "+y
			flag=True
			return redirect(url_for('schemeList'))
			#return render_template("complete.html",error="Already enrolled for "+y,data='',vis=visible)
			#return redirect(url_for('upload',data='',error="Already enrolled for "+y,vis=visible))
	return render_template("form.htm")


@app.route('/get_scheme')
def get_scheme():
	c,conn=connection()
	c.execute("select name from SCHEMES")
	results=c.fetchall()
	arr=[]
	for rows in results:
		arr.append(rows[0])

	return jsonify(data=arr)

@app.route('/get_desc')
def get_desc():
	c,conn=connection()
	c.execute("select description,eligibility from SCHEMES where name='"+request.args.get('name')+"'")
	results=c.fetchall()
	x=None
	y=None
	for rows in results:
		x=rows[0]
		y=rows[1]
	global schemeName
	schemeName = request.args.get('name');
	return jsonify(desc=x,elig=y)

@app.route('/logout')
def logout():
	session['logged_in'] = False
	session['user'] = None
	return redirect(url_for('index'))



if __name__=='__main__':
	app.run(debug=True)
