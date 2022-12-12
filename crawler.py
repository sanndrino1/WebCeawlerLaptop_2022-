import requests
import os
from bs4 import BeautifulSoup 
import re

BASE_URL = "https://www.jarcomputers.com/"



try:
	# when run 'crawler.py':
		from constant import DATA_PATH
except:
	# when run 'app.py'
		from libs.constant import DATA_PATH

class Crawler():
		def __init__(self, base_url):
				self.curent_page=1;
				self.url="https://www.jarcomputers.com/Laptopi_cat_2.html?ref="
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
				r=requests.get(url)
				if r.ok:
			
					return r.text
		#def bucks_page(self,html):
			#soup = BeautifulSoup(html,'html.parser')
			#data=list()
			#links_lap_top=soup.find(id="products_container")
			
			
			
			#link_laps=links_lap_top.find_all(class_="p1")
			#for div in link_laps:
				#a=div.a
				#print(a)

				
				#print(a)

				
		
		
		def mode_price_links(self,html):
			soup = BeautifulSoup(html,'html.parser')
			
			
			products = soup.find(id="products-container" )
			print(products.string)
			divs = products.find_all('div', class_="s2")
			#print(len(divs))
				
			for div in divs:
				price=div.find('div',class_="brand-name")
				print(price.text)
		
			


		def get_seed(self):
			page_links=[]
			
			page_url=self.url=self.curent_page
			html=self.get_html(page_url)
			soup = BeautifulSoup(html,'html.parser')
		
			brand=soup.find(id="products-container" )
			#print(brand.string)
			divs=brand.find_all('div', class_="row-price") 
			print(len(divs))
			for div in divs:
				model=div.find('div',  lass_="price"  )
				
				
				a=div.find('a')
				
				page_links.append(urljoin(BASE_URL, a['href']))
			if page_links:

				self.seed=[*self.seed,*page_links]
				self.curent_page+=1
				self.get_seed()


			
					
				
		def ekran_page(self,html):
			soup = BeautifulSoup(html,'html.parser')
			date=list()
			stil_products=soup.find( id="products-container" )
			print(stil_products.string)
			
			stil_product=stil_products.find_all('div',class_="s2")
			for span in stil_product:
				ekran=span.find('span', class_="short_title fn" )
				rx = re.compile(r'[0-9][0-9][0-9]')

				match = re.search(str(ekran))
				print( match)
				
				#print(ekran.text,'uuuuuuuuuuuuuuukkkkkkkkkkkk')
				
			
				
					
			




			
		
			
				
			
		def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""

			
			self.get_seed()
			
					
					
			print('finishito')

if __name__ == '__main__':
	
	crawler = Crawler( "https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1")
	crawler.run()