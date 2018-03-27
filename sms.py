import urllib.request, urllib.error, urllib.parse
import http.cookiejar
from getpass import getpass
import sys
def send(number,scheme):
	username="8870173154"
	passwd="kumaresh"
	message="You have successfully been enrolled for "+scheme

	''' 
	username = input("Enter Username: ")
	passwd = getpass()
	message = input("Enter Message: ")
	number = input("Enter Mobile number:")
	'''
	message = "+".join(message.split(' '))

	#Logging into the SMS Site
	url = 'http://site24.way2sms.com/Login1.action?'
	data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
	 
	#For Cookies:
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	 
	# Adding Header detail:
	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
	 
	try:
	    usock = opener.open(url, data.encode('utf-8'))
	except IOError:
	    print("Error while logging in.")
	    #sys.exit(1)
	 
	 
	jession_id = str(cj).split('~')[1].split(' ')[0]
	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
	opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	 
	try:
	    sms_sent_page = opener.open(send_sms_url,send_sms_data.encode('utf-8'))
	except IOError:
	    print("Error while sending message")
	    
	#sys.exit(1)
	print("SMS has been sent.")
	return True


#send("8870173154","piyu")