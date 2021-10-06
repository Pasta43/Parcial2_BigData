import json
import boto3
import csv
import ntpath
from bs4 import BeautifulSoup

def handler(event, context):
    bucketName= event['Records'][0]['s3']['bucket']['name']
    fileName=event['Records'][0]['s3']['object']['key']
    fileName=fileName.replace('%3D','=')
    print(bucketName,fileName,flush=True)
    s3 = boto3.resource('s3')
    justFileName=ntpath.basename(fileName)   
    s3.meta.client.download_file(bucketName, fileName, '/tmp/'+justFileName)
    f = open('/tmp/'+justFileName,'r',encoding='utf-8')
    txt=f.read()

    soup = BeautifulSoup(txt,'html.parser')
    articles=soup.find_all('article') #All of these articles, are news

    csvFile = open('/tmp/'+justFileName+'.csv', 'w',encoding='utf-8')
    writer = csv.writer(csvFile,dialect='unix')
    row=['title','section','url']
    writer.writerow(row)
    for article in articles:
        category_anchor=article.find("a",{'class':'category'})
        title_anchor= article.find("a",{'class':'title'})
        if(category_anchor and title_anchor):
            category=category_anchor.getText()
            title=title_anchor.getText()
            url='https://www.eltiempo.com'+title_anchor.get('href')
            row=[title,category,url]
            writer.writerow(row)

    csvFile.close()
    f.close()
    s3.meta.client.upload_file('/tmp/'+justFileName+'.csv', 'resultsnewspaperbucket','newspaper/final/'+ fileName.replace('stage/','')+'.csv')
    return {
        'statusCode': 200,
        'body': 'Logs generated!'
    }
