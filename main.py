from bs4 import BeautifulSoup
import lxml
import requests

html_text = requests.get('https://dowfutures.org/').text
# print(html_text)
# with open('DJIA.html', 'r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     td_tags = soup.find_all('td', class_="main-change")
#     # print(td_tags[3].text, td_tags[4].text, td_tags[5].text)
#     for td in td_tags:
#         print(td)

soup = BeautifulSoup(html_text, 'lxml')
td_tags = soup.find_all('td', class_="main-change")
# print(td_tags[3].text, td_tags[4].text, td_tags[5].text)
a = [i.text.strip() for i in td_tags]
print(a)
for td in td_tags:
    print(td.text)
