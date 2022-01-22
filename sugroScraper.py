from bs4 import BeautifulSoup
import requests
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
arabic_file = open(f"{dir_path}/data/quranTexts.json", "w")
sugro_bahasa = open(f"{dir_path}/bahasa/sugro.json", "w")

response = requests.get("https://almatsurat.net/sugro")
soup = BeautifulSoup(response.text)

zikirChilds = soup.findAll(attrs={'class': 'zikir-child'})
contents = []
translatedTextContents = []

for elementIndex in range(len(zikirChilds)):
    element = zikirChilds[elementIndex]

    content = {'id':elementIndex}
    translatedTextContent = {'id':elementIndex}
   
    textQurans = element.findAll(['p', 'div'], attrs={'class': 'text-quran text-justify'})
    intro = element.find('div',attrs={'class': 'text-center'})
    dzkirContents = []
    
    for textQuran in textQurans:
        dzkirContents.append(textQuran.text)

    if intro == None:
        pass
    else:
        content['intro'] = intro.text

    content['contents'] = dzkirContents
    contents.append(content)

    # the translation text
    
    title = element.find('span', attrs={'class': 'title'}).text
    translatedTexts = []

    textTranslatesDivs = element.findAll('div', attrs={'class': ['text-translate']})
    textTranslatesPs = element.findAll('p', attrs={'class': ['text-justify']})

    introTranslatedText = element.find('div', attrs={'class': 'text-translate'})

    if introTranslatedText is not None:
        translatedTextContent['intro'] = introTranslatedText.text


    if len(textTranslatesDivs) > 0:
        for text in textTranslatesDivs:
            translatedTexts.append(text.text)
    else:
        translatedTexts.append(textTranslatesPs[1].text)
        
    translatedTextContent['contents'] = translatedTexts
    translatedTextContents.append(translatedTextContent)
    


arabic_file.write(str(contents).replace('\'', '"'))
sugro_bahasa.write(json.dumps(translatedTextContents))
