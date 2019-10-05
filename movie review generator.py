import bs4
import urllib.request as url

userInput = input("Enter movie name : ")
userInput1 = userInput.split()
movieName = '+'.join(userInput1)
http = url.urlopen("https://www.imdb.com/find?ref_=nv_sr_fn&q="+movieName)

source = bs4.BeautifulSoup(http,'lxml')
td = source.find('td',class_='result_text')
a = td.find('a')
# print(a['href'])
href = a['href']
newUrl = "https://www.imdb.com" + href
http = url.urlopen(newUrl)
source = bs4.BeautifulSoup(http,'lxml')
div = source.find('div', class_='title_wrapper')
# print(div.text)
data = div.text.replace("\n","")
# print(data.split())
data = data.split()
data = ' '.join(data)
print(data)
summary = source.find('div', class_='summary_text')
print(summary.text.strip())

links = source.findAll('a',class_='quicklink')
#print(links)
url2 = "https://www.imdb.com" + links[2]['href']

http = url.urlopen(url2)
source = bs4.BeautifulSoup(http)
titles = source.findAll('a', class_='title')
for item in titles:
    print(item.text)
