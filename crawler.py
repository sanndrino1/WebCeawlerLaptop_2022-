import requests
import os

import re
from bs4 import BeautifulSoup 
from urllib.parse import urlparse

from urllib.parse import urljoin


BASE_URL=" https://www.jarcomputers.com"
#"https://zora.bg/"
		#"https://www.jarcomputers.com"






try:
	# when run 'crawler.py':
		from constant import DATA_PATH
except:
	# when run 'app.py'
		from libs.constant import DATA_PATH



class Crawler():
	def __init__(self):
			self.curent_page=1
			self.base_url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref="
			#"https://www.technomarket.bg/produkti/laptopi?page="
			#"https://zora.bg/category/laptopi?page="
			#"https://www.jarcomputers.com/Laptopi_cat_2.html?ref=1"
			self.seed=[]
			

	def write_to_file(self,filename, content):
		""" Write string to given filename
				:param filename: string
				:param content: sring
		"""

		with open(DATA_PATH+filename, 'w') as f:
			f.write(content)

	def get_html(self, url):
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
			r.encoding="utf-8"
		else:
			print('The server did not return success response. Bye...')
			exit


		#print(f'#####: {r.apparent_encoding}')

		if r.ok:
			return r.text;
	def get_seed(self):
		
		page_links = []
		page_url=self.base_url+str(self.curent_page)
		html=self.get_html(page_url)

		soup = BeautifulSoup(html,'html.parser')
		product= soup.find ('div',id="products-container" )
		print(len(product))

		divs = product.find_all('a',class_="brand-name")


		print(len(divs))
		for div in product:
			date = div.find('li', class_="list_warranty")
			#date= div.string
			rx = re.compile(r'(\d+)')
			m =rx.search(str(date))
			if m:
				date= int(m.group(1))
				print(date)
				
			#if date < 24:

				#print(date)
			
   

	
			
		
			a = div.find('a')
			page_links.append( urljoin(BASE_URL,a['href']))
			print(page_links)


		if page_links:
				self.seed = [*self.seed,*page_links]
				self.curent_page+=1
				self.get_seed()
               


				return page_links

	def get_page(self,html):
		soup=BeautifulSoup(html,'html.parser')

		bonus=soup.find('ol',class_="product_list")
		price=soup.find('div',class_="row-price")
		
		model=soup.find('span',class_="long_title description")
		marka=soup.find('div',class_="brand-name").getText()
		return{
			'price':price,
			'model':model,
			'marka':marka
			
		}
	
	


	def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""

			
			self.get_seed()
			print(f'Seed contains {len(self.seed)} urls')			
			
			
			for url in [1]:
				page_html=self.get_html("https://www.jarcomputers.com/Laptopi_cat_2.html?ref=")
				
				get_data_page=self.get_page(page_html)
				print(get_data_page)
				
			
           
				
				print('finishito')
#__name__ == '__main__'
##base_url="https://www.technomarket.bg/produkti/laptopi?page=1"
	
 	#"https://www.jarcomputers.com/Laptopi_cat_2.html?ref=1"
#crawler = Crawler()
#crawler.run()