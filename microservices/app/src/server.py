from flask import Flask,send_file,request,render_template
#from pdf import create
from fpdf import FPDF,HTMLMixin
import os
class MyFPDF(FPDF, HTMLMixin):
    pass


app=Flask(__name__)

@app.route("/")
def index():
	return "hello world"

@app.route("/getfile",methods=["GET","POST"])
def getfile():
	#return "hi"

	if request.method=="POST":
		uid=request.form["uid"]
		print("uid="+uid)
		html="""
<body>
	<form id="form" method="POST" action="">UID <input type="text" id="uid" class="fele">&nbsp;&nbsp;"""+uid+"""<br><br>
		Name <input type="text" id="name" class="fele"><br><br>
		Gender <input type="text" id="gender" class="fele"><br><br>
		YOB <input type="text" id="yob" class="fele"><br><br>
		CO <input type="text" id="co" class="fele"><br><br>
		House <input type="text" id="house" class="fele"><br><br>
		Street <input type="text" id="street" class="fele"><br><br>
		LM <input type="text" id="lm" class="fele"><br><br>
		VTC <input type="text" id="vtc" class="fele"><br><br>
		PO <input type="text" id="po" class="fele"><br><br>
		Dist <input type="text" id="dist" class="fele"><br><br>
		Subdist <input type="text" id="subdist" class="fele"><br><br>
		State <input type="text" id="state" class="fele"><br><br>
		PC <input type="text" id="pc" class="fele"><br><br>
		DOB <input type="text" id="dob" class="fele"><br><br>
		Mobile Number <input type="text" id="mobile" class="fele"><br><br>
		
	</form>
			
</body>

"""
	
		pdf = MyFPDF()
		#First page
		pdf.add_page()
		pdf.write_html(html)
		pdf.output(os.getcwd()+'/'+uid+'.pdf', 'F')
		print(os.listdir(os.getcwd()))
		return send_file(os.getcwd()+'/'+uid+'.pdf',attachment_filename=uid+'.pdf',as_attachment=True)
	return render_template("form.htm")


if __name__=='__main__':
	app.run(debug=True)