import requests
import os
from bs4 import BeautifulSoup
import re
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

		with open(DATA_PATH+filename, 'w') as f:
			f.write(content)

	def get_html(self, url):
		""" Make GET request and save content to file
			First try with SSL verification (default),
			if error => disable SSL verification
			:param url: string
		"""
		r = requests.get(url)

		#print(f'#####: {r.apparent_encoding}')

		if r.ok:
			return r.text;

	def get_seed(self):
		
		page_links = []
		page_url=self.base_url+str(self.curent_page)
		html=self.get_html(page_url)

		soup = BeautifulSoup(html,'html.parser')
		product= soup.find('div',id="content")
		#print(len(product))
		divs = product.find_all('div', id ="products-container")
		#print(len(divs))
		
		for div in divs:
			date = div.find('div',class_="price")
			print(date)
			a = div.find('a')
			#print(a['href'])
			#page_links.append(a['href'])
			#date = div.span.string
    		
			rx = re.compile(r'(\d+)')
	
			m =rx.search(str(date))
			if m:
    		
				date= int(m.group(1))
				print(date)






		if date <10:
			a = div.find('a')
			page_links.append( urljoin(BASE_URL,a['href']))
				

			if page_links:
				self.seed = [*self.seed,*page_links]
				self.curent_page+=1
				self.get_seed()


		return page_links

	def get_page_data(self, html):
			soup=BeautifulSoup(html,'html.paresr')
			
			product=soup.find('div' , id="product_info" )
			print(product)
			title=product.find('h1').getText(strip=True)
			print(title)
			pat_date=product.find('div',class_="price")
			size_li=product.find('b')
			
			return{
				'title':title,
				'pat_date':pat_date,
				'size_li':size_li
			}
			




			print(html)

		
	def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""

			#self.get_seed(self)
			self.get_seed()
			print(f'Seed contains {len(self.seed)} urls')			
			
			
			
			for url in self.seed:
				page_html=self.get_html(url)
				date=self.get_page_data(page_html)
				
				
			print('finishito')
if __name__ == '__main__':
	base_url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref=1"
	crawler = Crawler()
	crawler.run()