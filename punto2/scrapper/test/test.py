import csv
from bs4 import BeautifulSoup
import unittest

def srappingElTiempo():
	f = open('16758page.html',"r",encoding='utf-8')
	txt=f.read()
	
	soup = BeautifulSoup(txt,'html.parser')
	articles=soup.find_all('article') #All of these articles, are news

	csvFile = open('results/results.csv', 'w',encoding='utf-8')
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
	return True

def srappingElEspectador():
	f = open('05932page.html',"r",encoding='utf-8')
	txt=f.read()
	soup = BeautifulSoup(txt,'html.parser')
	articles=soup.findAll('div',{'class':'Card-Container'}) #All of these articles, are news
	csvFile = open('results/results2.csv', 'w',encoding='utf-8')
	writer = csv.writer(csvFile,dialect='unix')
	row=['title','section','url']
	writer.writerow(row)
	for article in articles:
		category_div=article.find("h4",{'class':'Card-Section'})
		title_div= article.find("h2",{'class':'Card-Title'})
		if(category_div and title_div):
			category_anchor = category_div.find("a")
			category=category_anchor.getText()
			title_anchor = title_div.find("a")
			title=title_anchor.getText()
			url='https://www.elespectador.com'+title_anchor.get('href')
			row=[title,category,url]
			writer.writerow(row)

	csvFile.close()
	f.close()
	return True
class TestScrapperElTiempo(unittest.TestCase):

	def test_elTiempo(self):
			self.assertEqual(srappingElTiempo(), True)
	def test_elEspectador(self):
			self.assertEqual(srappingElEspectador(), True)


if __name__ == '__main__':
		unittest.main()

