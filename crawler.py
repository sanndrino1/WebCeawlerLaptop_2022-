import requests
import os
from bs4 import BeautifulSoup 
import re
from urllib.parse import urljoin

import urllib3


BASE_URL="https://www.jarcomputers.com"




try:
	# when run 'crawler.py':
		from constant import DATA_PATH
except:
	# when run 'app.py'
		from libs.constant import DATA_PATH

class Crawler():
		def __init__(self,base_url):
			self.curent_page=1
			self.base_url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref=#"
			self.seed=[]
			
			self.base_url= base_url;
			self.seed=[]
				
				
				

	

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
				
				

				r = requests.get(url)
				if r.ok:
			
						return r.text
				else:

					print('The server did not return success response. Bye...')
					exit()
		

				
		
		
		
		def get_seed(self):
			
			page_links = []
			page_url=self.base_url+str(self.curent_page)
			html=self.get_html(page_url)
			soup=BeautifulSoup(html,'html.parser')
			contact=soup.find(id="products-container")
			print(len(contact))
			divs=contact.find_all('div',class_="s3")
			print(len(divs))
			for div in divs:
				date=div.find('div',class_="row-price")

				
				print(date)
				
				
					
			#if date<3000:
				a=div.find('a')
				
				
				
			
				page_links.append( urljoin(BASE_URL,a['href']))
			if page_links:
				self.seed =[*self.seed *page_links]
				self.curent_page+=1#
				self.get_seed()
			
		def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""

			self.get_seed()
			
			
			
			for url in [1]:
				page_html=self.get_html("https://www.jarcomputers.com/Laptopi_cat_2.html?ref=")
				#date=self.get_rule_page(page_html)
				
				
			print('finishito')
#if __name__ == '__main__':
	#base_url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref="
	#crawler = Crawler(base_url)
	#crawler.run()