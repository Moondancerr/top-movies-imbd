import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make request to website
url = "https://www.imdb.com/chart/top"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract data from website
titles = soup.find_all('td', class_='titleColumn')
ratings = soup.find_all('td', class_='ratingColumn imdbRating')

# Create dataframe to store scraped data
data = {'Title': [], 'Rating': [], 'Year': []}
for i in range(len(titles)):
    title = titles[i].find('a').get_text()
    rating = ratings[i].find('strong').get_text()
    year = int(titles[i].find('span').get_text()[1:5])
    data['Title'].append(title)
    data['Rating'].append(float(rating))
    data['Year'].append(year)

df = pd.DataFrame(data)

# Write dataframe to excel file
df.to_excel("imdb_data.xlsx")
