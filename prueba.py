import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')
soup = BeautifulSoup(page.content, 'html.parser')


for i, a in enumerate(soup.select('h3.yt-lockup-title a[title]')[:10], 1):
    print('{: <4}{}'.format(str(i)+'.', a['title']))