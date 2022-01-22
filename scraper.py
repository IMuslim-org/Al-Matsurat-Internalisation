from bs4 import BeautifulSoup
import requests
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
arabic_file = open(f"{dir_path}/data/quranTexts.json", "w")

response = requests.get("https://almatsurat.net/sugro")
soup = BeautifulSoup(response.text)

zikirChilds = soup.findAll(attrs={'class': 'zikir-child'})
contents = []

for elementIndex in range(len(zikirChilds)):
    element = zikirChilds[elementIndex]
   
    textQurans = element.findAll(['p', 'div'], attrs={'class': 'text-quran text-justify'})
    dzkirContents = []
    for textQuran in textQurans:
        dzkirContents.append(textQuran.text)

    intro = element.find('div',attrs={'class': 'text-center'})
    title = element.find('span', attrs={'class': 'title'}).text
     
    print(title.strip())


    content = {'id':elementIndex}
    content['contents'] = dzkirContents

    if intro == None:
        pass
    else:
        content['intro'] = intro.text

    # print(content)
    contents.append(content)


arabic_file.write(str(contents).replace('\'', '"'))
