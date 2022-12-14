
import os
import re
import requests
import datetime

from bs4 import BeautifulSoup
from urllib.parse import urljoin



BASE_URL="https://www.jarcomputers.com"




try:
	# when run 'crawler.py':
		from constant import DATA_PATH
except:
	# when run 'app.py'
		from libs.constant import DATA_PATH

class Crawler():
		def __init__(self):
			self.curent_page=1
			self.base_url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref=1"
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
				try:
					r = requests.get(url)
				except requests.RequestException:
			# try with SSL verification disabled.
			# this is just a dirty workaraound
			# check https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f
					r = requests.get(url,verify=False)
				except Exception as e:
					print(f'Can not get url: {url}: {str(e)}!')
					exit(-1)

		# set content encoding explicitely
				r.encoding="utf-8"
				
				

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

				
				print(str(date))
				

				rx = re.compile(r'(\d+)')
				m =rx.search(str(date))

				if m:
					date = int(m.group(1))
					print(date)
				
					
			if date <2500:
				a=div.find('a')
				
				
		
				page_links.append( urljoin(BASE_URL,a['href']))


			if page_links:
				self.seed =[*self.seed *page_links]
				self.curent_page+=1
				self.get_seed()
		def page_data(self,html):
			soup=BeautifulSoup(html,'html.paresr')
			product=soup.find('divi' ,id="content" )
			title=product.find('h1').getText(strip=True)
			pat_date=product.find('div',class_="price")
			size_li=product.find('b')
			
			return{
				'title':title,
				'pat_date':pat_date,
				'size_li':size_li
			}
			
				

			
			
		def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""

			#self.get_seed(self)
			self.get_seed()
			print(f'Seed contains {len(self.seed)} urls')			
			
			
			
			for url in self.seed:
				page_html=self.get_html(url)
				date=self.page_data(page_html)
				
				
			print('finishito')
if __name__ == '__main__':
	base_url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref="
	crawler = Crawler()
	crawler.run()