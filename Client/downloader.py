'''
Downloads using curl
'''
import subprocess
import createdir
import os

def download(data):
	'''
	Downloads the videos and automatically saves them in respective folders 
	'''
	cname = data['cname']
	for week in data['data']:
		title = week['title']
		title = title.replace(":","-")
		createdir.create_dir(title)
		for link in week['links']:
			vtitle = link['title']
			vtitle=vtitle.replace(":","-")
			vlink = link['link']
			subprocess.Popen(['curl','--location','--cookie','login_header.txt', vlink], stdout=open(get_video_path(title,vtitle), "w"))


def get_video_path(week, vtitle):
	return week+"/"+vtitle+'.mp4'