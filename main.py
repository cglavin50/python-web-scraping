# imports
import pandas as pd # allows us to read HTML tables and easily get the information from corresponding 'frames'
import requests # handles HTTPS requests
from bs4 import BeautifulSoup # handles parsing HTML
from datetime import date

# get_page function: takes in url string and 
def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print("Status code:", response.status_code)
        raise Exception("Failed to load page {}".format(url))
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc

# flow of control: get BeautifulSoup document, extract headlines + print, and store in csv
url = "https://finance.yahoo.com/news"
doc = get_page(url)
a_tags = doc.find_all('a', {'class': "js-content-viewer"}) # <a> = hyperlinks
print(len(a_tags), "Headlines found") # print how many hyperlinks there are, aka news articles from this page
news_list = []
# print top 10 headlines
for i in range(0, len(a_tags)):
    news = a_tags[i].text
    news_list.append(news)
    print(news)

news_df = pd.DataFrame(news_list)
today = date.today()
filename = 'YahooHeadlines' + str(today) + '.zip'
compression_opts = dict(method='zip', archive_name='headlines.csv')
news_df.to_csv(filename, index=False, compression=compression_opts)

print("Headlines saved to", filename)
# note for future self: alt shift a is block comment for python

