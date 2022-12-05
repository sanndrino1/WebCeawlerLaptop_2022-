import requests
import os
from bs4 import BeautifulSoup
import re
BASE_URL = "https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1"



try:
	# when run 'crawler.py':
	  from constant import DATA_PATH
except:
	# when run 'app.py'
	  from libs.constant import DATA_PATH

class Crawler():
      def __init__(self, base_url):
        self.seed=[base_url]
        pass
        

  

      def write_to_file(self,filename, content):
        """ Write string to given filename
          :param filename: string
         :param content: sring
        """
  

        with open(DATA_PATH+filename,'w', encoding='utf-8') as f:
          f.write(content)

    
        
      def get_html(self,url):
        """ Make GET request and save content to file
        First try with SSL verification (default),
        if error => disable SSL verification

        :param url: string
        """
        r=requests.get(url)
        if r.ok:
      
          return r.text;

      def scrape_links(self, html):
        soup = BeautifulSoup(html,'html.parser')
        date = list()
       


        prices_div=soup.find(class_='price')

        price_divs = prices_div.find_all('div', class_='price')
        for div in price_divs:
          price_num = div.span.string
          print(price_num)
      def run(self):
        for url in self.seed:
          html= self.get_html(url)
          #self.write_to_file('www.jarcomputers.html.html',html)
          links = self.scrape_links(html)
          main_url = 'https://jarcomputers.com/'
          urls = [ main_url + el  for el in links]
          print(urls)


          
      
		
      

if __name__ == '__main__':
  
  
  crawler = Crawler("https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1")
  crawler.run()

