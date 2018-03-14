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

@app.route("/upload", methods=['POST'])
def upload():
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
		html="""
<body>
	<form id="input-form" action="/getfile" method="POST" enctype="multipart/form-data">UID <input type="text" name="uid">&nbsp;&nbsp;&nbsp;&nbsp;"""+uid+"""<br><br>
	    Name <input type="text" name="name">&nbsp;&nbsp;&nbsp;&nbsp;"""+name+"""<br><br>
	    Gender <input type="text" name="gender">&nbsp;&nbsp;&nbsp;&nbsp;"""+gender+"""<br><br>
	    YOB <input type="text" name="yob">&nbsp;&nbsp;&nbsp;&nbsp;"""+yob+"""<br><br>
	    CO <input type="text" name="co">&nbsp;&nbsp;&nbsp;&nbsp;"""+co+"""<br><br>
	    LM <input type="text" name="lm">&nbsp;&nbsp;&nbsp;&nbsp;"""+loc+"""<br><br>
	    LOC <input type="text" name="loc">&nbsp;&nbsp;&nbsp;&nbsp;"""+lm+"""<br><br>
	    VTC <input type="text" name="vtc">&nbsp;&nbsp;&nbsp;&nbsp;"""+vtc+"""<br><br>
	    PO <input type="text" name="po">&nbsp;&nbsp;&nbsp;&nbsp;"""+po+"""<br><br>
	    DIST <input type="text" name="dist">&nbsp;&nbsp;&nbsp;&nbsp;"""+dist+"""<br><br>
	    State <input type="text" name="state">&nbsp;&nbsp;&nbsp;&nbsp;"""+state+"""<br><br>
	    PC <input type="text" name="pc">&nbsp;&nbsp;&nbsp;&nbsp;"""+pc+"""<br><br>
	    Income <input type="text" name="inc">&nbsp;&nbsp;&nbsp;&nbsp;"""+mobile+"""<br><br>
	    Mobile <input type="text" name="mobile">&nbsp;&nbsp;&nbsp;&nbsp;"""+inc+"""<br><br>

	    
	</form>
			
</body>

"""
	
		pdf = MyFPDF()
		#First page
		pdf.add_page()
		pdf.write_html(html)
		pdf.output(os.getcwd()+'/'+uid+'.pdf', 'F')
		print(os.listdir(os.getcwd()))
		with open('values.json', "a") as f:
			dump(request.form, f)
		return send_file(os.getcwd()+'/'+uid+'.pdf',attachment_filename=uid+'.pdf',as_attachment=True)
	return render_template("form.htm")


if __name__=='__main__':
	app.run(debug=True)