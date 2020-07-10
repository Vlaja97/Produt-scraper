# Produt-scraper
Scraping products of sites using BeatifoulSoup, formating data with pandas and storing it in DB which Flask app uses to render templates and show data.



# Frameworks and library used
  - BeautifulSoup
  - Flask
  - SQLAlchemy
  - Pandas

# How to use
  - First we need to start virtual environment using `source env/bin/activate`
  - `scrape.py` is file that does the scraping, format the data, and populates the DB. We can do that by typing `python scrape.py`
  - That data is stored in `app.db` and we can view data by starting flask app: `flask run`


# Disclaimer
*This project is for purpose of learning only*

*This project is for personal and not for comercial use*
