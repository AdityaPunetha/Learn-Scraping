from bs4 import BeautifulSoup
import lxml

with open('DJIA.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    td_tags = soup.find_all('td')
    print(td_tags[3].text, td_tags[4].text, td_tags[5].text)
    # for td in td_tags:
    #     print(td.text)
