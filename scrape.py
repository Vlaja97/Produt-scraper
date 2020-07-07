import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


### Scrape data
url = 'https://www.emmi.rs/racunari-komponente/racunarske-komponente/graficke-kartice-vga.html'
page = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(page.content, 'html.parser')

name = []
price = []
for card in soup.find_all('div', class_='product-info'):
    name_tmp = card.find('h2', class_='product-name').text
    name.append(name_tmp)
    price_tmp = card.find('span', class_='price').text
    price.append(price_tmp)


### Format data
df = pd.DataFrame(zip(name, price), columns=['Name', 'Price'])
df['Price'] = (df['Price'].str.replace('RSD', '').str.strip())
# Formating price to show more digits
### TODO set prices to float
#df['Price'] = df['Price'].astype(float)
#pd.set_option('display.float_format','{:.3f}'.format)

print(df)

# Create DB
Base = declarative_base()
engine = create_engine('sqlite:///app.db', echo=True)


# Product class for DB
class Product(Base):
    __tablename__ = 'products'

    name = Column(String, primary_key=True)
    price = Column(Float)
    def __repr__(self):
        return f'Product {self.name} - Price {self.price}'
    
    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).all()
    
Base.metadata.create_all(engine)
df.to_sql('products', con=engine, if_exists='replace')


# Create session
Session = sessionmaker(bind=engine)
session = Session()


# Test data
# product = Product(df)
# session.add(product)
# print(product)


# # Query data
# Product.find_by_name(session, 'graphic d')
# Product.find_by_name(session, 'AMD Radeon RX 570 XFX 8GB GDDR5,3xDP/HDMI/D-DVI-D/256bit/RX-570P8DFD6')
# products = session.query(Product).all()
# for product in products:
#     print(product)


# # Save to csv
# df.to_csv('graphic_cards-emmi.csv', index=False, encoding='utf-8')
# print(df)