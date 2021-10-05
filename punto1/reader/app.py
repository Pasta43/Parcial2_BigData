import requests
import boto3
import time

def handler(event,context):
	localtime=time.localtime()
	print("Getting html content...")
	r = requests.get('https://www.eltiempo.com/')
	print("Creating temporaly file...")	
	f = open("/tmp/newspaper.html","w")
	print("Saving file")
	f.write(r.text)
	f.close()
	s3 = boto3.resource('s3')
	print("Loading in s3...")
	data={
		'file':'/tmp/newspaper.html',
		'bucket':'newsdata202110',
		'path':'newspaper/stage/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/newspaper=El_tiempo/'+str(localtime.tm_hour)+str(localtime.tm_min)+str(localtime.tm_sec)+'page.html'
	}
	s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])
	print("file uploaded!")

	return {
			"status_code":200
		}
