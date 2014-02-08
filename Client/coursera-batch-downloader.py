import cookies
import argparse
import json
from pprint import pprint
from downloader import *


filename=''


def __main__():
	global filename
	parser = argparse.ArgumentParser('Coursera Downloader');
	parser.add_argument("-f", "--file",help="Path to the json file", required=True);
	parser.add_argument("-e","--email",help="Email ID to login",required=True);
	parser.add_argument("-p","--pass",help="Coursera password",required=True);
	args = vars(parser.parse_args());
	filename = args['file']
	data = parse_input()

	if not data:
		print 'Raise Exception'
		return

	if cookies.login(args['email'], args['pass'],data['cname']):
		download(data)

def parse_input():
		json_data = open(filename)
		if not json_data:
			return False
		try:
			return json.load(json_data);
		except Exception, e:
			raise e
		

__main__()

