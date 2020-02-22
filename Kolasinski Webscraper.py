#Jakub Kolasinski
#FE595
#Webscraper Assignment

import requests
from bs4 import BeautifulSoup


#create original list
scrapelist=[]

def scrape(k):
    if(k>0):
        result = k+scrape(k-1)
        url = 'http://18.207.92.139:8000/random_company'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')

        #add all li elements to list
        for tag in soup.find_all("li"):
            scrapelist.append(tag.text)
    else:
        result=0
    return result


#call function N times
scrape(50)

#list of elements we want to remove from the list
discard = ['CEO:', 'CTO:', 'Address:', 'CFO:', 'Investment Round:', 'Advisor:',]

#removing discard list from scrapelist
for i in scrapelist[:]:
    for x in discard:
        if x in i:
            scrapelist.remove(i)
            
#combine name and purpose elements into one tuple
it = iter(scrapelist)
zzz = list(zip(it, it))

#print each company in new file
count = 0
for item in zzz:
    count += 1
    filename = '{}.txt'.format(count)
    with open(filename, 'w') as f_out:
        f_out.write('{}\n'.format(item))
