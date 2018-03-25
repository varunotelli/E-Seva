from flask import Flask,send_file,request,render_template,redirect,url_for,session,flash
#from pdf import create
from fpdf import FPDF,HTMLMixin
import os
from json import dump
import xml.etree.ElementTree as ET
visible="readonly"
class MyFPDF(FPDF, HTMLMixin):
	pass


app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


@app.route("/", methods=["GET","POST"])
def index():
	if not session.get('logged_in'):
		if request.method == 'POST':
			if request.form['password'] == 'password' and request.form['username'] == 'admin':
				session['logged_in'] = True
				return redirect(url_for('card'))
			else:
				flash('Wrong password!')
		return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		if request.form['password'] == 'password' and request.form['username'] == 'admin':
			session['logged_in'] = True
			return redirect(url_for('card'))
		else:
			flash('Wrong password!')
	return render_template("login.html")

@app.route("/card",methods=["GET","POST"])
def card():
	if request.method=="POST":
		if request.form["id-type"]=="aadhar-card":
			return render_template("upload.html")
		else:
			visible=""
			return render_template("complete.html",data="",vis=visible)
	return render_template("card.html")

@app.route("/upload", methods=['GET','POST'])
def upload():
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

			return render_template("complete.html",data = root.attrib,vis=visible)
		except:
			return render_template("upload.html")
	return render_template("complete.html",data="",vis=visible)

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
			<h2 align="center"><b>MINISTRY OF SOCIAL JUSTICE AND EMPOWERMENT</b></h2>
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
	
		pdf = MyFPDF()
		#First page
		pdf.add_page()
		pdf.write_html(html)
		pdf.output(os.getcwd()+'/'+uid+'.pdf', 'F')
		print(os.listdir(os.getcwd()))
		with open('values.json', "a") as f:
			dump(request.form, f)
			f.write("\n")
		return send_file(os.getcwd()+'/'+uid+'.pdf',attachment_filename=uid+'.pdf',as_attachment=True)
	return render_template("form.htm")


if __name__=='__main__':
	app.run(debug=True)
