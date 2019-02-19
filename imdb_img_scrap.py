from bs4 import BeautifulSoup
import requests


url='https://www.imdb.com/gallery/rg1859820288?ref_=nv_ph_ls'
page=requests.get(url)

soup=BeautifulSoup(page.content,'lxml')

lis=soup.find('div',{'class':'media_index_thumb_list'})

title=list()
src=list()

for img_src in lis.find_all('img'):
    src.append(img_src['src'])


for title_All in lis.find_all('a'):
    title.append(title_All['title'])

i=0
while  i<=len(title):
    file=open(title[i],'wb')
    file.write(requests.get(src[i]).content)
    file.close()
