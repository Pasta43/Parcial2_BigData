import unittest
import app,requests
class TestsUrl(unittest.TestCase):

    def test_urls(self):
        urls=app.generateUrls()
        self.assertEqual(urls!=None, True)
    def test_download(self):
        today=1635146123-86400
        yesterday=today-86400
        url=f'https://query1.finance.yahoo.com/v7/finance/download/AVAL?period1={yesterday}&period2={today}&interval=1d&events=history&includeAdjustedClose=true'
        print(url)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
        r = requests.get(url,headers=headers)
        print(r.text)
        self.assertEqual(r.content!='Forbidden', True)

if __name__ == '__main__':
		unittest.main()