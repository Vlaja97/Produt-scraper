from flask import Flask, render_template
from config import Config

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

from scrape import Product


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list_products')
def list_products():
    engine = create_engine('sqlite:///app.db', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    products = session.query(Product).all()
    for product in products:
        print(product)
    return render_template('list.html', products = products )



if __name__ == '__main__':
    app.run(debug=True)
    app.config.from_object(Config)
    db = SQLAlchemy(app)