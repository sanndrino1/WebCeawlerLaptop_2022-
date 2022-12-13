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
		def __init__(self):
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
				

				#print(f'Can not get url: {url}: {str(e)}!')
				exit(-1)

				

				r = requests.get(url,verify=False)
				if r.ok:
			
						return r.text
				else:

					print('The server did not return success response. Bye...')
					exit
		

				
		
		
		
		def get_seed(self):
			
		
			page_links=[]
			
			page_url=self.url=str(self.curent_page)
			html=self.get_html(page_url)
			soup = BeautifulSoup(html,'html.parser')
		
			products=soup.find('div',id="central_main")
			
		#id="products-container" )
			#print(brand.string)
			divs=products.find_all('div', id="products_container") 
			print(len(divs))
			for div in divs:
				price=div.find( id="product_list" )
				
			
				a=div.find('a')
				
				page_links.append(urljoin(BASE_URL, a['href']))
			if page_links:

				self.seed=[*self.seed,*page_links]
				self.curent_page+=1
				self.get_seed()
		def get_rule_page(self,html):
			soup = BeautifulSoup(html,'html.parser')

			product_name=soup.find('div',id="product_name")
			title=product_name.find('h1').getText(strip=True)
			rule_page=product_name.find('span', class_="short_title fn")
			price=product_name.find('div',class_="price">1348 )

			return {
				'title': title,
				'rule_page': rule_page,
				'price':price

			}
			


			
					
				
		
				#print(ekran.text,'uuuuuuuuuuuuuuukkkkkkkkkkkk'
			
				
			
		def run(self):
			""" run the crawler for each url in seed
						Use multithreading for each GET request

			"""

			self.get_seed()
			print(self.seed)
			
			
			for url in [1]:
				page_html=self.get_html("https://www.jarcomputers.com/Laptopi_cat_2.html?ref=1")
				date=self.get_rule_page(page_html)
				print(date)
					
			print('finishito')
if __name__ == '__main__':
	
	crawler = Crawler()
	crawler.run()