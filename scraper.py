import requests
from bs4 import BeautifulSoup
import re

from csv_handler import write_data_to_csv
from db_handler import create_db, insert_data


url = 'https://www.theverge.com'
website_data = requests.get(url)
website_data = website_data.text

def find_links(website_html):
    main_link_regex = r'(https://www.theverge.com)'
    date_regex = r'(\d{4}/\d(\d)?/\d(\d)?/)?'
    id_regex = r'\d+/'
    article_regex = r'([a-z]+)(-[a-z]+)+'
    r_compiled = re.compile(main_link_regex + '?' + r'/' + date_regex + id_regex + article_regex)
    proper_link = re.compile(main_link_regex + r'/' + date_regex + id_regex + article_regex)
    starts_with = re.compile('^' + main_link_regex)

    links = []
    for link_matched in r_compiled.finditer(website_html):
        link = link_matched.group()
        if not starts_with.search(link):
            link = url + link
            links.append(link)

    return links



def find_article_details(article_html):
    soup = BeautifulSoup(article_html, 'html.parser')
    title = soup.find('h1')
    title = title.string

    author = soup.find('span', class_='duet--article-byline-and italic')
    author = author.parent.find('a').string
    
    date = soup.find('time')['datetime'][:10]
    date = date.replace('-', '/')
    return [title, author, date]

if __name__ == '__main__':
    create_db()

    links = find_links(website_data)
    links = set(links)
    article_infos = set()
    for link in links:
        article_data = requests.get(link)
        if article_data:
            try:
                details = [link]
                details += *find_article_details(article_data.text),
     
                article_infos.add(tuple(details))
                
            
            except AttributeError:
                pass
    
    article_infos = list(article_infos)
    write_data_to_csv(article_infos)
    conn = insert_data(article_infos)
    conn.close()
