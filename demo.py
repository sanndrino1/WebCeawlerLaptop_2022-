 
from bs4 import BeautifulSoup
import re
 


html = '''
<body>
	<h1>Page Title</h1>
	<div class="price">
        <div class="price">
        <span class="price-num">1749</span>
        <a href="/title/Laptopi_cat_2.html?ref=c_1" class="dark white">Laptopi:</a>
        
    </div>
    <div class="price">
        <div class="price">
        <span class="price-num">1 899 </span>
        <a href ="/title/Laptopi_cat_2.html?ref=c_1" class="dark light">Laptopi:</a>
        </div>
    </div>
    </body>
    ''';


soup = BeautifulSoup(html,'html.parser')
data = list ()
prices_div=soup.find(class_='price')



price_divs = prices_div.find_all('div', class_='price')
for div in price_divs:
    price = div.span.string
    print(price)

    rx = re.compile(r'(\d+)')
    m =rx.search(price)
    if m:
        price = int(m.group(1))
        #print(price)

    if price<3000:
        a = div.a
        print(a.attrs)
        data.append(a.attrs)
      
        
    
    

