import requests
import os
from bs4 import BeautifulSoup 
import re



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
	

				#with open(DATA_PATH+filename,'w', encoding='utf-8') as f:
					#f.write(content)

		
				
		def get_html(self,url):
				""" Make GET request and save content to file
				First try with SSL verification (default),
				if error => disable SSL verification

				:param url: string
				"""
				r=requests.get(url)
				if r.ok:
			
					return r.text;
		
		
		def scrape_links(self,html):
			soup = BeautifulSoup(html,'html.parser')
				
				 
			product=soup.find (id="products-container")
			divs=product.find_all('div',class_="s1" )

			#print(len(divs))
			for div in divs:
				price=div.find('div',class_="price")
				#print(price)
				a=div.find('a')
				print(a['href'])
				
			for div in divs:
				model=div.find('div',class_="disc" )
				print(model)
				
		def page_links(self,url):
			print(url)
				

		def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""
			for url in self.seed:
					self.get_html(url)
					html=self.get_html(url)
					self.write_to_file('jarcomputers.com.html',html)
					links=self.scrape_links(html)
					main_url="https://www.jarcomputers.com/"
					urls = [ main_url+ el  for el in links]
					print(urls)

					print('finishito')

#if __name__ == '__main__':
	
	#crawler = Crawler( "https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1")
	#crawler.run()