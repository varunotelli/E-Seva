from flask import Flask,send_file,request,render_template
#from pdf import create
from fpdf import FPDF,HTMLMixin
import os
from json import dump
import xml.etree.ElementTree as ET
class MyFPDF(FPDF, HTMLMixin):
    pass


app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['GET','POST'])
def upload():
	if request.method=='POST':
	    target = os.path.join(APP_ROOT, 'file/')
	    print(target)

	    if not os.path.isdir(target):
	        os.mkdir(target)

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

	    return render_template("complete.html",data = root.attrib)
	return render_template("complete.html",data="")

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
  <form id="input-form" action="/getfile" method="POST" enctype="multipart/form-data">

  <img src="logo-gov.png" alt="logo-gov" width="72" height="72"/>
  <p align="right"><b>Ministry of Social Justice and Empowerment</b></p>

  <br><hr><h3 align="center">Aadhaar Details</h3><br>
    <b>UID</b>&nbsp;&nbsp;&nbsp;&nbsp;"""+uid+"""
    <br><br>
    <b>Name</b> <input type="text" name="name">&nbsp;&nbsp;&nbsp;&nbsp;"""+name+"""
    <br><br>
    <b>Gender</b> <input type="text" name="gender">&nbsp;&nbsp;&nbsp;&nbsp;"""+gender+"""
    <br><br>
    <b>YOB</b> <input type="text" name="yob">&nbsp;&nbsp;&nbsp;&nbsp;"""+yob+"""
    <br><br>
    <b>CO</b> <input type="text" name="co">&nbsp;&nbsp;&nbsp;&nbsp;"""+co+"""
    <br><br>
    <b>LM</b> <input type="text" name="lm">&nbsp;&nbsp;&nbsp;&nbsp;"""+lm+"""
    <br><br>
    <b>LOC</b> <input type="text" name="loc">&nbsp;&nbsp;&nbsp;&nbsp;"""+loc+"""
    <br><br>
    <b>VTC</b> <input type="text" name="vtc">&nbsp;&nbsp;&nbsp;&nbsp;"""+vtc+"""
    <br><br>
    <b>PO</b> <input type="text" name="po">&nbsp;&nbsp;&nbsp;&nbsp;"""+po+"""
    <br><br>
    <b>DIST</b> <input type="text" name="dist">&nbsp;&nbsp;&nbsp;&nbsp;"""+dist+"""
    <br><br>
    <b>State</b> <input type="text" name="state">&nbsp;&nbsp;&nbsp;&nbsp;"""+state+"""
    <br><br>
    <b>PC</b> <input type="text" name="pc">&nbsp;&nbsp;&nbsp;&nbsp;"""+pc+"""
    <br><br>
    <b>Income</b> <input type="text" name="inc">&nbsp;&nbsp;&nbsp;&nbsp;"""+mobile+"""
    <br><br>
    <b>Mobile</b> <input type="text" name="mobile">&nbsp;&nbsp;&nbsp;&nbsp;"""+inc+"""
    <br><br>     
  </form> 
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
