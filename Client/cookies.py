'''
Takes care of logging into coursera and setting cookies
'''
import subprocess
import re
from exceptions import *

AUTH_URL="https://accounts.coursera.org/api/v1/login"

def login(username, password,classname):
	'''
	Logs into coursera 
	'''
	classurl=create_class_url(classname)
	data = "email="+username+"&password="+password
	p = subprocess.Popen(["curl", "--dump-header","temp.txt",classurl],stdout=subprocess.PIPE)
	p.wait()

	headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", open('temp.txt').read()))
	cookie = dict(re.findall(r"(?P<name>.*?)=(?P<value>.*?);? ?;", headers['Set-Cookie']));
	csrftoken=cookie['csrf_token']
	if not csrftoken:
		'''
		Authentication failed
		'''
		raise AuthenticationFailure('Unable to fetch csrftoken')
	else:
		p=subprocess.Popen(["curl","--dump-header","login_header.txt","--cookie","temp.txt", "-H","Cookie: csrftoken=" + csrftoken,"-H","Referer: https://accounts.coursera.org/signin","-H", "X-CSRFToken: "+csrftoken,"-d",data,AUTH_URL], stdout=subprocess.PIPE)
		p.wait()

		login_header = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", open('login_header.txt').read()))
		login_cookies = dict(re.findall(r"(?P<name>.*?)=(?P<value>.*?);? ?;", login_header['Set-Cookie']));
		return True

def create_class_url(classname):
	'''
	Create class url from classname
	'''
	return "https://class.coursera.org/"+classname